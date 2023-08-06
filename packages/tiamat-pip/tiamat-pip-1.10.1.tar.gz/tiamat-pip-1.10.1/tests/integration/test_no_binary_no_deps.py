import logging
import os

import pytest

from tests.conftest import Package
from tests.conftest import package_ids
from tests.support.helpers import TiamatPipProject

log = logging.getLogger(__name__)


@pytest.fixture(
    scope="module",
    params=[
        Package("black", version="22.6.0", upgrade="22.8.0"),
    ],
    ids=package_ids,
)
def package(request):
    return request.param


@pytest.fixture(scope="module")
def project(request, tmp_path_factory):
    name = "tiamat-no-binary-no-deps"
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


@pytest.mark.xfail(reason="Expected failure for issue #14")
def test_install_no_binary_no_deps(project, package):
    installed_packages = project.get_installed_packages()
    assert package.name not in installed_packages

    # Installing docker compose will bump docopt to 0.6.0
    ret = project.run(
        "pip",
        "install",
        "--no-binary",
        ":all:",
        "--no-deps",
        f"{package.name}=={package.version}",
    )
    assert ret.returncode == 0
    installed_packages = project.get_installed_packages()
    assert package.name in installed_packages
    assert installed_packages[package.name] == package.version
