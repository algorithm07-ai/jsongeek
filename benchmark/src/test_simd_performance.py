"""
SIMD Performance Benchmarks for JSONGeek
Tests the performance improvements from SIMD optimization
"""
import json
import time
import numpy as np
from jsongeek.core.simd import SIMDOptimizer
from jsongeek.core.compression import SmartCompressor

class SIMDBenchmark:
    def __init__(self):
        self.simd_optimizer = SIMDOptimizer()
        self.smart_compressor = SmartCompressor()
        
    def generate_test_data(self, size):
        """Generate test data that benefits from SIMD processing"""
        return {
            "numbers": list(range(size)),
            "strings": [f"test{i}" for i in range(size)],
            "nested": [{"id": i, "value": i * 2} for i in range(size)]
        }
        
    def run_simd_benchmark(self, sizes=[1000, 10000, 100000]):
        """Run SIMD vs non-SIMD comparison benchmark"""
        results = {}
        
        for size in sizes:
            test_data = self.generate_test_data(size)
            json_str = json.dumps(test_data)
            
            # Test with SIMD
            start_time = time.time()
            parsed_simd = self.simd_optimizer.parse(json_str)
            simd_time = time.time() - start_time
            
            # Test without SIMD
            start_time = time.time()
            parsed_regular = json.loads(json_str)
            regular_time = time.time() - start_time
            
            # Calculate speedup
            speedup = regular_time / simd_time
            
            results[size] = {
                "simd_time": simd_time,
                "regular_time": regular_time,
                "speedup": speedup,
                "memory_usage": self.simd_optimizer.get_memory_usage()
            }
            
        return results
        
    def test_compression_ratio(self, sizes=[1000, 10000, 100000]):
        """Test smart compression effectiveness"""
        results = {}
        
        for size in sizes:
            test_data = self.generate_test_data(size)
            json_str = json.dumps(test_data)
            
            # Test compression
            compressed = self.smart_compressor.compress(json_str)
            compression_ratio = len(compressed) / len(json_str)
            
            # Test decompression accuracy
            decompressed = self.smart_compressor.decompress(compressed)
            accuracy = decompressed == json_str
            
            results[size] = {
                "original_size": len(json_str),
                "compressed_size": len(compressed),
                "compression_ratio": compression_ratio,
                "accuracy": accuracy
            }
            
        return results

if __name__ == "__main__":
    benchmark = SIMDBenchmark()
    
    # Run SIMD benchmarks
    print("Running SIMD performance tests...")
    simd_results = benchmark.run_simd_benchmark()
    for size, result in simd_results.items():
        print(f"\nData size: {size}")
        print(f"SIMD processing time: {result['simd_time']:.4f}s")
        print(f"Regular processing time: {result['regular_time']:.4f}s")
        print(f"Speedup factor: {result['speedup']:.2f}x")
        print(f"Memory usage: {result['memory_usage']} MB")
    
    # Run compression tests
    print("\nRunning compression tests...")
    compression_results = benchmark.test_compression_ratio()
    for size, result in compression_results.items():
        print(f"\nData size: {size}")
        print(f"Original size: {result['original_size']} bytes")
        print(f"Compressed size: {result['compressed_size']} bytes")
        print(f"Compression ratio: {result['compression_ratio']:.2f}")
        print(f"Decompression accuracy: {'Success' if result['accuracy'] else 'Failed'}")
