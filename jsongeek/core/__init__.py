"""
Core functionality for JsonGeek
"""

from .parser import JSONParser, loads, dumps
from .exceptions import JSONParseError

__all__ = ["JSONParser", "loads", "dumps", "JSONParseError"]
