"""BiTIA command line interface to submit job to the BiTIA server.

bitia dir
"""

__author__ = "Dilawar Singh"
__email__ = "dilawar@subcom.tech"

import sys
import typing as T
import requests
import zipfile
from pathlib import Path
import tempfile
import bitia
from bitia.checksumdir import dirhash

import logging
from rich.logging import RichHandler

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

logger = logging.getLogger("bitia")

import typer

app = typer.Typer()


def version_callback(value: bool):
    if value:
        print(bitia.version())


def bitia_dir() -> Path:
    """CLI cache directory"""
    bdir = Path(tempfile.gettempdir()) / "bitia"
    bdir.mkdir(parents=True, exist_ok=True)
    return bdir


def dir_info(user_dir: Path) -> dict:
    """Check if directory is in good condition."""
    files = [f.resolve() for f in user_dir.glob("**/*") if f.is_file()]
    size_in_mb = sum(f.stat().st_size / 1024.0 / 1024.0 for f in files)
    if size_in_mb > 20:
        logger.error(
            "The size of pipeline is more than 20MB. Uploading this big pipeline is now allowed."
        )
        quit(-1)
    if size_in_mb > 10:
        logger.warning(
            "The size of pipeline is >10MB ({size_in_mb} MB)."
            " You should try to reduce the size of the pipeline. TODO: See this link."
        )
    return dict(size_in_mb=size_in_mb, num_files=len(files), files=files)


def prepare_archive(user_dir: Path) -> Path:
    """Prepare the file to upload. Store it in temp directory"""
    dinfo = dir_info(user_dir)
    dhash = dirhash(user_dir)
    logger.info(f"Preparing the zipfile pipeline from {user_dir}")
    logger.info(f" size={dinfo['size_in_mb']} MB, total files={dinfo['num_files']}")
    outfile = bitia_dir() / "pipelines" / f"{dhash}.zip"
    outfile.parent.mkdir(parents=True, exist_ok=True)
    assert dinfo["files"], f"No file found in {user_dir}"
    with zipfile.ZipFile(outfile, "w", zipfile.ZIP_DEFLATED) as zfile:
        for entry in dinfo["files"]:
            logger.info(f"Adding {entry} to zipfile")
            zfile.write(entry)

    # check the prepared zip file.
    with zipfile.ZipFile(outfile) as zfile:
        assert zfile.namelist(), "Empty zipfile"

    # assert non-zero size of the zip file.
    assert outfile.is_file(), f"{outfile} does not exists"
    return outfile


def submit_job(pipeline_zip: Path, server: str):
    """Submit job to the API and stream the output."""
    session = requests.Session()
    numbytes = pipeline_zip.stat().st_size
    assert numbytes > 0
    logger.info(
        f"Submitting {pipeline_zip} (size={numbytes/1024.0:.2f} KB) to the {server}"
    )
    files = {"pipeline_zip": open(str(pipeline_zip), "rb")}
    r = session.post(
        f"{server}/submit", files=files, data=dict(filename=pipeline_zip), stream=True
    )
    for line in r.iter_lines():
        print(line)


@app.command()
def submit(user_input: str, server: str = "https://public.bitia.link"):
    """Submit your pipelin (url, directory, zip_file).

    Prepare the user directory to send to the server. User can also provide link
    to the pipeline to run.
    """
    if (path := Path(user_input)).exists():
        if path.is_dir():
            pipeline_zip = prepare_archive(path)
        elif path.is_file() and path.suffix.lower() == ".zip":
            pipeline_zip = path
        else:
            raise RuntimeError(f"Not supported: {path}")
        submit_job(pipeline_zip, server)
    else:
        logger.warning("Fetching pipeline from url is not supported")
        sys.exit(-1)


@app.command()
def version():
    """version information"""
    print(bitia.version())


if __name__ == "__main__":
    app()
