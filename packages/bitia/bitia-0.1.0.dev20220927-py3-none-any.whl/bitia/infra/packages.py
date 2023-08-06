"""Management of packages and images."""

__author__ = "Dilawar Singh"
__email__ = "dilawar@subcom.tech"

import logging
import tempfile
import subprocess
import typing as T
import os
import sys
import shutil
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
        elif manager == "any" or manager is None:
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

    def cnf_package(
        self, cnf: str, *, manager: T.Optional[str] = None
    ) -> T.Optional[str]:
        """Find package for given command."""
        manager = "pacman" if manager is None else manager
        if manager == "pacman":
            if shutil.which("pkgfile") is None:
                logging.warning(f"pkgfile not found. I will not install any package.")
                return None
            try:
                return subprocess.check_output(["pkgfile", cnf], text=True)
            except subprocess.CalledProcessError:
                logging.warning(
                    f"Could not find a package that provides command `{cnf}`.\
                    Maybe the command name is not correct or a package is \
                    missing from the reposistory?!"
                )
                return None
        else:
            logging.warning(
                f"package manager {manager} is not supported. I will not try to install"
            )
            return None

    def ensures(self, executables: T.List[str], manager: T.Optional[str] = None):
        for exe in executables:
            if shutil.which(exe):
                logging.info(f"Command {exe} is already available")
                continue
            logging.info(
                f"Command {exe} is not found. Looking for a suitable installation... "
            )
            pkg = self.cnf_package(exe)
            if pkg:
                self.install_pkg(pkg, manager=manager)

    def install_pkg(self, pkg: str, *, manager: T.Optional[str] = None):
        """Install a given package."""
        print(f"Installing package {pkg}")
        run_blocking(self.__install_command__(pkg, manager=manager))

    def uninstall_pkg(self, pkg: str, manager: T.Optional[str] = None):
        """Uninstall a given package"""
        run_blocking(self.__uninstall_command__(pkg, manager=manager))
