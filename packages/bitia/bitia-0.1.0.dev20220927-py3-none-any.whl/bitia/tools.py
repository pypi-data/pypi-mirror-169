__author__ = "Dilawar Singh"
__email__ = "dilawar@subcom.tech"

import typing as T
from pathlib import Path

import typer

app = typer.Typer()

#
# Utilities
#
@app.command("make_available")
@app.command("download")
def download(urls_or_file):
    """Make the data available from a given user input.

    Parameters
    ----------
    urls_or_file : str, Path
        urls as csv or a file containing url. One one each line.
    """
    import bitia.infra.cache

    bitia.infra.cache.make_available(urls_or_file)


if __name__ == "__main__":
    app()
