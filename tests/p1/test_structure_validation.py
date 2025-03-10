"""
P1 (Regular) Tests for Structure and Semantic Validation
These tests are part of regular testing cycles
"""
import pytest
from jsongeek import JSONParser, JSONSchemaValidator
from jsongeek.core.schema import SchemaInference

def test_schema_inference():
    """Test schema inference capabilities"""
    inferrer = SchemaInference()
    
    # Test data with mixed types
    test_data = [
        {"id": 1, "name": "test1", "active": True},
        {"id": 2, "name": "test2", "active": False},
        {"id": 3, "name": "test3", "scores": [95, 87, 92]}
    ]
    
    inferred_schema = inferrer.infer(test_data)
    assert inferred_schema["properties"]["id"]["type"] == "integer"
    assert inferred_schema["properties"]["name"]["type"] == "string"
    assert inferred_schema["properties"]["active"]["type"] == "boolean"
    assert "scores" in inferred_schema["properties"]

def test_cross_platform_compatibility():
    """Test JSON compatibility across platforms"""
    parser = JSONParser()
    
    # Test various number formats
    number_cases = {
        "integer": "42",
        "negative": "-17",
        "float": "3.14159",
        "scientific": "1.23e-4",
        "zero": "0",
        "max_safe_integer": "9007199254740991"
    }
    
    for case_name, number_str in number_cases.items():
        json_str = f'{{"value": {number_str}}}'
        result = parser.parse(json_str)
        assert isinstance(result["value"], (int, float))

def test_api_compatibility():
    """Test API response validation"""
    validator = JSONSchemaValidator()
    
    # Define API response schema
    api_schema = {
        "type": "object",
        "required": ["status", "data"],
        "properties": {
            "status": {"type": "string"},
            "data": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["id", "timestamp"],
                    "properties": {
                        "id": {"type": "integer"},
                        "timestamp": {"type": "string", "format": "date-time"}
                    }
                }
            }
        }
    }
    
    # Test valid API response
    valid_response = {
        "status": "success",
        "data": [
            {"id": 1, "timestamp": "2025-03-10T09:00:00Z"},
            {"id": 2, "timestamp": "2025-03-10T09:01:00Z"}
        ]
    }
    
    assert validator.validate(valid_response, api_schema)

def test_performance_regression():
    """Test performance regression checks"""
    parser = JSONParser(use_simd=True)
    
    # Generate test data
    test_sizes = [1000, 10000, 100000]
    baseline_metrics = {}
    
    for size in test_sizes:
        test_data = {"array": list(range(size))}
        metrics = parser.parse_with_metrics(str(test_data))
        baseline_metrics[size] = metrics["parse_time"]
        
        # Ensure parsing time scales sub-linearly
        if size > 1000:
            ratio = metrics["parse_time"] / baseline_metrics[1000]
            expected_ratio = size / 1000
            assert ratio < expected_ratio  # Should scale better than linear
