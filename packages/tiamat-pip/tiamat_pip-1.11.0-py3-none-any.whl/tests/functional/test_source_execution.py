import logging
import os

import pytest

from tests.support.helpers import TiamatPipProject

log = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def project(request, tmp_path_factory):
    name = "tiamat-source-execution"
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


def test_raw_python(project, subtests):
    with subtests.test("exitcode with no exception"):
        # Some pip calls shell out to python with -c or python foo.py; verify
        # that when -c is used, it doesn't continue back in to user code.
        ret = project.run("-c", "print('-c SENTINEL')", env={"TIAMAT_PIP_INSTALL": "1"})
        assert ret.returncode == 0
        assert "-c SENTINEL" in ret.stdout
        assert (
            "No command" not in ret.stdout
        ), '`binary -c "..."` should terminate execution'

    with subtests.test("exitcode with exception"):
        # If -c code raises an exception, we should see the exception and an error code.
        ret = project.run("-c", "raise Exception()", env={"TIAMAT_PIP_INSTALL": "1"})
        assert ret.returncode == 1
        assert "Traceback (most recent call last)" in ret.stderr
        assert (
            "No command" not in ret.stdout
        ), '`binary -c "..."` should terminate execution'
