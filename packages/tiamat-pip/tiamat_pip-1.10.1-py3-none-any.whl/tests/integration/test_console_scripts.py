import os
import logging
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

    installed_script_path = str(project.pypath_scripts_dir / "main-project-cli")
    ret = shell.run(installed_script_path, "--version")
    assert ret.returncode == 0
    assert ret.stdout.strip() == main_project.version
