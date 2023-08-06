import logging
import os
import shutil

import pytest

from tests.support.helpers import Project
from tests.support.helpers import TiamatPipProject

log = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def projects_dir(tmp_path_factory):
    dirpath = tmp_path_factory.mktemp("projects", numbered=False)
    try:
        yield dirpath
    finally:
        shutil.rmtree(dirpath, ignore_errors=True)


@pytest.fixture(scope="module")
def main_project(projects_dir, shell):
    project = Project(
        name="tiamat-pip-main-project",
        version="1.0.0",
        pkgname="pkg1",
        projects_dir=projects_dir,
    )
    pyproject_contents = f"""
    [build-system]
    requires = ["setuptools"]
    build-backend = "setuptools.build_meta"

    [project]
    name = "{project.name}"
    classifiers = [
        "Programming Language :: Python :: 3",
    ]
    dynamic = ["version"]

    [tool.setuptools]
    packages = ["{project.pkgname}"]

    [tool.setuptools.dynamic]
    version = {{attr = "{project.pkgname}.VERSION"}}
    """
    log.info(f"Building {project}")
    project.write_pyproject(pyproject_contents)
    init_module_contents = f"""
    VERSION='{project.version}'
    """
    project.write_init_module(init_module_contents)
    ret = shell.run("python", "-m", "build", "--wheel", cwd=project.path)
    assert ret.returncode == 0
    return project


@pytest.fixture(scope="module")
def dependant_project(projects_dir, main_project, shell):
    project = Project(
        name="tiamat-pip-main-project-dependant",
        version="2.0.0",
        pkgname="pkg2",
        projects_dir=projects_dir,
    )
    pyproject_contents = f"""
    [build-system]
    requires = ["setuptools"]
    build-backend = "setuptools.build_meta"

    [project]
    name = "{project.name}"
    classifiers = [
        "Programming Language :: Python :: 3",
    ]

    dependencies = [
      "{main_project.name} >= {main_project.version}"
    ]
    dynamic = ["version"]

    [tool.setuptools]
    packages = ["{project.pkgname}"]

    [tool.setuptools.dynamic]
    version = {{attr = "{project.pkgname}.VERSION"}}
    """
    log.info(f"Building {project}")
    project.write_pyproject(pyproject_contents)
    init_module_contents = f"""
    VERSION='{project.version}'
    """
    project.write_init_module(init_module_contents)
    ret = shell.run("python", "-m", "build", "--wheel", cwd=project.path)
    assert ret.returncode == 0
    return project


@pytest.fixture(scope="module")
def project(request, tmp_path_factory, main_project):
    name = "tiamat-dependant-project"
    requirements = [
        f"file:///{main_project.path}",
    ]
    instance = TiamatPipProject(
        name=name,
        path=tmp_path_factory.mktemp(name, numbered=False),
        one_dir=request.config.getoption("--singlebin") is False,
        requirements=requirements,
    )
    with instance:
        if os.environ.get("CI_RUN", "0") == "0":
            instance.copy_generated_project_to_temp()
        try:
            log.info("Using built Project: %s", instance)
            yield instance
        finally:
            instance.delete_pypath()


def test_dependant_project_install(project, main_project, dependant_project):
    installed_packages = project.get_installed_packages(include_frozen=True)
    assert main_project.name in installed_packages
    assert installed_packages[main_project.name] == main_project.version
    assert dependant_project.name not in installed_packages

    ret = project.run("pip", "install", str(dependant_project.get_wheel_package_path()))
    assert ret.returncode == 0

    installed_packages = project.get_installed_packages()
    assert dependant_project.name in installed_packages
    assert installed_packages[dependant_project.name] == dependant_project.version

    ret = project.run("pip", "uninstall", "-y", dependant_project.name)
    assert ret.returncode == 0
    assert "as it is not installed" not in ret.stderr

    installed_packages = project.get_installed_packages()
    assert dependant_project.name not in installed_packages

    installed_packages = project.get_installed_packages(include_frozen=True)
    assert main_project.name in installed_packages
    assert installed_packages[main_project.name] == main_project.version
    assert dependant_project.name not in installed_packages

    ret = project.run("pip", "uninstall", "-y", main_project.name)
    assert "as it is not installed" in ret.stderr
