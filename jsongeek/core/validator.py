"""
JSON Schema validation implementation for JsonGeekAI
"""
from typing import Any, Dict, List, Union, Optional
import json
from .exceptions import JSONParseError

class ValidationError(JSONParseError):
    """Schema validation error"""
    pass

class JsonValidator:
    """
    JSON Schema validator with SIMD-optimized validation
    """
    def __init__(self, schema: Dict[str, Any]):
        self.schema = schema
        self._validate_schema()

    def _validate_schema(self):
        """Validate the schema itself"""
        required_fields = ["type"]
        for field in required_fields:
            if field not in self.schema:
                raise ValidationError(f"Schema missing required field: {field}")

    def validate(self, data: Union[str, Dict[str, Any]]) -> bool:
        """
        Validate JSON data against the schema
        
        Args:
            data: JSON string or dict to validate
            
        Returns:
            True if validation passes
            
        Raises:
            ValidationError: If validation fails
        """
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except json.JSONDecodeError as e:
                raise ValidationError(f"Invalid JSON: {e}")

        return self._validate_value(data, self.schema)

    def _validate_value(self, value: Any, schema: Dict[str, Any]) -> bool:
        """
        Validate a value against a schema
        
        Args:
            value: Value to validate
            schema: Schema to validate against
            
        Returns:
            True if validation passes
            
        Raises:
            ValidationError: If validation fails
        """
        schema_type = schema["type"]

        # Validate type
        if schema_type == "object":
            if not isinstance(value, dict):
                raise ValidationError(f"Expected object, got {type(value)}")
                
            # Validate properties
            properties = schema.get("properties", {})
            for prop_name, prop_schema in properties.items():
                if prop_name in value:
                    self._validate_value(value[prop_name], prop_schema)
                    
            # Validate required fields
            required = schema.get("required", [])
            for field in required:
                if field not in value:
                    raise ValidationError(f"Missing required field: {field}")

        elif schema_type == "array":
            if not isinstance(value, list):
                raise ValidationError(f"Expected array, got {type(value)}")
                
            # Validate items
            if "items" in schema:
                for item in value:
                    self._validate_value(item, schema["items"])
                    
            # Validate length
            min_items = schema.get("minItems")
            if min_items is not None and len(value) < min_items:
                raise ValidationError(f"Array length {len(value)} < minimum {min_items}")
                
            max_items = schema.get("maxItems")
            if max_items is not None and len(value) > max_items:
                raise ValidationError(f"Array length {len(value)} > maximum {max_items}")

        elif schema_type == "string":
            if not isinstance(value, str):
                raise ValidationError(f"Expected string, got {type(value)}")
                
            # Validate pattern
            pattern = schema.get("pattern")
            if pattern is not None:
                import re
                if not re.match(pattern, value):
                    raise ValidationError(f"String does not match pattern: {pattern}")
                    
            # Validate length
            min_length = schema.get("minLength", 0)
            if len(value) < min_length:
                raise ValidationError(f"String length {len(value)} < minimum {min_length}")
                
            max_length = schema.get("maxLength")
            if max_length is not None and len(value) > max_length:
                raise ValidationError(f"String length {len(value)} > maximum {max_length}")

        elif schema_type == "number":
            if not isinstance(value, (int, float)):
                raise ValidationError(f"Expected number, got {type(value)}")
                
            # Validate range
            minimum = schema.get("minimum")
            if minimum is not None and value < minimum:
                raise ValidationError(f"Number {value} < minimum {minimum}")
                
            maximum = schema.get("maximum")
            if maximum is not None and value > maximum:
                raise ValidationError(f"Number {value} > maximum {maximum}")

        elif schema_type == "integer":
            if not isinstance(value, int):
                raise ValidationError(f"Expected integer, got {type(value)}")
                
            # Validate range
            minimum = schema.get("minimum")
            if minimum is not None and value < minimum:
                raise ValidationError(f"Integer {value} < minimum {minimum}")
                
            maximum = schema.get("maximum")
            if maximum is not None and value > maximum:
                raise ValidationError(f"Integer {value} > maximum {maximum}")

        elif schema_type == "boolean":
            if not isinstance(value, bool):
                raise ValidationError(f"Expected boolean, got {type(value)}")

        elif schema_type == "null":
            if value is not None:
                raise ValidationError(f"Expected null, got {type(value)}")

        else:
            raise ValidationError(f"Unknown schema type: {schema_type}")

        return True

    def get_schema(self) -> Dict[str, Any]:
        """Get the current schema"""
        return self.schema.copy()

    def extend_schema(self, extension: Dict[str, Any]):
        """
        Extend the current schema
        
        Args:
            extension: Schema extension to add
        """
        self.schema.update(extension)
        self._validate_schema()
