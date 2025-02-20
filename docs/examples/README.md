# JsonGeekAI 使用示例

## 基本用法

### 解析 JSON 字符串

```python
from jsongeekai import JsonParser

# 创建解析器实例
parser = JsonParser()

# 解析简单的 JSON 字符串
json_str = '{"name": "JsonGeek", "version": "0.1.1"}'
result = parser.parse(json_str)
print(result)  # {'name': 'JsonGeek', 'version': '0.1.1'}
```

### 处理复杂数据

```python
# 解析嵌套的 JSON
complex_json = '''
{
    "user": {
        "name": "JsonGeek",
        "preferences": {
            "theme": "dark",
            "notifications": true
        },
        "scores": [95, 88, 92]
    }
}
'''
result = parser.parse(complex_json)
print(result['user']['preferences']['theme'])  # 'dark'
```

## 性能优化示例

### 批量处理

```python
# 批量解析多个 JSON 字符串
json_list = [
    '{"id": 1, "value": "first"}',
    '{"id": 2, "value": "second"}',
    '{"id": 3, "value": "third"}'
]

results = [parser.parse(json_str) for json_str in json_list]
```

## 错误处理

```python
try:
    result = parser.parse('{"invalid": json}')
except Exception as e:
    print(f"解析错误: {e}")
```

更多示例请参考我们的 [API 文档](../api/README.md)。
