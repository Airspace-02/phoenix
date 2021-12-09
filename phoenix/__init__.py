# -*- coding: utf-8 -*-

from pathlib import Path

try:
    __PHOENIX_SETUP__
except NameError:
    __PHOENIX_SETUP__ = False

# global namespace
try:
    from phoenix import utils
    from phoenix import augmentation
except ImportError:
    if __PHOENIX_SETUP__ is False:
        raise

try:
    version_path = Path(__file__).parent / "VERSION"
    version = version_path.read_text().strip()
except FileNotFoundError:
    version = "0.0.0"

__version__ = version
__all__ = (
    "__version__",
    "augmentation",
    "utils",
)

del Path
