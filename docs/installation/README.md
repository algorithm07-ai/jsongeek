# 安装指南

## 系统要求

- Python 3.7 或更高版本
- 支持 AVX2 指令集的 CPU（可选，用于性能优化）

## 使用 pip 安装

```bash
pip install jsongeekai
```

## 从源代码安装

1. 克隆仓库：
```bash
git clone https://github.com/zhanghongping/jsongeek.git
cd jsongeek
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 构建和安装：
```bash
python setup.py install
```

## 验证安装

```python
import jsongeekai
print(jsongeekai.__version__)
```

## 常见问题

如果遇到任何安装问题，请查看我们的 [FAQ](../FAQ.md) 或在 [GitHub Issues](https://github.com/zhanghongping/jsongeek/issues) 上提问。
