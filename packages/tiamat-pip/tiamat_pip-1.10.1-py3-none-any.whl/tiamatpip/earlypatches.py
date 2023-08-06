import sys
import logging

log = logging.getLogger(__name__)

from typing import Optional
import pip._internal.metadata
import pip._internal.req.req_install
from pip._internal.req.req_install import InstallRequirement
from pip._internal.req.req_uninstall import UninstallPathSet


class TiamatPipInstallRequirement(InstallRequirement):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        log.warning("DIST InstallRequirement: %s", self)

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
        from pip._internal.req.req_uninstall import UninstallPathSet
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
pip._internal.req.req_install.InstallRequirement = TiamatPipInstallRequirement
