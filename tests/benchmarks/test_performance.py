"""
Tests for the JSON parser
"""
import pytest
from jsongeek import JSONParser, loads, JSONParseError

def test_basic_parsing():
    """Test basic JSON parsing"""
    data = '{"key": "value", "numbers": [1, 2, 3]}'
    result = loads(data)
    assert result["key"] == "value"
    assert result["numbers"] == [1, 2, 3]

def test_parser_options():
    """Test parser configuration options"""
    parser = JSONParser(use_simd=False, validate_utf8=True, max_depth=16)
    data = '{"nested": {"level": 1}}'
    result = parser.parse(data)
    assert result["nested"]["level"] == 1

def test_invalid_json():
    """Test handling of invalid JSON"""
    with pytest.raises(JSONParseError):
        loads('{"unclosed": "string}')

def test_utf8_validation():
    """Test UTF-8 validation"""
    parser = JSONParser(validate_utf8=True)
    data = '{"unicode": "Hello, 世界"}'
    result = parser.parse(data)
    assert result["unicode"] == "Hello, 世界"

def test_max_depth():
    """Test maximum nesting depth"""
    parser = JSONParser(max_depth=2)
    with pytest.raises(JSONParseError):
        parser.parse('{"a": {"b": {"c": 1}}}')
