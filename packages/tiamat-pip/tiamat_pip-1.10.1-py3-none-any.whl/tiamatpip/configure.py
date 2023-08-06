"""
Tiamat PIP configuration.
"""
import contextlib
import importlib.machinery
import logging
import os
import pathlib
import pprint
import re
import site
import sys
from typing import Optional
from typing import Union

from importlib_metadata import FastPath
from importlib_metadata import PathDistribution
from importlib_metadata import Prepared

log = logging.getLogger(__name__)

PYINSTALLER_IMPORTERS_REGEX = re.compile(r"pyimod([\d]{2})_importers")


class GlobalContext:
    """
    This class will hold some global runtime context information.
    """

    __slots__ = ("user_base", "user_site", "pip_command_name")

    def __init__(self):
        self.pip_command_name: str = "pip"
        self.user_base: Optional[pathlib.Path] = None
        self.user_site: Optional[pathlib.Path] = None


GLOBAL_CONTEXT = GlobalContext()
if "TIAMAT_PIP_PYPATH" in os.environ:
    GLOBAL_CONTEXT.user_base = pathlib.Path(os.environ["TIAMAT_PIP_PYPATH"]).resolve()
    GLOBAL_CONTEXT.user_site = (
        GLOBAL_CONTEXT.user_base
        / "lib"
        / "python{}.{}".format(*sys.version_info)
        / "site-packages"
    )

if GLOBAL_CONTEXT.user_base is not None:
    site.ENABLE_USER_SITE = True
    site.USER_BASE = str(GLOBAL_CONTEXT.user_base)
    site.USER_SITE = str(GLOBAL_CONTEXT.user_site)


class TiamatPipPathFinder(importlib.machinery.PathFinder):
    """
    Tiamat PIP implementation of python's PathFinder.

    A subclass of PathFinder with the intent to only try and load
    existing modules/packages from the tiamat-pip pypath.

    The reason for this is because pyinstaller specifically pushes PathFinder instances
    to the end of the sys.meta_path list, however, for our hacked pip support to work,
    we need a PathFinder instance before Pyinstaller's pyimod03_importers.FrozenImporter
    """

    path = None

    def __init__(self, path):
        if TiamatPipPathFinder.path is None:
            TiamatPipPathFinder.path = path
        log.debug(
            "Instantiating TiamatPipPathFinder(path=%s)", TiamatPipPathFinder.path
        )

    @classmethod
    def _path_importer_cache(cls, path):
        """
        Get the finder for the path entry from sys.path_importer_cache.

        If the path entry is not in the cache, find the appropriate finder
        and cache it. If no finder is available, store None.
        """
        if not path.startswith(str(TiamatPipPathFinder.path)):
            # Don't handle any other paths
            return None
        return super()._path_importer_cache(path)  # type: ignore[misc]

    @classmethod
    def find_spec(cls, fullname, path=None, target=None):
        """
        Find the spec for a module.
        """
        if path is None:
            log.debug(
                "TiamatPipPathFinder.find_spec: First time trying to load %s", fullname
            )
            assert TiamatPipPathFinder.path
            # First time trying to load
            top_level = fullname.split(".")[0]
            top_level_path = TiamatPipPathFinder.path / top_level
            if top_level_path.is_dir():
                log.debug(
                    "TiamatPipPathFinder.find_spec: %s is a directory", top_level_path
                )
                return super().find_spec(fullname, path=path, target=target)
            top_level_entries = list(TiamatPipPathFinder.path.glob(f"{top_level}.*"))
            if top_level_entries:
                log.debug(
                    "TiamatPipPathFinder.find_spec: entries found: %s",
                    top_level_entries,
                )
                return super().find_spec(fullname, path=path, target=target)
        else:
            # Previously loaded, likely the top level package
            # log.debug(
            #    "TiamatPipPathFinder.find_spec: finding previously loaded %s", fullname
            # )
            for entry in path:
                if entry.startswith(str(TiamatPipPathFinder.path)):
                    # log.debug(
                    #    "TiamatPipPathFinder.find_spec: previously loaded %s found: %s",
                    #    fullname,
                    #    entry,
                    # )
                    return super().find_spec(fullname, path=path, target=target)
        return None

    @classmethod
    def find_distributions(cls, context):
        """
        This method applies to importlib.metadata and importlib_metadata.
        """
        for entry in FastPath(TiamatPipPathFinder.path).search(Prepared(context.name)):
            yield PathDistribution(entry)


def set_user_base_path(
    user_base: Union[pathlib.Path, str],
    create: bool = True,
    create_mode: int = 0o0755,
) -> None:
    """
    Set the runtime ``user_base`` path.
    """
    if not isinstance(user_base, pathlib.Path):
        user_base = pathlib.Path(user_base)

    user_site = (
        user_base / "lib" / "python{}.{}".format(*sys.version_info) / "site-packages"
    )
    if create is True:
        with contextlib.suppress(PermissionError):
            user_site.mkdir(parents=True, exist_ok=True, mode=create_mode)

    # Make sure our pypath comes first in sys.path
    if str(user_site) in sys.path:
        sys.path.remove(str(user_site))
    sys.path.insert(0, str(user_site))

    GLOBAL_CONTEXT.user_base = user_base
    GLOBAL_CONTEXT.user_site = user_site
    site.ENABLE_USER_SITE = True
    site.USER_BASE = str(user_base)
    site.USER_SITE = str(user_site)

    refresh_pkg_resources_working_set()

    inject_index = None
    path_finder_present = False
    for idx, item in enumerate(sys.meta_path):
        name = getattr(item, "__qualname__", None)
        if name == "TiamatPipPathFinder":
            log.debug("TiamatPipPathFinder already present in sys.meta_path")
            # our TiamatPipPathFinder is already present, stop processing
            path_finder_present = True
            break
        module = getattr(item, "__module__", None)
        if module and PYINSTALLER_IMPORTERS_REGEX.match(module):
            # We found Pyinstaller's FrozenImporter, our TiamatPipPathFinder
            # needs to be added in front of it. Store the index.
            inject_index = idx
            break

    if inject_index:
        # Insert our TiamatPipPathFinder before Pyinstaller's FrozenImporter
        log.debug(
            "Injecting TiamatPipPathFinder instance into sys.meta_path index: %s",
            inject_index,
        )
        sys.meta_path.insert(inject_index, TiamatPipPathFinder(user_site))
    elif path_finder_present is False:
        log.debug(
            "Did NOT inject TiamatPipPathFinder into sys.meta_path: %s", sys.meta_path
        )


def unset_user_base_path() -> None:
    """
    Remove tiamat-pip's pypath from the python import machinery.
    """
    refresh_pkg_resources_working_set(include_pypath=False)

    exclude_index = None
    for idx, item in enumerate(sys.meta_path):
        if isinstance(item, TiamatPipPathFinder):
            exclude_index = idx
            break
    if exclude_index:
        log.debug(
            "Removing TiamatPipPathFinder instance from sys.meta_path at index: %s",
            exclude_index,
        )
        sys.meta_path.pop(exclude_index)

    str_user_site = str(get_user_site_path())
    if str_user_site in sys.path:
        log.debug("Removing pypath from sys.path")
        sys.path.remove(str_user_site)


def get_user_base_path() -> Optional[pathlib.Path]:
    """
    Get the runtime ``user_base`` path.
    """
    return GLOBAL_CONTEXT.user_base


def get_user_site_path() -> Optional[pathlib.Path]:
    """
    Get the runtime ``user_site`` path.
    """
    return GLOBAL_CONTEXT.user_site


def set_pip_command_name(name: str) -> None:
    """
    Set the runtime ``pip_command_name``.
    """
    GLOBAL_CONTEXT.pip_command_name = name


def get_pip_command_name() -> str:
    """
    Get the runtime ``pip_command_name``.
    """
    return GLOBAL_CONTEXT.pip_command_name


def refresh_pkg_resources_working_set(
    include_pypath: bool = True, exclude_builtin: bool = False
) -> None:
    """
    Refresh `pkg_resources.working_set`.
    """
    try:
        import pkg_resources

        user_site_path = str(get_user_site_path())
        if exclude_builtin:
            log.debug(
                "Starting with a clean pkg_resources.working_set to exclude "
                "the internal paths."
            )
            entries = []
        else:
            entries = list(pkg_resources.working_set.entries)
        log.debug("pkg_resources.working_set.entries:\n%s", pprint.pformat(entries))
        if include_pypath:
            log.debug(
                "Clearing pkg_resources.working_set to give preference to "
                "tiamat-pip's pypath"
            )
            entries.insert(0, user_site_path)
        else:
            log.debug(
                "Refreshing pkg_resources.working_set, excluding tiamat-pip's pypath"
            )
        pkg_resources.working_set.entries.clear()
        pkg_resources.working_set.entry_keys.clear()  # type: ignore[attr-defined]
        pkg_resources.working_set.by_key.clear()  # type: ignore[attr-defined]
        try:
            pkg_resources.working_set.normalized_to_canonical_keys.clear()  # type: ignore[attr-defined]
        except AttributeError:
            # Older version of setuptools, < 62.0.0
            pass
        for entry in entries:
            pkg_resources.working_set.add_entry(entry)
    except ImportError:
        pass
