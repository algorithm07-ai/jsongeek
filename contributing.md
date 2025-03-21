# JsonGeekAI 贡献指南

## 1. 开发环境设置

### 1.1 基本要求

- Python 3.8+
- pip 20.0+
- Git

### 1.2 开发环境准备

```bash
# 克隆仓库
git clone https://github.com/your-org/jsongeek.git
cd jsongeek

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows

# 安装依赖
pip install -r requirements-dev.txt
```

### 1.3 IDE配置

推荐使用PyCharm或VS Code，并安装以下插件：
- Python
- Pylint
- Black Formatter
- isort

## 2. 代码规范

### 2.1 Python代码风格

遵循PEP 8规范，主要包括：

```python
# 正确的命名方式
class JsonValidator:  # 类名使用CamelCase
    def validate_json(self):  # 方法名使用snake_case
        pass

# 正确的导入顺序
import os
import sys
from typing import Dict, List

import numpy as np
import pandas as pd

from jsongeek_cli import JsonGeekAI
```

### 2.2 文档规范

所有公共API都需要添加文档字符串：

```python
def validate(
    data: Dict[str, Any],
    schema: Dict[str, Any],
    strict: bool = False
) -> ValidationReport:
    """
    验证JSON数据是否符合Schema
    
    Args:
        data: 待验证的JSON数据
        schema: JSON Schema
        strict: 是否启用严格模式
        
    Returns:
        ValidationReport: 验证报告
        
    Raises:
        ValidationError: 验证失败时抛出
        SecurityError: 发现未处理的敏感数据时抛出
    """
    pass
```

### 2.3 测试规范

使用pytest进行测试：

```python
import pytest
from jsongeek_cli import JsonGeekAI

def test_validation():
    # 准备测试数据
    data = {"name": "test"}
    schema = {"type": "object"}
    
    # 执行验证
    report = JsonGeekAI.validate(data, schema)
    
    # 验证结果
    assert report.is_valid
    assert report.validation_type == "fast"
    assert report.execution_time > 0
```

## 3. 开发流程

### 3.1 功能开发流程

1. 创建特性分支
```bash
git checkout -b feature/new-feature
```

2. 编写代码和测试
```bash
# 运行测试
pytest tests/

# 运行代码检查
pylint src/
black src/
isort src/
```

3. 提交代码
```bash
git add .
git commit -m "feat: add new feature"
```

4. 创建Pull Request

### 3.2 Bug修复流程

1. 创建修复分支
```bash
git checkout -b fix/bug-description
```

2. 修复并验证
```bash
# 运行相关测试
pytest tests/test_specific.py

# 运行全套测试
pytest
```

3. 提交修复
```bash
git commit -m "fix: resolve specific bug"
```

## 4. 测试指南

### 4.1 单元测试

```python
# test_validator.py
class TestJsonValidator:
    def setup_method(self):
        self.validator = JsonGeekAI()
        
    def test_simple_validation(self):
        data = {"key": "value"}
        schema = {"type": "object"}
        result = self.validator.validate(data, schema)
        assert result.is_valid
        
    def test_invalid_data(self):
        with pytest.raises(ValidationError):
            self.validator.validate({"key": 123}, {"type": "string"})
```

### 4.2 集成测试

```python
# test_integration.py
def test_end_to_end():
    # 1. 准备数据
    data = load_test_data()
    
    # 2. 生成Schema
    schema = JsonGeekAI.auto_schema(data)
    
    # 3. 验证数据
    report = JsonGeekAI.validate(data, schema)
    
    # 4. 检查结果
    assert report.is_valid
    assert report.validation_type == "hybrid"
```

### 4.3 性能测试

```python
# test_performance.py
def test_validation_performance():
    # 准备大量数据
    large_data = generate_large_dataset()
    
    # 测量执行时间
    start_time = time.time()
    report = JsonGeekAI.validate(large_data, schema)
    execution_time = time.time() - start_time
    
    # 验证性能指标
    assert execution_time < 1.0  # 期望小于1秒
    assert report.execution_time < 1000  # 期望小于1000ms
```

## 5. 发布流程

### 5.1 版本管理

遵循语义化版本规范：
- MAJOR.MINOR.PATCH
- 例如：1.2.3

### 5.2 发布检查清单

- [ ] 所有测试通过
- [ ] 代码风格检查通过
- [ ] 文档已更新
- [ ] CHANGELOG已更新
- [ ] 版本号已更新
- [ ] 依赖列表已更新

### 5.3 发布步骤

```bash
# 1. 更新版本号
bump2version patch  # 或 minor 或 major

# 2. 构建包
python setup.py sdist bdist_wheel

# 3. 上传到PyPI
twine upload dist/*
```

## 6. 文档维护

### 6.1 文档结构

```
docs/
├── api/              # API文档
├── examples/         # 示例代码
├── guides/           # 使用指南
└── reference/        # 参考资料
```

### 6.2 文档生成

使用Sphinx生成文档：

```bash
# 生成API文档
sphinx-apidoc -f -o docs/api src/jsongeek_cli

# 构建文档
cd docs
make html
```

## 7. 性能优化指南

### 7.1 代码优化原则

- 使用性能分析工具识别瓶颈
- 优化关键路径代码
- 合理使用缓存
- 实现并行处理

### 7.2 内存优化

```python
# 使用生成器处理大数据
def process_large_file(file_path):
    with open(file_path) as f:
        for line in f:
            yield json.loads(line)

# 使用上下文管理器
with JsonGeekAI.debug_session() as session:
    for data in process_large_file("large.json"):
        session.validate(data)
```

## 8. 安全开发指南

### 8.1 安全检查清单

- [ ] 输入验证
- [ ] 敏感数据处理
- [ ] 错误处理
- [ ] 日志安全
- [ ] 依赖检查

### 8.2 安全最佳实践

```python
# 安全的数据处理
def process_sensitive_data(data):
    try:
        # 1. 数据验证
        validate_input(data)
        
        # 2. 敏感数据处理
        sanitized = sanitize_data(data)
        
        # 3. 业务处理
        result = process_data(sanitized)
        
        # 4. 输出净化
        return sanitize_output(result)
        
    except Exception as e:
        # 5. 安全的错误处理
        log_error(e)  # 不暴露敏感信息
        raise SecurityError("处理失败")
```
