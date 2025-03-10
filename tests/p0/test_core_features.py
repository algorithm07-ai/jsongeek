"""
P0 (Mandatory) Tests for Core Features
These tests are critical and must pass before any release
"""
import pytest
from jsongeek import JSONParser, loads, JSONParseError
from jsongeek.core.simd import SIMDOptimizer
from jsongeek.core.compression import SmartCompressor

def test_simd_parsing():
    """Test SIMD-optimized parsing performance"""
    parser = JSONParser(use_simd=True)
    # Generate test data that benefits from SIMD
    large_array = [i for i in range(10000)]
    test_json = {"data": large_array}
    
    # Measure parsing time with SIMD
    with_simd = parser.parse_with_metrics(str(test_json))
    
    # Compare with non-SIMD parsing
    parser.use_simd = False
    without_simd = parser.parse_with_metrics(str(test_json))
    
    # SIMD should provide significant speedup
    assert with_simd["parse_time"] < without_simd["parse_time"]
    assert with_simd["parsed_data"]["data"] == large_array

def test_smart_compression():
    """Test smart compression feature"""
    compressor = SmartCompressor()
    test_data = {"repeated": "value" * 1000}
    
    # Test compression ratio
    compressed = compressor.compress(test_data)
    assert len(compressed) < len(str(test_data))
    
    # Test lossless decompression
    decompressed = compressor.decompress(compressed)
    assert decompressed == test_data

def test_memory_boundaries():
    """Test memory usage boundaries"""
    parser = JSONParser()
    large_json = {"data": [i for i in range(100000)]}
    
    # Monitor memory usage
    memory_stats = parser.parse_with_memory_tracking(str(large_json))
    assert memory_stats["peak_memory_mb"] < 50  # Maximum allowed memory usage
    assert memory_stats["memory_efficiency_score"] > 0.8  # Efficiency threshold

def test_syntax_validation():
    """Test critical syntax validation"""
    parser = JSONParser()
    
    # Test various syntax errors
    invalid_cases = [
        '{"unclosed": "string}',
        '{"extra": "comma",}',
        '{"missing": value}',
        '[1, 2, 3,]'
    ]
    
    for invalid_json in invalid_cases:
        with pytest.raises(JSONParseError) as exc:
            parser.parse(invalid_json)
        assert str(exc.value)  # Error message should be informative
