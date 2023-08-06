import logging
import os
import sys

import pytest

from tests.support.helpers import TiamatPipProject

log = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def project(request, tmp_path_factory, main_project):
    name = "tiamat-console-scripts"
    instance = TiamatPipProject(
        name=name,
        path=tmp_path_factory.mktemp(name, numbered=False),
        one_dir=request.config.getoption("--singlebin") is False,
    )
    with instance:
        if os.environ.get("CI_RUN", "0") == "0":
            instance.copy_generated_project_to_temp()
        try:
            log.info("Using built Project: %s", instance)
            yield instance
        finally:
            instance.delete_pypath()


def test_package_console_scripts(project, main_project, shell):
    installed_packages = project.get_installed_packages(include_frozen=True)
    assert main_project.name not in installed_packages

    ret = project.run("pip", "install", str(main_project.get_wheel_package_path()))
    assert ret.returncode == 0

    installed_packages = project.get_installed_packages(include_frozen=True)
    assert main_project.name in installed_packages
    assert installed_packages[main_project.name] == main_project.version

    log.debug("SCRIPTS IN DIR: %s", list(project.pypath_scripts_dir.glob("*")))
    installed_cli_path = project.pypath_scripts_dir / "main-project-cli"
    expected_cli_output = f"{installed_cli_path.name} {main_project.version}"
    if sys.platform.startswith("win"):
        installed_cli_path = installed_cli_path.with_suffix(".exe")
    else:
        log.debug("Installed CLI Contents:\n%s", installed_cli_path.read_text().strip())
    ret = shell.run(str(installed_cli_path), "--version", env={"TIAMAT_PIP_DEBUG": "1"})
    assert ret.cmdline[0] == str(installed_cli_path)
    assert "No command?!" not in ret.stdout
    assert ret.returncode == 0
    assert ret.stdout.strip() == expected_cli_output

    if sys.platform.startswith("win"):
        # Stop testing. The code below will NOT work on windows
        return

    installed_script_path = project.pypath_scripts_dir / "main-project-script"
    expected_script_output = f"{installed_script_path.name} {main_project.version}"
    log.debug(
        "Installed Script Contents:\n%s", installed_script_path.read_text().strip()
    )
    ret = shell.run(
        str(installed_script_path), "--version", env={"TIAMAT_PIP_DEBUG": "1"}
    )
    assert ret.cmdline[0] == str(installed_script_path)
    assert "No command?!" not in ret.stdout
    assert ret.returncode == 0
    assert ret.stdout.strip() == expected_script_output
