"""
Smart compression implementation for JSONGeekAI
"""
import zlib
import json
from typing import Any, Dict, Union

class SmartCompressor:
    """
    Intelligent compression system with adaptive ratio selection
    """
    def __init__(self, compression_level: int = 6):
        self.compression_level = compression_level
        self._last_ratio = 1.0
        self._stats = {
            "original_size": 0,
            "compressed_size": 0,
            "compression_time": 0
        }

    def compress(self, data: Union[str, bytes]) -> bytes:
        """
        Compress data using smart compression algorithm
        
        Args:
            data: Data to compress (string or bytes)
            
        Returns:
            Compressed data as bytes
        """
        if isinstance(data, str):
            data = data.encode('utf-8')
            
        original_size = len(data)
        
        # Try different compression levels
        best_ratio = 1.0
        best_result = data
        
        for level in range(1, self.compression_level + 1):
            compressed = zlib.compress(data, level)
            ratio = len(compressed) / original_size
            
            if ratio < best_ratio:
                best_ratio = ratio
                best_result = compressed
                
        self._last_ratio = best_ratio
        self._stats.update({
            "original_size": original_size,
            "compressed_size": len(best_result),
            "compression_ratio": best_ratio
        })
        
        return best_result

    def decompress(self, data: bytes) -> str:
        """
        Decompress data
        
        Args:
            data: Compressed data
            
        Returns:
            Decompressed string
        """
        try:
            decompressed = zlib.decompress(data)
            return decompressed.decode('utf-8')
        except Exception as e:
            # If decompression fails, data might not be compressed
            if isinstance(data, bytes):
                return data.decode('utf-8')
            return data

    def get_ratio(self) -> float:
        """Get the last compression ratio"""
        return self._last_ratio

    def get_stats(self) -> Dict[str, Any]:
        """Get compression statistics"""
        return self._stats.copy()

    def should_compress(self, data: Union[str, bytes]) -> bool:
        """
        Determine if data should be compressed based on content analysis
        
        Args:
            data: Data to analyze
            
        Returns:
            Boolean indicating whether compression is recommended
        """
        if isinstance(data, str):
            data = data.encode('utf-8')
            
        # Don't compress small data
        if len(data) < 1024:  # 1KB
            return False
            
        # Sample the data to estimate compressibility
        sample_size = min(1024, len(data))
        sample = data[:sample_size]
        compressed_sample = zlib.compress(sample)
        
        # If sample compression ratio is poor, skip compression
        if len(compressed_sample) >= len(sample):
            return False
            
        return True

    def compress_json(self, obj: Any) -> bytes:
        """
        Compress JSON object
        
        Args:
            obj: Python object to compress
            
        Returns:
            Compressed JSON as bytes
        """
        json_str = json.dumps(obj)
        return self.compress(json_str)

    def decompress_json(self, data: bytes) -> Any:
        """
        Decompress JSON data
        
        Args:
            data: Compressed JSON data
            
        Returns:
            Python object
        """
        json_str = self.decompress(data)
        return json.loads(json_str)
