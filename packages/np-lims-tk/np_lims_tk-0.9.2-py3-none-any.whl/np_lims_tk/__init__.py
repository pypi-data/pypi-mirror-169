"""Awesome `np-lims-tk` is a Python cli/package created with https://github.com/TezRomacH/python-package-template"""

import sys

if sys.version_info >= (3, 8):
    from importlib import metadata as importlib_metadata
else:
    import importlib_metadata

from .core import find_files, get_suffixes, get_wkft_names
from .exceptions import LimsError, NPTKError


def get_version() -> str:
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "unknown"


version: str = get_version()

__all__ = [
    "find_files",
    "get_suffixes",
    "get_wkft_names",
    "version",
    "NPTKError",
    "LimsError",
]
