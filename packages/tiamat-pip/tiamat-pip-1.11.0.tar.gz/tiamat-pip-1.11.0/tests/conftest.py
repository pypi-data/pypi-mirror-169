import logging
import os
import pathlib
import shutil
from typing import Optional

import attr
import pytest

import tiamatpip
from tests.support.helpers import SourceProject
from tests.support.helpers import TiamatPipProject

log = logging.getLogger(__name__)

CODE_ROOT = pathlib.Path(tiamatpip.__file__).resolve().parent.parent


@attr.s(frozen=True, slots=True)
class Package:
    name: str = attr.ib()
    version: str = attr.ib()
    upgrade: str = attr.ib()
    altname: Optional[str] = attr.ib(default=None)


def package_ids(value):
    return f"{value.name}=={value.version}"


@pytest.fixture(scope="module", params=["pypath"])
def package_type(request):
    return request.param


@pytest.fixture(
    scope="module",
    params=[
        Package(name="pep8", version="1.7.0", upgrade="1.7.1"),
    ],
    ids=package_ids,
)
def package(request):
    return request.param


@pytest.fixture(scope="module")
def built_project(request, tmp_path_factory, package, package_type):
    name = f"tiamat-{package.name}-{package.version.replace('.', '_')}-{package_type}"
    requirements = []
    if package_type == "builtin":
        requirements.append(f"{package.name}=={package.version}")
    instance = TiamatPipProject(
        name=name,
        path=tmp_path_factory.mktemp(name, numbered=False),
        one_dir=request.config.getoption("--singlebin") is False,
        requirements=requirements,
    )
    with instance:
        if os.environ.get("CI_RUN", "0") == "0":
            instance.copy_generated_project_to_temp()
        yield instance


@pytest.fixture
def project(built_project, package, package_type):
    try:
        log.info("Using built Project: %s", built_project)
        if package_type == "pypath":
            installed_packages = built_project.get_installed_packages()
            assert package.name not in installed_packages
            ret = built_project.run(
                "pip", "install", f"{package.name}=={package.version}"
            )
            assert ret.returncode == 0
        yield built_project
    finally:
        built_project.delete_pypath()


@pytest.fixture(scope="session")
def projects_dir(tmp_path_factory):
    dirpath = tmp_path_factory.mktemp("projects", numbered=False)
    try:
        yield dirpath
    finally:
        shutil.rmtree(dirpath, ignore_errors=True)


@pytest.fixture(scope="session")
def main_project(projects_dir, shell):
    project = SourceProject(
        name="tiamat-pip-main-project",
        version="1.0.0",
        pkgname="pkg1",
        projects_dir=projects_dir,
    )
    log.info(f"Building {project}")
    project.write_pyproject()
    # project.write_setup_py()
    main_project_cli_name = "main-project-cli"
    main_project_script_name = "main-project-script"
    setup_cfg_contents = f"""
    [metadata]
    name = {project.name}
    version = attr: {project.pkgname}.VERSION

    [options]
    packages = find:
    scripts = scripts/{main_project_script_name}

    [options.entry_points]
    console_scripts =
        {main_project_cli_name} = {project.pkgname}:main
    """
    project.write_setup_cfg(setup_cfg_contents)
    init_module_contents = f"""
    import sys
    import json
    import argparse

    VERSION='{project.version}'

    def print_data():
        data = {{
            "name": "{project.name}",
            "pkgname": "{project.pkgname}",
            "version": VERSION,
            "argv": sys.argv
        }}
        sys.stdout.write(json.dumps(data))
        sys.stdout.flush()

    def main():
        parser = argparse.ArgumentParser()
        parser.add_argument('--version', action='version', version=f'%(prog)s {{VERSION}}')
        parser.add_argument("--data", action="store_true", default=False)
        options = parser.parse_args()
        if options.data:
            print_data()
            parser.exit(0)
        parser.exit(1)

    if __name__ == '__main__':
        main()
    """
    project.write_init_module(init_module_contents)
    scripts_dir = project.path / "scripts"
    scripts_dir.mkdir()
    script_contents = f"""
    #!/usr/bin/env python
    from {project.pkgname} import main

    if __name__ == '__main__':
        main()
    """
    project.write_file(scripts_dir / main_project_script_name, script_contents)
    ret = shell.run("python", "-m", "build", "--wheel", cwd=project.path)
    assert ret.returncode == 0
    return project


# ----- CLI Options Setup ------------------------------------------------------------------------>
def pytest_addoption(parser):
    """
    Register argparse-style options and ini-style config values.
    """
    test_selection_group = parser.getgroup("Tests Selection")
    test_selection_group.addoption(
        "--singlebin",
        default=False,
        help="Choose singlebin instead of onedir to run the tests agaist.",
    )


# <---- CLI Options Setup -------------------------------------------------------------------------
