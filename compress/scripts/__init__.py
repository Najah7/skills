"""Caveman compress scripts.

This package provides tools to compress natural language markdown files
into caveman format to save input tokens.
"""

from . import cli
from . import compress
from . import detect
from . import validate

__all__ = ["cli", "compress", "detect", "validate"]

__version__ = "1.0.0"
