"""meta package manager interface

In fact, we use meta-package-manager here.
"""

__author__ = "Dilawar Singh"
__email__ = "dilawar@subcom.tech"

from pathlib import Path
import typing as T

import typer

from bitia.infra.packages import PackageManger
from bitia.common.path import sniff_executales

app = typer.Typer()

g_pm = PackageManger()


@app.command("install")
def install(pkgs: T.List[str], manager: T.Optional[str] = None):
    """Install given packages"""
    for pkg in pkgs:
        g_pm.install_pkg(pkg, manager=manager)


@app.command("uninstall")
@app.command("remove")
def uninstall(pkgs: T.List[str], manager: T.Optional[str] = None):
    """Install given packages"""
    for pkg in pkgs:
        g_pm.uninstall_pkg(pkg, manager=manager)


@app.command("ensure")
@app.command("make_available")
def make_available(executables: T.List[str]):
    """Ensure that following executables are available.
    This is meant to work inside the container.

    Parameters
    ----------
    executables:
        List of executables.
    """
    g_pm.ensures(executables)


def ensure_from_script(main_script: Path):
    """Ensure that following executables are available.
    This is meant to work inside the container.

    Parameters
    ----------

    main_script:
        Sniff the file and install required packages.
    """
    execs = sniff_executales(main_script)
    assert execs, f"No executable found in {main_script}"
    return make_available(execs)


if __name__ == "__main__":
    app()
