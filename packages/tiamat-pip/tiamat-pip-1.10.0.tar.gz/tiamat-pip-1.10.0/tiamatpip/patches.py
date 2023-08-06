import logging
import pathlib
import sys
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Sequence
from typing import TYPE_CHECKING

import pip._internal.metadata
import pip._internal.req.req_install
from pip._internal.models.scheme import Scheme
from pip._internal.req.req_install import InstallRequirement
from pip._internal.req.req_uninstall import UninstallPathSet

from tiamatpip import configure

log = logging.getLogger(__name__)

# Hold a reference to the real function
real_get_environment = pip._internal.metadata.get_environment


class TiamatPipScheme(Scheme):
    """
    Custom platform scheme to support tiamat-pip.
    """

    def __init__(self):
        base = configure.get_user_base_path()
        prefix = configure.get_user_site_path()
        if TYPE_CHECKING:
            assert base
            assert prefix
        if not sys.platform.lower().startswith("win"):
            scripts_path = base / "bin"
        else:
            scripts_path = base / "Scripts"
        meipass = pathlib.Path(sys._MEIPASS)  # type: ignore[attr-defined]
        self.platlib = str(prefix)
        self.purelib = str(prefix)
        self.headers = str(meipass / "include")
        self.scripts = str(scripts_path)
        self.data = str(prefix)

    def __repr__(self):
        """
        Return a string representation of the class.
        """
        return (
            f"<TiamatPipScheme "
            f"platlib={self.platlib} "
            f"purelib={self.purelib} "
            f"headers={self.headers} "
            f"scripts={self.scripts} "
            f"data={self.data}>"
        )

    def to_dict(self) -> Dict[str, str]:
        """
        Return the instance attributes as a dictionary.
        """
        return {
            "platlib": self.platlib,
            "purelib": self.purelib,
            "headers": self.headers,
            "scripts": self.scripts,
            "data": self.data,
        }


class TiamatPipInstallRequirement(InstallRequirement):
    """
    Replacement for pip's InstallRequirement which is aware of tiamat-pip.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        log.warning("DIST InstallRequirement: %s", self)

    def install(
        self,
        install_options: List[str],
        global_options: Optional[Sequence[str]] = None,
        root: Optional[str] = None,
        home: Optional[str] = None,
        prefix: Optional[str] = None,
        warn_script_location: bool = True,
        use_user_site: bool = False,
        pycompile: bool = True,
    ) -> None:
        patch_get_scheme()
        super().install(
            install_options,
            global_options=global_options,
            root=root,
            home=home,
            prefix=prefix,
            warn_script_location=False,
            use_user_site=use_user_site,
            pycompile=pycompile,
        )

    def uninstall(
        self, auto_confirm: bool = False, verbose: bool = False
    ) -> Optional[UninstallPathSet]:
        # This is a 1 to to copy of the method contents, adjusted to
        # deny uninstalling tiamat built-in packages
        assert self.req
        dist = get_environment([]).get_distribution(self.req.name)
        if not dist:
            log.warning("Skipping %s as it is not installed.", self.name)
            return None
        log.info("Found existing installation: %s", dist)

        log.warning("DIST3: %s", dist)

        uninstalled_pathset = UninstallPathSet.from_dist(dist)
        uninstalled_pathset.remove(auto_confirm, verbose)
        return uninstalled_pathset


def get_environment(paths):
    """
    Patched ``pip._internal.metadata.get_environment`` to include tiamat-pip paths.
    """
    log.debug(
        "Using patched ``pip._internal.metadata.get_environment`` to include tiamat-pip paths"
    )
    user_base_path = configure.get_user_base_path()
    assert user_base_path
    user_site_path = configure.get_user_site_path()
    assert user_site_path
    _paths = [
        str(user_base_path),
        str(user_site_path),
    ]
    if paths:
        for path in paths:
            if path not in _paths:
                _paths.append(path)
    return real_get_environment(paths=_paths)


def patch_pip_internal_metadata_get_environment() -> None:
    """
    Patch ``pip._internal.metadata.get_environment``.
    """
    log.debug(
        "Patching 'pip._internal.metadata.get_environment' to include the tiamat-pip pypath site packages"
    )
    pip._internal.metadata.get_environment = get_environment


def get_lib_location_guesses(
    user: bool = False,
    home: Optional[str] = None,
    root: Optional[str] = None,
    isolated: bool = False,
    prefix: Optional[str] = None,
) -> List[str]:
    """
    Patched 'pip._internal.commands.install.get_lib_location_guesses'.

    This method will return the paths proper for a tiamat-pip install.
    """
    scheme = get_tiamat_pip_scheme()
    return [scheme.purelib, scheme.platlib]


def get_tiamat_pip_scheme(*args: Any, **kwargs: Any) -> TiamatPipScheme:
    """
    Override pip's get_scheme calls.

    This allows us to always return a scheme proper for tiamat-pip.
    """
    scheme = TiamatPipScheme()
    log.debug(
        "Using custom TiamatPipScheme to work with tiamat-pip directory structure: %s",
        scheme,
    )
    return scheme


def patch_get_scheme() -> None:
    """
    Patch a couple of pip functions to work with tiamat-pip.
    """
    import pip._internal.commands.install

    log.debug(
        "Patching 'pip._internal.commands.install.get_lib_location_guesses' to work with tiamat-pip"
    )
    pip._internal.commands.install.get_lib_location_guesses = get_lib_location_guesses
    log.debug(
        "Patching 'pip._internal.req.req_install.get_scheme' to work with tiamat-pip"
    )
    pip._internal.req.req_install.get_scheme = get_tiamat_pip_scheme  # type: ignore[attr-defined]


def patch_get_scheme_distutils() -> None:
    """
    Patch 'distutils.command.install.INSTALL_SCHEMES' to work with tiamat-pip.
    """
    import distutils.command.install

    scheme = TiamatPipScheme()
    log.debug(
        "Patching 'distutils.command.install.INSTALL_SCHEMES' to work with tiamat-pip"
    )
    for key in distutils.command.install.INSTALL_SCHEMES:
        distutils.command.install.INSTALL_SCHEMES[key] = scheme.to_dict()
    distutils.command.install._inject_headers = (  # type: ignore[attr-defined]
        lambda name, scheme: get_tiamat_pip_scheme().to_dict()
    )


# Overwrite pip's InstallRequirement with out own
pip._internal.req.req_install.InstallRequirement = TiamatPipInstallRequirement  # type: ignore[misc]
