"""
Standard compliance test suite for JsonGeekAI
Implements RFC 8259 and ECMA-404 compliance tests
"""
import pytest
import json
from jsongeekai import JSONParser, JsonValidator
from jsongeekai.core.exceptions import JSONParseError

@pytest.fixture
def parser():
    return JSONParser(use_simd=True, validate_utf8=True)

@pytest.fixture
def validator():
    return JsonValidator({
        "type": "object",
        "properties": {
            "test": {"type": "string"}
        }
    })

class TestRFC8259Compliance:
    """
    RFC 8259 标准合规性测试 (P1)
    测试JSON解析器是否符合RFC 8259规范
    """
    
    def test_basic_json_types(self, parser):
        """Test all basic JSON types defined in RFC 8259"""
        test_cases = [
            ('{"string": "value"}', dict),
            ('[1, 2, 3]', list),
            ('42', int),
            ('3.14', float),
            ('true', bool),
            ('false', bool),
            ('null', type(None))
        ]
        
        for json_str, expected_type in test_cases:
            result = parser.parse(json_str)
            assert isinstance(result, expected_type)

    def test_unicode_handling(self, parser):
        """Test Unicode handling (RFC 8259 Section 8.1)"""
        test_cases = [
            '{"test": "Hello, 世界"}',
            '{"test": "\\u4F60\\u597D"}',  # 你好
            '{"emoji": "\\uD83D\\uDE00"}'  # 😀
        ]
        
        for json_str in test_cases:
            result = parser.parse(json_str)
            assert isinstance(result, dict)

    def test_number_formats(self, parser):
        """Test number formats (RFC 8259 Section 6)"""
        test_cases = [
            ('{"num": 42}', int),
            ('{"num": -42}', int),
            ('{"num": 3.14}', float),
            ('{"num": -3.14}', float),
            ('{"num": 1.23e4}', float),
            ('{"num": 1.23e-4}', float)
        ]
        
        for json_str, expected_type in test_cases:
            result = parser.parse(json_str)
            assert isinstance(result["num"], expected_type)

class TestECMA404Compliance:
    """
    ECMA-404 标准合规性测试 (P1)
    测试JSON解析器是否符合ECMA-404规范
    """
    
    def test_object_structure(self, parser):
        """Test object structure rules"""
        valid_cases = [
            '{}',
            '{"a": 1}',
            '{"a": 1, "b": 2}'
        ]
        
        invalid_cases = [
            '{',
            '{"a": 1,}',
            '{"a"}',
            '{a: 1}'
        ]
        
        for case in valid_cases:
            result = parser.parse(case)
            assert isinstance(result, dict)
            
        for case in invalid_cases:
            with pytest.raises(JSONParseError):
                parser.parse(case)

    def test_array_structure(self, parser):
        """Test array structure rules"""
        valid_cases = [
            '[]',
            '[1, 2, 3]',
            '[1, "two", true]'
        ]
        
        invalid_cases = [
            '[',
            '[1,]',
            '[1 2]'
        ]
        
        for case in valid_cases:
            result = parser.parse(case)
            assert isinstance(result, list)
            
        for case in invalid_cases:
            with pytest.raises(JSONParseError):
                parser.parse(case)

class TestSchemaValidation:
    """
    JSON Schema 验证测试 (P1)
    测试模式验证功能
    """
    
    def test_basic_validation(self, validator):
        """Test basic schema validation"""
        valid_cases = [
            '{"test": "value"}',
            '{"test": "another value"}'
        ]
        
        invalid_cases = [
            '{"test": 42}',
            '{"wrong": "value"}',
            '{"test": true}'
        ]
        
        for case in valid_cases:
            assert validator.validate(case) is True
            
        for case in invalid_cases:
            with pytest.raises(JSONParseError):
                validator.validate(case)

class TestExtendedCompliance:
    """
    扩展合规性测试 (P2)
    测试额外的边界情况和特殊场景
    """
    
    def test_nested_structures(self, parser):
        """Test deeply nested structures"""
        # 生成深度嵌套的JSON
        depth = 20
        data = {"level": 1}
        current = data
        for i in range(2, depth + 1):
            current["nested"] = {"level": i}
            current = current["nested"]
            
        json_str = json.dumps(data)
        result = parser.parse(json_str)
        
        # 验证嵌套层次
        current = result
        for i in range(1, depth + 1):
            assert current["level"] == i
            if i < depth:
                current = current["nested"]

    def test_large_strings(self, parser):
        """Test handling of large string values"""
        # 生成大字符串
        large_str = "x" * 1000000
        data = {"large": large_str}
        json_str = json.dumps(data)
        
        result = parser.parse(json_str)
        assert len(result["large"]) == 1000000

    def test_special_characters(self, parser):
        """Test handling of special characters"""
        test_cases = [
            '{"test": "\\n\\r\\t"}',
            '{"test": "\\\\"}',
            '{"test": "\\"quoted\\""}',
            '{"test": "\\u0000"}',
            '{"test": "\\u001F"}'
        ]
        
        for case in test_cases:
            result = parser.parse(case)
            assert isinstance(result["test"], str)
