import sys
import logging
import pathlib
from typing import List
from typing import Optional
from typing import Sequence

import pip._internal.metadata
import pip._internal.req.req_install
from pip._internal.models.scheme import Scheme
from pip._internal.req.req_install import InstallRequirement
from pip._internal.req.req_uninstall import UninstallPathSet

log = logging.getLogger(__name__)


class TiamatPipScheme(Scheme):
    """
    Custom platform scheme to support tiamat-pip.
    """

    def __init__(self):
        base = get_user_base_path()
        prefix = get_user_site_path()
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
        import tiamatpip.utils

        tiamatpip.utils.patch_get_scheme()
        tiamatpip.utils.patch_get_scheme_distutils()
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
        """
        Uninstall the distribution currently satisfying this requirement.
        Prompts before removing or modifying files unless
        ``auto_confirm`` is True.
        Refuses to delete or modify files outside of ``sys.prefix`` -
        thus uninstallation within a virtual environment can only
        modify that virtual environment, even if the virtualenv is
        linked to global site-packages.
        """
        # This is a 1:1 copy of the same class and method as seen in pip's source
        # with the difference that we call our own get_default_environment function
        import tiamatpip.utils

        # This is a 1 to to copy of the method contents, adjusted to
        # deny uninstalling tiamat built-in packages
        assert self.req
        dist = tiamatpip.utils.get_default_environment().get_distribution(self.req.name)
        if not dist:
            log.warning("Skipping %s as it is not installed.", self.name)
            return None
        log.info("Found existing installation: %s", dist)

        log.warning("DIST3: %s", dist)

        uninstalled_pathset = UninstallPathSet.from_dist(dist)
        uninstalled_pathset.remove(auto_confirm, verbose)
        return uninstalled_pathset


# Overwrite pip's InstallRequirement with out own
pip._internal.req.req_install.InstallRequirement = TiamatPipInstallRequirement  # type: ignore[misc]
