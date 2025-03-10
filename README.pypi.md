# JsonGeekAI

🚀 A high-performance JSON parser for Python with SIMD optimization and AI features.

[![PyPI version](https://badge.fury.io/py/jsongeekai.svg)](https://badge.fury.io/py/jsongeekai)
[![Python](https://img.shields.io/pypi/pyversions/jsongeekai.svg?style=plastic)](https://badge.fury.io/py/jsongeekai)

## Features

- 🏃‍♂️ **High Performance**: Up to 2-3x faster than native JSON parsing with SIMD optimization
- 🎯 **Smart Compression**: Adaptive compression with intelligent ratio selection
- 🔄 **Java API**: Full Java compatibility layer for seamless integration
- 📊 **Performance Metrics**: P0-P2 classification for performance monitoring
- 💪 **SIMD Optimized**: Utilizes WebAssembly SIMD instructions for parallel processing
- 🔒 **Safe**: Full JSON specification compliance with robust error handling
- 🌟 **Modern**: Python 3.8+ with type hints and async support

## Installation

```bash
pip install jsongeekai
```

## Quick Start

```python
from jsongeekai import loads, dumps

# Simple parsing
data = loads('{"name": "JsonGeekAI", "type": "SIMD"}')

# With compression
compressed_json = dumps(data, enable_compression=True)

# With performance metrics
from jsongeekai import JSONParser

parser = JSONParser(use_simd=True, enable_compression=True)
result = parser.parse_with_metrics('{"numbers": [1, 2, 3, 4, 5]}')
print(f"Parse time: {result['metrics']['parse_time']}ms")
```

## Performance Classification

JsonGeekAI uses a P0-P2 classification system for performance monitoring:

| Grade | Parse Time | Memory Usage | Use Case |
|-------|------------|--------------|----------|
| P0    | <50ms     | <100MB       | Critical performance requirements |
| P1    | <200ms    | <500MB       | Regular performance targets |
| P2    | >200ms    | >500MB       | Optional performance goals |

## Java Integration

```java
import ai.jsongeek.JsonGeekBridge;
import ai.jsongeek.JsonGeekMetrics;

// Create parser instance
JsonGeekBridge parser = new JsonGeekBridge();

// Parse JSON with SIMD optimization
Object result = parser.parse("{\"key\": \"value\"}");

// Get performance metrics
JsonGeekMetrics metrics = parser.getMetrics();
System.out.println("Performance grade: " + metrics.getPerformanceGrade());
```

## Advanced Usage

### Streaming Parsing
```python
from jsongeekai import StreamParser

parser = StreamParser()
with open("large_data.json", "rb") as f:
    for chunk in parser.iter_parse(f):
        process(chunk)
```

### Schema Validation
```python
from jsongeekai import JsonValidator

schema = {
    "type": "object",
    "properties": {"id": {"type": "integer"}}
}
validator = JsonValidator(schema)

# Validation examples
validator.validate('{"id": 1}')  # Passes
validator.validate('{"id": "1"}')  # Raises ValidationError
```

### Parallel Processing
```python
from jsongeekai import JSONParser

# Configure advanced options
parser = JSONParser(
    use_simd=True,           # Enable SIMD optimizations
    enable_compression=True,  # Enable smart compression
    validate_utf8=True,      # Strict UTF-8 validation
    max_depth=32             # Maximum nesting depth
)

# Process multiple chunks in parallel
chunks = [{"id": i} for i in range(1000)]
results = parser.process_parallel(chunks)

# Get performance metrics
metrics = parser.get_performance_metrics()
print(f"Performance grade: {metrics['performance_grade']}")
```

## Security

### Vulnerability Reporting
Please report security vulnerabilities to security@jsongeek.ai. For more details about our security policy and procedures, see our [Security Policy](https://github.com/algorithm07-ai/jsongeek/blob/main/SECURITY.md).

### Data Safety
JsonGeekAI implements several security measures:
- Input validation and sanitization
- Memory safety through WebAssembly sandboxing
- Configurable parsing depth limits
- UTF-8 validation options

## License
JsonGeekAI is released under the MIT License. See the [LICENSE](https://github.com/algorithm07-ai/jsongeek/blob/main/LICENSE) file for the full text.

## Contributing
We welcome contributions! Please check our [Contributing Guide](https://github.com/algorithm07-ai/jsongeek/blob/main/CONTRIBUTING.md).

## Support

- 📚 [Documentation](https://github.com/algorithm07-ai/jsongeek/tree/main/docs)
- 🐛 [Issue Tracker](https://github.com/algorithm07-ai/jsongeek/issues)
- 💬 [Community Discussions](https://github.com/algorithm07-ai/jsongeek/discussions)
