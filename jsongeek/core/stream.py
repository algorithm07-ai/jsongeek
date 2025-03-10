"""
Stream parsing implementation for JsonGeekAI
"""
from typing import BinaryIO, Iterator, Any, Optional
import json
from .parser import JSONParser
from .exceptions import JSONParseError

class StreamParser:
    """
    Stream parser for processing large JSON files
    """
    def __init__(
        self,
        chunk_size: int = 8192,
        use_simd: bool = True,
        validate_utf8: bool = True
    ):
        self.chunk_size = chunk_size
        self.parser = JSONParser(use_simd=use_simd, validate_utf8=validate_utf8)
        self._buffer = ""

    def iter_parse(self, stream: BinaryIO) -> Iterator[Any]:
        """
        Iterate over JSON objects in a stream
        
        Args:
            stream: Binary stream containing JSON data
            
        Yields:
            Parsed JSON objects
        """
        while True:
            chunk = stream.read(self.chunk_size)
            if not chunk:
                break
                
            # Decode chunk and add to buffer
            try:
                self._buffer += chunk.decode('utf-8')
            except UnicodeDecodeError as e:
                raise JSONParseError(f"Invalid UTF-8 encoding: {e}")
                
            # Process complete objects from buffer
            while True:
                obj = self._extract_object()
                if obj is None:
                    break
                yield obj
                
        # Process any remaining data
        if self._buffer.strip():
            try:
                yield self.parser.parse(self._buffer)
            except Exception as e:
                raise JSONParseError(f"Error parsing final chunk: {e}")
                
        self._buffer = ""

    def _extract_object(self) -> Optional[Any]:
        """
        Extract a complete JSON object from the buffer
        
        Returns:
            Parsed object if complete object found, None otherwise
        """
        try:
            # Find complete object
            decoder = json.JSONDecoder()
            obj, index = decoder.raw_decode(self._buffer)
            
            # Update buffer and return object
            self._buffer = self._buffer[index:].lstrip()
            return obj
        except json.JSONDecodeError:
            return None

    def parse_file(self, filename: str) -> Iterator[Any]:
        """
        Parse JSON objects from a file
        
        Args:
            filename: Path to JSON file
            
        Yields:
            Parsed JSON objects
        """
        with open(filename, 'rb') as f:
            yield from self.iter_parse(f)
