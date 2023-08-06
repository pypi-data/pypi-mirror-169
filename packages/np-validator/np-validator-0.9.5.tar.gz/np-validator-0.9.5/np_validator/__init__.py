"""Awesome `np-validator` is a Python cli/package created with https://github.com/TezRomacH/python-package-template"""

import sys

if sys.version_info >= (3, 8):
    from importlib import metadata as importlib_metadata
else:
    import importlib_metadata

from .core import run_validation
from .models import (
    Processor,
    ValidationStep,
    Validator,
    autogenerate_validation_steps,
    dump_ValidationResults,
    load_ValidationStep,
    update_project_validation_steps,
)


def get_version() -> str:
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "unknown"


version: str = get_version()

# needed or else mypy will complain as of 0.971
__all__ = [
    "run_validation",
    "ValidationStep",
    "Validator",
    "Processor",
    "load_ValidationStep",
    "autogenerate_validation_steps",
    "update_project_validation_steps",
    "version",
]
