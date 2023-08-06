"""
Tiamat pip related utilities.
"""
import logging
import os
import pprint
import sys
from contextlib import contextmanager
from typing import Any
from typing import Dict
from typing import Generator
from typing import List
from typing import Optional
from typing import Sequence


log = logging.getLogger(__name__)


@contextmanager
def patched_environ(
    *, environ: Optional[Dict[str, str]] = None, **kwargs: str
) -> Generator[None, None, None]:
    """
    Context manager to patch ``os.environ``.
    """
    _environ = environ.copy() if environ else {}
    _environ.update(**kwargs)
    old_values = {}
    try:
        for key, value in _environ.items():
            msg_prefix = "Setting"
            if key in os.environ:
                msg_prefix = "Updating"
                old_values[key] = os.environ[key]
            log.debug(f"{msg_prefix} environ variable {key} to: '{value}'")
            os.environ[key] = value
        yield
    finally:
        for key in _environ:
            if key in old_values:
                log.debug(f"Restoring environ variable {key} to: '{old_values[key]}'")
                os.environ[key] = old_values[key]
            else:
                if key in os.environ:
                    log.debug(f"Removing environ variable {key}")
                    os.environ.pop(key)


@contextmanager
def patched_sys_argv(argv: Sequence[str]) -> Generator[None, None, None]:
    """
    Context manager to patch ``sys.argv``.
    """
    previous_sys_argv = list(sys.argv)
    try:
        log.debug(f"Patching sys.argv to: {argv}")
        sys.argv[:] = argv
        yield
    finally:
        log.debug(f"Restoring sys.argv to: {previous_sys_argv}")
        sys.argv[:] = previous_sys_argv


@contextmanager
def prepend_sys_path(
    *paths: str, excludes: Optional[List[str]] = None
) -> Generator[None, None, None]:
    """
    Context manager to prepend the passed paths to ``sys.path``.
    """
    previous_sys_path = list(sys.path)
    if excludes:
        log.debug("Exluding from sys.path: %s", excludes)
        for path in excludes:
            if path in sys.path:
                sys.path.remove(path)
    try:
        log.debug("Prepending sys.path with: %s", list(paths))
        for path in reversed(list(paths)):
            sys.path.insert(0, path)
        yield
    finally:
        log.debug(f"Restoring sys.path to: {previous_sys_path}")
        sys.path[:] = previous_sys_path


@contextmanager
def debug_print(
    funcname: str, argv: List[str], **extra: Any
) -> Generator[None, None, None]:
    """
    Helper debug function.
    """
    try:
        indent = "  " * getattr(debug_print, "__indent__")
        debug_print.__indent__ += 1  # type: ignore[attr-defined]
    except AttributeError:
        indent = ""
        debug_print.__indent__ = 1  # type: ignore[attr-defined]

    prefixes_of_interest = (
        "TIAMAT_",
        "LD_",
        "C_",
        "CPATH",
        "CWD",
        "PYTHON",
        "PIP_",
    )
    environ: Dict[str, Any] = {}
    for key, value in os.environ.items():
        if key.startswith(prefixes_of_interest):
            environ[key] = value

    header = f"Func: {funcname}"
    tail_len = 70 - len(header) - 5
    environ_str = "\n".join(
        f"{indent}    {line}" for line in pprint.pformat(environ).splitlines()
    )
    # Include sys.path in the debug output
    sys_path_str = "\n".join(
        f"{indent}    {line}" for line in pprint.pformat(sys.path).splitlines()
    )
    argv_str = "\n".join(
        f"{indent}    {line}" for line in pprint.pformat(argv).splitlines()
    )
    message = (
        f"{indent}>>> {header} " + ">" * tail_len + "\n"
        f"{indent}  CWD: {os.getcwd()}\n"
        f"{indent}  ENVIRON:\n{environ_str}\n"
        f"{indent}  sys.path:\n{sys_path_str}\n"
        f"{indent}  ARGV:\n{argv_str}\n"
    )
    if extra:
        message += f"{indent}  EXTRA:\n"
        for key, value in extra.items():
            message += f"{indent}    {key}: {value}\n"
    log.debug(message)
    try:
        yield
    finally:
        message = f"{indent}<<< {header} " + "<" * tail_len + "\n"
        log.debug(message)
        debug_print.__indent__ -= 1  # type: ignore[attr-defined]
