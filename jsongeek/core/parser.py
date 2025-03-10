"""
Core JSON parser implementation with SIMD optimization and smart compression
"""
from typing import Any, Dict, Optional, Union, List
import time
import numpy as np
from wasmer import Store, Module, Instance
import os

from .exceptions import JSONParseError
from ..utils.simd_detection import has_simd_support
from ..utils.compression import SmartCompressor

class JSONParser:
    """
    High-performance JSON parser with SIMD optimization and smart compression
    """
    def __init__(
        self,
        use_simd: bool = True,
        validate_utf8: bool = True,
        max_depth: int = 32,
        enable_compression: bool = True
    ):
        self.use_simd = use_simd and has_simd_support()
        self.validate_utf8 = validate_utf8
        self.max_depth = max_depth
        self.enable_compression = enable_compression
        self._instance = self._initialize_wasm()
        self._compressor = SmartCompressor() if enable_compression else None
        self._performance_metrics = {}

    def _initialize_wasm(self) -> Instance:
        """Initialize the WebAssembly module with SIMD support"""
        store = Store()
        module_path = os.path.join(
            os.path.dirname(__file__),
            "wasm",
            "simd.wasm" if self.use_simd else "fallback.wasm"
        )
        
        with open(module_path, "rb") as f:
            module = Module(store, f.read())
            return Instance(module)

    def parse_with_metrics(self, json_str: str) -> Dict[str, Any]:
        """
        Parse JSON with performance metrics
        
        Args:
            json_str: JSON string to parse
            
        Returns:
            Dictionary containing parsed data and performance metrics
        """
        start_time = time.time()
        start_memory = self.get_memory_usage()
        
        result = self.parse(json_str)
        
        end_time = time.time()
        end_memory = self.get_memory_usage()
        
        metrics = {
            "parse_time": end_time - start_time,
            "memory_used": end_memory - start_memory,
            "simd_enabled": self.use_simd,
            "compression_enabled": self.enable_compression
        }
        
        if self.enable_compression:
            metrics["compression_ratio"] = self._compressor.get_ratio()
            
        self._performance_metrics = metrics
        return {"data": result, "metrics": metrics}

    def parse(self, json_str: str) -> Any:
        """
        Parse a JSON string into Python objects with SIMD optimization
        
        Args:
            json_str: JSON string to parse
            
        Returns:
            Parsed Python object
            
        Raises:
            JSONParseError: If parsing fails
        """
        try:
            if self.enable_compression:
                json_str = self._compressor.decompress(json_str)
                
            # Convert string to numpy array for SIMD processing
            if self.use_simd:
                data = np.frombuffer(json_str.encode(), dtype=np.uint8)
                result = self._instance.exports.parse_simd(data.tobytes())
            else:
                result = self._instance.exports.parse(json_str)
                
            return result
        except Exception as e:
            raise JSONParseError(str(e))

    def get_memory_usage(self) -> float:
        """Get current memory usage in MB"""
        import psutil
        process = psutil.Process(os.getpid())
        return process.memory_info().rss / 1024 / 1024

    def get_performance_metrics(self) -> Dict[str, Any]:
        """Get the latest performance metrics"""
        return self._performance_metrics

    def process_parallel(self, chunks: List[Dict[str, Any]]) -> List[Any]:
        """
        Process multiple JSON chunks in parallel using SIMD
        
        Args:
            chunks: List of JSON objects to process
            
        Returns:
            List of processed results
        """
        if not self.use_simd:
            raise ValueError("Parallel processing requires SIMD support")
            
        results = []
        # Convert chunks to numpy array for parallel processing
        data = np.array([str(chunk).encode() for chunk in chunks], dtype=object)
        
        # Process in parallel using SIMD
        for chunk in data:
            result = self._instance.exports.parse_simd(chunk.tobytes())
            results.append(result)
            
        return results

def loads(s: Union[str, bytes], **kwargs) -> Any:
    """
    Parse a JSON string with SIMD optimization
    
    This is a convenience function that wraps JSONParser
    
    Args:
        s: JSON string to parse
        **kwargs: Additional arguments to pass to JSONParser
        
    Returns:
        Parsed Python object
    """
    parser = JSONParser(**kwargs)
    return parser.parse(s if isinstance(s, str) else s.decode('utf-8'))

def dumps(obj: Any, enable_compression: bool = True) -> str:
    """
    Serialize object to JSON string with optional compression
    
    Args:
        obj: Python object to serialize
        enable_compression: Whether to enable smart compression
        
    Returns:
        JSON string
    """
    import json
    result = json.dumps(obj)
    
    if enable_compression:
        compressor = SmartCompressor()
        result = compressor.compress(result)
        
    return result
