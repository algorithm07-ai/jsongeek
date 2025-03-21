# JsonGeek

[![Build Status](https://github.com/algorithm07-ai/jsongeek/workflows/CI/badge.svg)](https://github.com/algorithm07-ai/jsongeek/actions)
[![npm version](https://badge.fury.io/js/jsongeek.svg)](https://www.npmjs.com/package/jsongeek)
[![PyPI version](https://badge.fury.io/py/jsongeek.svg)](https://pypi.org/project/jsongeek/)
[![Documentation Status](https://readthedocs.org/projects/jsongeek/badge/?version=latest)](https://jsongeek.readthedocs.io/)
[![Code Quality](https://app.codacy.com/project/badge/Grade/123456)](https://www.codacy.com/gh/algorithm07-ai/jsongeek)
[![Coverage](https://codecov.io/gh/algorithm07-ai/jsongeek/branch/master/graph/badge.svg)](https://codecov.io/gh/algorithm07-ai/jsongeek)
[![Performance](https://img.shields.io/badge/performance-SIMD-brightgreen.svg)](https://github.com/algorithm07-ai/jsongeek)
[![MCP Compliant](https://img.shields.io/badge/MCP-compliant-blue.svg)](https://github.com/algorithm07-ai/jsongeek)

JsonGeek 是一个基于 MCP 协议和 DeepSeek LLM 的高性能 JSON 处理引擎，提供智能分析、验证和可视化功能。

## 核心特性

- 🚀 SIMD 加速，处理性能 < 2秒/10MB
- 🧠 DeepSeek LLM 深度集成
- 🛡️ 多层验证架构，准确率 > 99.9%
- 📊 内存高效，占用 < 500MB# JsonGeek 

JsonGeek 是一个强大的 Chrome 扩展，用于 JSON 数据的处理、分析和可视化。

## 项目结构

```
jsongeek/
├── extension/                    # Chrome 扩展
│   ├── src/                     # 源代码
│   │   ├── background/          # 后台脚本
│   │   │   └── index.ts        # 后台入口
│   │   ├── content/            # 内容脚本
│   │   │   └── index.ts        # 内容脚本入口
│   │   ├── popup/              # 弹出窗口
│   │   │   ├── components/     # UI 组件
│   │   │   └── index.tsx       # 弹窗入口
│   │   └── utils/              # 工具函数
│   ├── public/                  # 静态资源
│   │   └── icons/              # 扩展图标
│   ├── manifest.json            # 扩展配置
│   └── package.json            # 包配置
│
├── benchmark/              # 性能测试框架
│   ├── json-benchmark/    # JSON性能测试
│   │   ├── src/          # 源代码
│   │   │   ├── main/     # 主要实现
│   │   │   └── test/     # 测试用例
│   │   └── docs/         # 文档
│   └── results/          # 测试结果
│
├── website/                     # 扩展文档网站
│   ├── src/                    # 源代码
│   │   ├── pages/             # 页面组件
│   │   │   ├── docs/         # 文档页面
│   │   │   └── examples/     # 示例页面
│   │   └── components/       # 共享组件
│   ├── public/                # 静态资源
│   │   ├── images/          # 图片资源
│   │   └── icons/           # 图标资源
│   └── package.json          # 包配置
│
├── docs/                 # 项目文档
│   ├── zh-CN/           # 中文文档
│   └── en-US/           # 英文文档
│
├── package.json               # 根配置
└── README.md                 # 项目说明
```

## 功能特性

1. **JSON 数据处理**
   - 自动检测页面中的 JSON 数据
   - 格式化和语法高亮
   - 数据复制和导出

2. **数据分析**
   - JSONPath 查询
   - 数据统计和分析
   - 结构可视化

3. **开发工具**
   - API 调试助手
   - 数据验证
   - 格式转换

4. **SIMD 优化**
   - SIMD 加速的 JSON 解析
   - SIMD 优化的数据处理

## 测试框架

我们采用分级测试策略（P0-P2）来确保代码质量：

### P0级别（核心测试）
- **范围**：语法和边界测试
- **执行**：强制执行，阻塞发布
- **工具**：JSONTestSuite

### P1级别（标准测试）
- **范围**：Schema验证、RFC合规性
- **执行**：常规执行，可选发布
- **工具**：JSON Schema Test Suite

### P2级别（扩展测试）
- **范围**：性能测试、边缘场景
- **执行**：选择性执行，建议发布
- **工具**：自定义性能测试套件

## 开发指南

### 环境要求

- Node.js >= 18
- pnpm >= 8
- Chrome >= 88

### 安装依赖

```bash
pnpm install
```

### 开发扩展

```bash
# 开发模式
pnpm dev:extension

# 构建扩展
pnpm build:extension
```

### 开发文档网站

```bash
# 开发模式
pnpm dev:website

# 构建网站
pnpm build:website
```

## 测试策略

我们遵循 P0-P2 分类策略来组织我们的测试套件：

### P0 (强制)
- 语法和边界测试
- 核心功能验证
- SIMD 优化验证
- 内存使用基准测试

### P1 (常规)
- 结构和语义验证
- API 兼容性测试
- 性能回归测试
- 跨平台验证

### P2 (可选)
- 扩展测试用例
- 边缘情况场景
- 压力测试
- 集成测试

## 发布流程

1. 更新版本号：
   ```bash
   pnpm version patch # 或 minor/major
   ```

2. 构建扩展：
   ```bash
   pnpm build:extension
   ```

3. 打包扩展：
   ```bash
   pnpm pack:extension
   ```

4. 在 Chrome Web Store 发布新版本

## 许可证

MIT

# JsonGeek

强大的 JSON 数据处理、分析和可视化工具

## 功能特性

### 1. 智能分析
- 上下文感知增强
- 会话记忆支持
- Schema 智能推断
- 多维度类型检测

### 2. 大数据支持
- 流式处理
- 分片策略
- 内存优化
- 渐进式分析

### 3. 可视化
- 力导向图
- 鱼眼放大镜
- 主题切换
- 交互优化

### 4. 安全性
- 最小权限原则
- 资源访问控制
- 内容隔离
- 沙箱执行

## 目录结构

```
jsongeek/
├── extension/          # 扩展主目录
│   ├── manifest.json   # 扩展配置
│   └── src/           # 源代码
│       ├── core/      # 核心功能
│       │   ├── context/     # 上下文管理
│       │   ├── detector/    # 检测器
│       │   ├── processor/   # 数据处理
│       │   ├── schema/      # Schema 相关
│       │   └── visualization/ # 可视化
│       ├── content/    # 内容脚本
│       ├── devtools/   # 开发者工具
│       ├── popup/      # 弹出窗口
│       └── sandbox/    # 沙箱环境
└── docs/             # 文档
    ├── CHANGELOG.md  # 更新日志
    └── README.md     # 说明文档
```

## 核心模块

### 1. ConversationContext
会话上下文管理，负责：
- 用户偏好存储
- 查询历史跟踪
- Schema 模式记录

### 2. StreamProcessor
流式处理器，支持：
- 大规模 JSON 处理
- 内存使用优化
- 进度跟踪

### 3. SchemaInference
Schema 推断引擎：
- 概率分布分析
- 智能类型推断
- 置信度计算

### 4. DetectorSystem
多维度检测系统：
- 日期格式检测
- 数值范围验证
- 正则表达式匹配
- 结构识别

### 5. ForceGraph
力导向图可视化：
- D3.js 实现
- 鱼眼效果
- 交互支持

## 使用方法

### 安装
1. 克隆仓库
2. 安装依赖：`npm install`
3. 构建项目：`npm run build`
4. 在 Chrome 中加载扩展

### 快捷键
- `Ctrl+Shift+J`: 打开 JsonGeek
- `Alt+Shift+F`: 格式化 JSON
- `Alt+Shift+M`: 压缩 JSON

### 可视化
```typescript
const visualizer = new JsonVisualizer({
  container: document.getElementById('graph'),
  width: 800,
  height: 600,
  theme: 'dark'
});

visualizer.visualize(jsonData);
```

### 流式处理
```typescript
const processor = new StreamProcessor();
for await (const chunk of processor.processStream(response.body)) {
  // 处理数据块
}
```

## 贡献指南

1. Fork 项目
2. 创建特性分支
3. 提交改动
4. 发起 Pull Request

## 许可证

MIT License
