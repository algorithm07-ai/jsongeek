"""
Exceptions for JsonGeek
"""

class JSONParseError(ValueError):
    """Base exception for JSON parsing errors"""
    def __init__(self, message: str, position: int = -1):
        self.position = position
        super().__init__(f"{message} at position {position}" if position >= 0 else message)
