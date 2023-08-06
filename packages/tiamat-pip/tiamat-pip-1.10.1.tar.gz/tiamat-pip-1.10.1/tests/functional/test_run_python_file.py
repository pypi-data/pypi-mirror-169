import pytest

from tiamatpip.cli import run_python_file


def test_run_python_file_valid():
    with pytest.raises(SystemExit) as e:
        run_python_file([__file__])
    assert e.value.code == 0


def test_run_python_file_invalid():
    with pytest.raises(SystemExit) as e:
        run_python_file(["no_such_file_exists.py"])
    assert e.value.code == 1
