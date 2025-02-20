# 贡献指南

感谢你对 JsonGeekAI 项目的关注！我们欢迎各种形式的贡献。

## 如何贡献

1. Fork 项目仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的改动 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

## 开发环境设置

1. 克隆仓库：
```bash
git clone https://github.com/YOUR_USERNAME/jsongeek.git
cd jsongeek
```

2. 安装开发依赖：
```bash
pip install -r requirements-dev.txt
```

3. 运行测试：
```bash
python -m pytest tests/
```

## 代码风格

我们使用 PEP 8 作为 Python 代码风格指南。在提交代码前，请确保：

1. 使用 4 个空格缩进
2. 行长度不超过 79 个字符
3. 适当的空行分隔
4. 有意义的变量和函数名

## 提交 Pull Request

1. 更新 CHANGELOG.md
2. 如果添加了新功能，请更新文档
3. 确保所有测试都通过
4. 确保代码符合我们的代码风格要求

## 报告问题

如果你发现了 bug 或有新功能建议，请：

1. 检查是否已经有相关的 issue
2. 如果没有，创建一个新的 issue
3. 清晰地描述问题或建议
4. 如果可能，提供重现步骤或示例代码

## 许可证

通过贡献代码，你同意你的贡献将使用 MIT 许可证。
