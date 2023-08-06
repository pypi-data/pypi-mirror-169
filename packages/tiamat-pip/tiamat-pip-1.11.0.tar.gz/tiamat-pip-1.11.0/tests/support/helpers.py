import logging
import pathlib
import random
import shutil
import string
import sys
import tempfile
import textwrap
from subprocess import CalledProcessError
from typing import cast
from typing import List
from typing import Optional

import attr
import PyInstaller
from pytestshellutils.customtypes import EnvironDict
from pytestshellutils.shell import Subprocess
from pytestshellutils.utils.processes import ProcessResult

import tiamatpip
from tiamatpip.store import parse_package_name
from tiamatpip.store import Store

log = logging.getLogger(__name__)

CODE_ROOT = pathlib.Path(tiamatpip.__file__).resolve().parent.parent


def random_string(
    prefix: str,
    size: int = 6,
    uppercase: bool = True,
    lowercase: bool = True,
    digits: bool = True,
) -> str:
    """
    Generates a random string.

    :keyword str prefix: The prefix for the random string
    :keyword int size: The size of the random string
    :keyword bool uppercase: If true, include upper-cased ascii chars in choice sample
    :keyword bool lowercase: If true, include lower-cased ascii chars in choice sample
    :keyword bool digits: If true, include digits in choice sample
    :return str: The random string
    """
    if not any([uppercase, lowercase, digits]):
        raise RuntimeError(
            "At least one of 'uppercase', 'lowercase' or 'digits' needs to be true"
        )
    choices: List[str] = []
    if uppercase:
        choices.extend(string.ascii_uppercase)
    if lowercase:
        choices.extend(string.ascii_lowercase)
    if digits:
        choices.extend(string.digits)

    return prefix + "".join(random.choice(choices) for _ in range(size))


@attr.s(frozen=True, slots=True)
class SourceProject:
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

    def write_pyproject(self, contents=None):
        if contents is None:
            contents = """
            [build-system]
            requires = ["setuptools"]
            build-backend = "setuptools.build_meta"
            """
        path = self.path / "pyproject.toml"
        self.write_file(path, contents)

    def write_setup_py(self, contents=None):
        if contents is None:
            contents = """
            import setuptools

            if __name__ == "__main__":
                setuptools.setup()
            """
        path = self.path / "setup.py"
        self.write_file(path, contents)

    def write_setup_cfg(self, contents):
        path = self.path / "setup.cfg"
        self.write_file(path, contents)

    def write_init_module(self, contents):
        path = self.pkg_path / "__init__.py"
        self.write_file(path, contents)

    def write_file(self, fpath, contents):
        if contents.startswith("\n"):
            contents = contents[1:]
        if not contents.endswith("\n"):
            contents += "\n"
        contents = textwrap.dedent(contents)
        filename = f" {fpath.name} "
        log.info(
            f"Writing {fpath}\n"
            f"{filename.center(80, '>')}\n"
            f"{contents.rstrip()}\n"
            f"{filename.center(80, '<')}"
        )
        fpath.write_text(contents)


@attr.s(kw_only=True, slots=True)
class TiamatPipProject:
    name: str = attr.ib()
    path: pathlib.Path = attr.ib()
    one_dir: bool = attr.ib(default=True)
    pypath: pathlib.Path = attr.ib(init=False)
    pypath_scripts_dir: pathlib.Path = attr.ib(init=False)
    build_conf_contents: str = attr.ib()
    run_py_contents: str = attr.ib()
    requirements: List[str] = attr.ib(default=attr.Factory(list))
    requirements_txt_contents: str = attr.ib()
    build_conf: pathlib.Path = attr.ib(init=False)
    run_py: Optional[pathlib.Path] = attr.ib(init=False)
    requirements_txt: Optional[pathlib.Path] = attr.ib(init=False)
    subprocess: Subprocess = attr.ib(init=False)

    @name.default
    def _default_name(self) -> str:
        return random_string("project-")

    @pypath.default
    def _default_pypath(self) -> pathlib.Path:
        pypath = self.path / "pypath"
        pypath.mkdir(parents=True, exist_ok=True, mode=0o755)
        return pypath

    @pypath_scripts_dir.default
    def _default_pypath_scripts_dir(self) -> pathlib.Path:
        if sys.platform.startswith("win"):
            return self.pypath / "Scripts"
        return self.pypath / "bin"

    @build_conf.default
    def _default_build_conf(self) -> pathlib.Path:
        return self.path / "build.conf"

    @build_conf_contents.default
    def _default_build_conf_contents(self) -> str:
        if sys.platform.startswith("win"):
            pyinstaller_version = "dev"
        else:
            pyinstaller_version = PyInstaller.__version__
        return textwrap.dedent(
            """\
        tiamat:
          name: {}
          onedir: {}
          pyinstaller_version: "{}"
          dev_pyinstaller: False
        """.format(
                self.name,
                self.one_dir,
                pyinstaller_version,
            )
        )

    @run_py.default
    def _default_run_py(self) -> pathlib.Path:
        return self.path / "run.py"

    @run_py_contents.default
    def _default_run_py_contents(self) -> str:
        return textwrap.dedent(
            """\
            #!/usr/bin/env python3

            import os
            import sys
            import traceback
            import multiprocessing
            import tiamatpip.cli
            import tiamatpip.configure


            tiamatpip.configure.set_user_base_path({!r})

            def main(argv):
                if argv[1] == "shell":
                    py_shell()
                    return
                if tiamatpip.cli.should_redirect_argv(argv):
                    tiamatpip.cli.process_pip_argv(argv)

                # If we reached this far, it means we're not handling pip stuff

                if argv[1] == "test":
                    print("Tested!")
                if argv[1] == "code":
                    tiamatpip.cli._run_code(sys.argv[2])
                else:
                    print("No command?!")

                sys.exit(0)


            def py_shell():
                import readline  # optional, will allow Up/Down/History in the console
                import code

                variables = globals().copy()
                variables.update(locals())
                shell = code.InteractiveConsole(variables)
                shell.interact()

            if __name__ == "__main__":
                if sys.platform.startswith("win"):
                    multiprocessing.freeze_support()
                main(sys.argv)
            """.format(
                str(self.pypath)
            )
        )

    @requirements_txt.default
    def _default_requirements_txt(self) -> pathlib.Path:
        return self.path / "requirements.txt"

    @requirements_txt_contents.default
    def _default_requirements_txt_contents(self) -> str:
        return "\n".join([str(CODE_ROOT)] + list(self.requirements))

    @subprocess.default
    def _default_subprocess(self):
        return Subprocess(cwd=self.path)

    def __attrs_post_init__(self) -> None:
        self.build_conf.write_text(self.build_conf_contents)
        assert self.run_py
        self.run_py.write_text(self.run_py_contents)
        assert self.requirements_txt
        self.requirements_txt.write_text(self.requirements_txt_contents)
        log.debug(
            "Contents of '%s' for project '%s':\n%s",
            self.requirements_txt,
            self.name,
            self.requirements_txt_contents,
        )

    @property
    def generated_binary_path(self) -> pathlib.Path:
        if self.one_dir:
            if sys.platform.startswith("win"):
                binary_path = self.path / "dist" / self.name / self.name
            else:
                binary_path = self.path / "dist" / "run" / "run"
        else:
            binary_path = self.path / "dist" / self.name
        if sys.platform.startswith("win"):
            return binary_path.with_suffix(".exe")
        return binary_path

    def copy_generated_project_to_temp(self) -> None:
        return self.copy_generated_project_to(pathlib.Path(tempfile.gettempdir()))

    def copy_generated_project_to(self, path: pathlib.Path) -> None:
        if self.one_dir:
            generated_binary_path = self.generated_binary_path.parent
        else:
            generated_binary_path = self.generated_binary_path
        dst = path / generated_binary_path.name
        if dst.exists():
            if dst.is_file():
                dst.unlink()
            else:
                shutil.rmtree(dst, ignore_errors=True)
        log.info("Copying %s -> %s", generated_binary_path, dst)
        if generated_binary_path.is_dir():
            shutil.copytree(generated_binary_path, dst)
        else:
            shutil.copyfile(generated_binary_path, dst)

    def run(self, *args, cwd=None, check=None, **kwargs) -> ProcessResult:
        if cwd is None:
            cwd = str(self.path)

        generated_binary_path = self.generated_binary_path
        if not sys.platform.startswith("win"):
            # Only use relative paths on non Windows platforms
            generated_binary_path = generated_binary_path.relative_to(self.path)

        log.info(
            "Generated binary path: %s",
            generated_binary_path,
        )
        # Create the cmdline to run
        cmdline = [str(generated_binary_path)] + list(args)

        env = cast(EnvironDict, kwargs.pop("env", None) or {})
        env["TIAMAT_PIP_DEBUG"] = "1"

        ret = self.subprocess.run(*cmdline, env=env, **kwargs)
        if ret.returncode != 0:
            if check is True:
                raise CalledProcessError(
                    returncode=ret.returncode,
                    cmd=cmdline,
                    output=ret.stdout,
                    stderr=ret.stderr,
                )
        return ret

    def run_code(self, code: str) -> ProcessResult:
        if code.startswith("\n"):
            code = code[1:]
        code = textwrap.dedent(code)
        return self.run("code", code)

    def build(self) -> None:
        cmdline = ["tiamat", "--log-level=debug", "build", "-c", "build.conf"]
        ret = self.subprocess.run(*cmdline)
        if ret.returncode == 0:
            log.debug(ret)
        else:
            log.error(ret)
            raise CalledProcessError(
                returncode=ret.returncode,
                cmd=cmdline,
                output=ret.stdout,
                stderr=ret.stderr,
            )
        log.info("%s was successfuly built!", self.name)

    def delete_pypath(self) -> None:
        assert self.pypath
        if self.pypath.exists():
            shutil.rmtree(self.pypath, ignore_errors=True)

    def get_store(self) -> Store:
        return Store(pypath=self.pypath)

    def get_installed_packages(self, include_frozen=False):
        data = {}
        if include_frozen:
            ret = self.run("pip", "frozen", "--format", "json")
            assert ret.data is not None
            for pkginfo in ret.data:
                data[parse_package_name(pkginfo["name"])] = pkginfo["version"]
        ret = self.run("pip", "list", "--format", "json")
        assert ret.data is not None
        for pkginfo in ret.data:
            data[parse_package_name(pkginfo["name"])] = pkginfo["version"]
        return data

    def run_common_tests(self, package, package_type):
        common_package_test(self, package, package_type)

    def __enter__(self):
        self.build()
        return self

    def __exit__(self, *args):
        shutil.rmtree(self.path, ignore_errors=True)


def common_package_test(project, package, package_type):
    installed_packages = project.get_installed_packages(
        include_frozen=package_type == "builtin"
    )
    assert package.name in installed_packages
    assert installed_packages[package.name] == package.version

    if package_type == "pypath":
        store = project.get_store()
        assert package.name in store
        if package.altname:
            assert package.altname in store
        assert store[package.name].version == package.version

    ret = project.run(
        "pip", "install", f"{package.altname or package.name}=={package.upgrade}"
    )
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
    assert installed_packages[package.name] == package.upgrade
    store = project.get_store()
    assert package.name in store
    assert store[package.name].version == package.upgrade

    ret = project.run("pip", "uninstall", "-y", package.name)
    assert ret.returncode == 0
    assert "as it is not installed" not in ret.stderr

    installed_packages = project.get_installed_packages()
    assert package.name not in installed_packages

    if package_type == "builtin":
        # We can uninstall the upgrade, but not the builtin
        installed_packages = project.get_installed_packages(
            include_frozen=package_type == "builtin"
        )
        assert package.name in installed_packages

        ret = project.run("pip", "uninstall", "-y", package.name)
        assert "as it is not installed" in ret.stderr
    else:
        store = project.get_store()
        assert package.name not in store
        if package.altname:
            assert package.altname not in store
