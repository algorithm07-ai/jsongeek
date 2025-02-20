# JsonGeekAI Documentation

欢迎使用 JsonGeekAI 文档！

## 目录

- [安装指南](installation/README.md)
- [API 文档](api/README.md)
- [使用示例](examples/README.md)
- [贡献指南](contributing/README.md)

## 快速开始

```python
from jsongeekai import JsonParser

# 创建解析器实例
parser = JsonParser()

# 解析 JSON 字符串
result = parser.parse('{"key": "value"}')
print(result)  # {'key': 'value'}
```

## 性能优化

JsonGeekAI 使用 AVX2 SIMD 指令集优化，提供了极致的解析性能：

- 字符串解析优化
- 数字解析优化
- 批量数据处理
- CPU 特性自动检测

## 支持

如果你遇到任何问题或有建议，请：

1. 查看我们的[常见问题](docs/FAQ.md)
2. 在 [GitHub Issues](https://github.com/zhanghongping/jsongeek/issues) 上提交问题
3. 阅读我们的[贡献指南](contributing/README.md)
