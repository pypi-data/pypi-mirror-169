"""Management of packages and images."""

__author__ = "Dilawar Singh"
__email__ = "dilawar@subcom.tech"

import tempfile
import typing as T
import os
import sys
from pathlib import Path
from bitia.common import run_blocking

SUDO = "sudo" if os.getuid() != 0 else ""

MPM = f"{sys.executable} -m meta_package_manager --no-color"
"""meta package manager cli interface"""


class PackageManger:
    """Package manager"""

    def __init__(self):
        self.scripts: T.Dict[str, Path] = {}

    def __install_command__(self, pkg: str, **kwargs) -> str:
        """Install command for installing a package"""
        manager = kwargs.get("manager", "pacman")
        if manager == "pacman":
            return f"{SUDO} pacman -Sy --noconfirm {pkg}"
        elif manager == "any":
            return f"{MPM} install {pkg}"
        else:
            return f"{MPM} --{manager} install {pkg}"

    def __uninstall_command__(self, pkg: str, **kwargs) -> str:
        """Uninstall command to uninstall a package"""
        manager = kwargs.get("manager", "pacman")
        if manager == "any":
            return f"{MPM} uninstall {pkg}"
        else:
            return f"{MPM} --{manager} uninstall {pkg}"

    def make_available_command(self, cmd: str) -> str:
        """If a command not found then return a installation command that will
        make the command available. This is in beta and may not always work.
        """
        script = []
        script.append(f"if ! command -v {cmd} &> /dev/null; then")
        script.append("\t" + f"echo '{cmd} is not found';")
        script.append("\t" + self.__install_command__(f"$(pkgfile {cmd})"))
        script.append("fi")
        return "\n".join(script)

    def install_script(self, cmds: T.List[str]) -> str:
        """Generate a bash script to install given commands"""
        txt = "#!/bin/sh\n"
        txt += "\n".join([self.make_available_command(cmd) for cmd in cmds])
        return txt

    def ensures(self, executables: T.List[str]):
        """Ensure that given executable exists"""
        script = self.install_script(executables)
        with tempfile.NamedTemporaryFile(
            mode="w", prefix="bitia", suffix=".sh", delete=False
        ) as file:
            file.write(script)
            run_blocking(f"sh {file.name}")
            Path(file.name).unlink(missing_ok=True)

    def install_pkg(self, pkg: str, *, manager: T.Optional[str] = None):
        """Install a given package."""
        run_blocking(self.__install_command__(pkg, manager=manager))

    def uninstall_pkg(self, pkg: str, manager: T.Optional[str] = None):
        """Uninstall a given package"""
        run_blocking(self.__uninstall_command__(pkg, manager=manager))
