"""
Performance test suite for JsonGeekAI
Implements P0-P1-P2 test classification
"""
import pytest
import json
import time
from pathlib import Path
from jsongeekai import JSONParser, StreamParser, JsonValidator

# Test data paths
TEST_DATA_DIR = Path(__file__).parent / "data"
P0_TEST_FILE = TEST_DATA_DIR / "p0_test.json"
P1_TEST_FILE = TEST_DATA_DIR / "p1_test.json"
P2_TEST_FILE = TEST_DATA_DIR / "p2_test.json"

@pytest.fixture
def parser():
    return JSONParser(use_simd=True)

@pytest.fixture
def stream_parser():
    return StreamParser(use_simd=True)

@pytest.fixture
def validator():
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "data": {"type": "array", "items": {"type": "number"}}
        }
    }
    return JsonValidator(schema)

def generate_test_data(size: int) -> dict:
    """Generate test data of specified size"""
    return {
        "id": 1,
        "name": "test" * (size // 4),
        "data": [i * 0.1 for i in range(size)]
    }

# P0 Tests (Critical Performance Requirements)
class TestP0Performance:
    """
    P0级测试：语法和边界测试
    - 解析时间 < 50ms
    - 内存使用 < 100MB
    """
    def test_small_json_parse(self, parser, benchmark):
        """Test parsing small JSON (P0)"""
        data = generate_test_data(100)
        json_str = json.dumps(data)
        
        result = benchmark(parser.parse, json_str)
        metrics = parser.get_performance_metrics()
        
        assert metrics["parse_time"] < 50  # 50ms
        assert metrics["memory_used"] < 100  # 100MB

    def test_json_validation(self, validator, benchmark):
        """Test JSON validation (P0)"""
        data = {
            "id": 1,
            "name": "test",
            "data": [1.0, 2.0, 3.0]
        }
        json_str = json.dumps(data)
        
        result = benchmark(validator.validate, json_str)
        assert result is True

# P1 Tests (Standard Performance Targets)
class TestP1Performance:
    """
    P1级测试：结构和语义验证
    - 解析时间 < 200ms
    - 内存使用 < 500MB
    """
    def test_medium_json_parse(self, parser, benchmark):
        """Test parsing medium JSON (P1)"""
        data = generate_test_data(10000)
        json_str = json.dumps(data)
        
        result = benchmark(parser.parse, json_str)
        metrics = parser.get_performance_metrics()
        
        assert metrics["parse_time"] < 200  # 200ms
        assert metrics["memory_used"] < 500  # 500MB

    def test_stream_parsing(self, stream_parser):
        """Test stream parsing (P1)"""
        data = generate_test_data(10000)
        json_str = json.dumps(data)
        
        with open(P1_TEST_FILE, "wb") as f:
            f.write(json_str.encode())
            
        count = 0
        start_time = time.time()
        
        with open(P1_TEST_FILE, "rb") as f:
            for obj in stream_parser.iter_parse(f):
                count += 1
                
        parse_time = (time.time() - start_time) * 1000
        assert parse_time < 200  # 200ms
        assert count > 0

# P2 Tests (Extended Performance Goals)
class TestP2Performance:
    """
    P2级测试：标准合规性扩展测试
    - 无严格时间限制
    - 关注特殊场景和边界情况
    """
    def test_large_json_parse(self, parser):
        """Test parsing large JSON (P2)"""
        data = generate_test_data(100000)
        json_str = json.dumps(data)
        
        start_time = time.time()
        result = parser.parse(json_str)
        parse_time = (time.time() - start_time) * 1000
        
        metrics = parser.get_performance_metrics()
        print(f"Large JSON parse time: {parse_time}ms")
        print(f"Memory used: {metrics['memory_used']}MB")

    def test_parallel_processing(self, parser):
        """Test parallel processing (P2)"""
        chunks = [generate_test_data(1000) for _ in range(10)]
        
        start_time = time.time()
        results = parser.process_parallel(chunks)
        process_time = (time.time() - start_time) * 1000
        
        assert len(results) == 10
        print(f"Parallel processing time: {process_time}ms")
