"""
Test single python module packages installations.

This test is important because doctop imports itself in setup.py during install
to know it's own version.
"""
import pytest
from packaging import version

from tests.conftest import Package
from tests.conftest import package_ids


@pytest.fixture(
    scope="module",
    params=[
        Package("docopt", version="0.5.0", upgrade="0.6.2"),
    ],
    ids=package_ids,
)
def package(request):
    return request.param


@pytest.fixture(scope="module", params=["pypath", "builtin"])
def package_type(request):
    return request.param


def test_docopt(project, package, package_type):
    project.run_common_tests(package, package_type)


def test_docker_compose_with_older_docopt(project, package, package_type):
    compose_package = "docker-compose"
    compose_package_version = "1.29.2"

    installed_packages = project.get_installed_packages(
        include_frozen=package_type == "builtin"
    )
    assert package.name in installed_packages
    assert installed_packages[package.name] == package.version

    # Installing docker compose will bump docopt to 0.6.0
    ret = project.run("pip", "install", f"{compose_package}=={compose_package_version}")
    assert ret.returncode == 0
    if package_type == "builtin":
        assert (
            f"Found existing installation: {package.name} {package.version}"
            not in ret.stdout
        )
        assert f"Uninstalling {package.name}-{package.version}" not in ret.stdout
    else:
        assert (
            f"Found existing installation: {package.name} {package.version}"
            in ret.stdout
        )
        assert f"Uninstalling {package.name}-{package.version}" in ret.stdout
    installed_packages = project.get_installed_packages()
    assert package.name in installed_packages
    assert version.parse(installed_packages[package.name]) >= version.parse(
        package.version
    )
    assert compose_package in installed_packages
    assert installed_packages[compose_package] == compose_package_version
