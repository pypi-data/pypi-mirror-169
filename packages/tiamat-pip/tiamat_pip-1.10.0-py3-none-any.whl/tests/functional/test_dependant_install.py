import logging
import os
import pathlib
import shutil
import textwrap

import attr
import pytest

from tests.conftest import CODE_ROOT
from tests.support.helpers import TiamatPipProject

log = logging.getLogger(__name__)

PROJECTS_PATH = CODE_ROOT / "tests" / "projects"


@attr.s(frozen=True, slots=True)
class Project:
    name: str = attr.ib()
    version: str = attr.ib()
    pkgname: str = attr.ib()
    projects_dir: pathlib.Path = attr.ib(repr=False)
    path: pathlib.Path = attr.ib(init=False)
    pkg_path: pathlib.Path = attr.ib(init=False, repr=False)
    dist_path: pathlib.Path = attr.ib(init=False, repr=False)

    @path.default
    def _path_default(self):
        path = self.projects_dir / self.name
        path.mkdir()
        return path

    @pkg_path.default
    def _pkg_path_default(self):
        path = self.path / self.pkgname
        path.mkdir()
        return path

    @dist_path.default
    def _dist_path_default(self):
        return self.path / "dist"

    def get_wheel_package_path(self):
        return list(self.dist_path.glob("*.whl"))[0]

    def write_pyproject(self, contents):
        if contents.startswith("\n"):
            contents = contents[1:]
        if not contents.endswith("\n"):
            contents += "\n"
        contents = textwrap.dedent(contents)
        path = self.path / "pyproject.toml"
        filename = f" {path.name} "
        log.info(
            f"Writing {path}\n"
            f"{filename.center(80, '>')}\n"
            f"{contents.rstrip()}\n"
            f"{filename.center(80, '<')}"
        )
        path.write_text(contents)

    def write_init_module(self, contents):
        if contents.startswith("\n"):
            contents = contents[1:]
        if not contents.endswith("\n"):
            contents += "\n"
        contents = textwrap.dedent(contents)
        path = self.pkg_path / "__init__.py"
        filename = f" {path.name} "
        log.info(
            f"Writing {path}\n"
            f"{filename.center(80, '>')}\n"
            f"{contents.rstrip()}\n"
            f"{filename.center(80, '<')}"
        )
        path.write_text(contents)


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
        # str(CODE_ROOT / "deps" / "pip-22.2.2"),
        f"file:///{main_project.path}",
        # "trepan3k",
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
