import pytest
import json
from jsongeek.core.parser import JSONParser
from jsongeek.core.simd import SIMDOptimizer

class TestJSONCore:
    def test_basic_json_parsing(self):
        parser = JSONParser()
        test_json = '{"name": "test", "value": 123}'
        result = parser.parse(test_json)
        assert result["name"] == "test"
        assert result["value"] == 123

    def test_simd_optimization(self):
        optimizer = SIMDOptimizer()
        large_array = [i for i in range(1000)]
        test_json = {"data": large_array}
        
        # Test SIMD-optimized parsing
        result = optimizer.parse(json.dumps(test_json))
        assert result["data"] == large_array
        
        # Verify performance improvement
        assert optimizer.get_performance_metrics()["simd_speedup"] > 1.0

    def test_memory_usage(self):
        parser = JSONParser()
        # Generate a large JSON object
        large_json = {"data": [{"id": i, "value": f"test{i}"} for i in range(10000)]}
        
        # Monitor memory usage during parsing
        mem_usage = parser.get_memory_usage(json.dumps(large_json))
        assert mem_usage["peak_mb"] < 100  # Maximum allowed memory usage
