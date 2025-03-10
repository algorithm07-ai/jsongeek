"""
P0 (Mandatory) Tests for SIMD Optimization
These tests verify the core SIMD functionality and performance improvements
"""
import pytest
import json
import time
from jsongeek.core.simd import SIMDOptimizer
from jsongeek.core.compression import SmartCompressor
from ..test_config import SIMD_CONFIG, COMPRESSION_CONFIG

class TestSIMDCore:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.simd_optimizer = SIMDOptimizer()
        self.smart_compressor = SmartCompressor()
        
    def test_simd_speedup(self):
        """Verify SIMD provides significant speedup"""
        # Generate test data above minimum size
        test_size = SIMD_CONFIG['min_data_size']
        test_data = {
            "numbers": list(range(test_size)),
            "nested": [{"id": i, "value": i * 2} for i in range(test_size)]
        }
        json_str = json.dumps(test_data)
        
        # Measure SIMD performance
        start_time = time.time()
        simd_result = self.simd_optimizer.parse(json_str)
        simd_time = time.time() - start_time
        
        # Measure standard parsing performance
        start_time = time.time()
        standard_result = json.loads(json_str)
        standard_time = time.time() - start_time
        
        # Verify speedup meets requirement
        speedup = standard_time / simd_time
        assert speedup >= SIMD_CONFIG['target_speedup'], \
            f"SIMD speedup ({speedup:.2f}x) below target ({SIMD_CONFIG['target_speedup']}x)"
        
        # Verify results match
        assert simd_result == standard_result, "SIMD parsing results differ from standard parsing"
        
    def test_memory_efficiency(self):
        """Verify memory usage efficiency"""
        test_size = SIMD_CONFIG['min_data_size'] * 2
        test_data = {"data": list(range(test_size))}
        json_str = json.dumps(test_data)
        
        # Monitor memory usage
        mem_stats = self.simd_optimizer.get_memory_stats(json_str)
        efficiency = mem_stats['efficiency_score']
        
        assert efficiency >= SIMD_CONFIG['memory_efficiency'], \
            f"Memory efficiency ({efficiency:.2f}) below target ({SIMD_CONFIG['memory_efficiency']})"
            
    def test_compression_effectiveness(self):
        """Verify smart compression effectiveness"""
        # Generate compressible data
        test_data = {
            "repeated": "test" * 1000,
            "structured": [{"key": "value"} for _ in range(100)]
        }
        json_str = json.dumps(test_data)
        
        # Test compression
        compressed = self.smart_compressor.compress(json_str)
        ratio = len(compressed) / len(json_str)
        
        # Verify compression ratio
        assert COMPRESSION_CONFIG['min_ratio'] <= ratio <= COMPRESSION_CONFIG['max_ratio'], \
            f"Compression ratio ({ratio:.2f}) outside target range"
            
        # Verify lossless decompression if required
        if COMPRESSION_CONFIG['lossless_required']:
            decompressed = self.smart_compressor.decompress(compressed)
            assert decompressed == json_str, "Lossless decompression failed"
            
    def test_parallel_processing(self):
        """Verify parallel processing capabilities"""
        # Generate multiple chunks of data
        chunks = [
            {"chunk": i, "data": list(range(1000))}
            for i in range(4)
        ]
        
        # Process chunks in parallel
        start_time = time.time()
        results = self.simd_optimizer.process_parallel(chunks)
        parallel_time = time.time() - start_time
        
        # Process sequentially for comparison
        start_time = time.time()
        sequential_results = [json.loads(json.dumps(chunk)) for chunk in chunks]
        sequential_time = time.time() - start_time
        
        # Verify parallel processing is faster
        assert parallel_time < sequential_time, "Parallel processing not showing improvement"
        assert results == sequential_results, "Parallel processing results differ"
