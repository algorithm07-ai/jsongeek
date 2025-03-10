"""
JsonGeek - High-performance JSON parser using WebAssembly SIMD
"""

__version__ = "0.1.0"

from .core.parser import JSONParser, loads, dumps
from .core.exceptions import JSONParseError

__all__ = ["JSONParser", "loads", "dumps", "JSONParseError"]
