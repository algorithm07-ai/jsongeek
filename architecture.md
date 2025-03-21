# JsonGeek 架构文档

## 1. 整体架构

### 1.1 核心模块
```
core/
├── context/      # 上下文管理
├── detector/     # 类型检测
├── processor/    # 数据处理
├── schema/       # Schema 相关
└── visualization/ # 可视化
```

### 1.2 扩展模块
```
extension/
├── content/    # 内容脚本
├── devtools/   # 开发者工具
├── popup/      # 弹出窗口
└── sandbox/    # 沙箱环境
```

## 2. 模块说明

### 2.1 上下文管理 (context)
- **ConversationContext**: 会话上下文管理器
  - 用户偏好存储
  - 查询历史跟踪
  - Schema 模式记录
  - 状态持久化

### 2.2 类型检测 (detector)
- **DetectorSystem**: 多维度检测系统
  - 日期格式检测
  - 数值范围验证
  - 正则表达式匹配
  - 结构模式识别

### 2.3 数据处理 (processor)
- **StreamProcessor**: 流式处理器
  - 大规模 JSON 处理
  - 分片策略
  - 内存优化
  - 进度跟踪

### 2.4 Schema 处理 (schema)
- **SchemaInference**: Schema 推断引擎
  - 概率分布分析
  - 类型推断
  - 格式检测
  - 置信度计算

### 2.5 可视化 (visualization)
- **ForceGraph**: 力导向图实现
  - D3.js 集成
  - 鱼眼效果
  - 交互支持
  - 主题切换

## 3. 数据流

### 3.1 JSON 处理流程
```
输入 JSON
  ↓
StreamProcessor (分片处理)
  ↓
DetectorSystem (类型检测)
  ↓
SchemaInference (模式推断)
  ↓
ForceGraph (可视化)
```

### 3.2 上下文更新流程
```
用户操作
  ↓
ConversationContext (记录)
  ↓
存储系统 (持久化)
  ↓
下次启动 (恢复)
```

## 4. 安全机制

### 4.1 权限控制
- 最小权限原则
- Host 权限精确匹配
- 资源访问限制

### 4.2 内容隔离
- 样式隔离
- 脚本沙箱
- CSP 策略

### 4.3 数据保护
- 本地存储加密
- 敏感数据处理
- 跨域安全

## 5. 性能优化

### 5.1 内存管理
- 流式处理
- 分片策略
- 资源释放

### 5.2 渲染优化
- 虚拟滚动
- 延迟加载
- 局部更新

### 5.3 缓存策略
- 会话缓存
- Schema 缓存
- 可视化缓存

## 6. 扩展性

### 6.1 插件系统
- 检测器插件
- 可视化插件
- 格式化插件

### 6.2 API 设计
- 模块化接口
- 事件系统
- 配置系统

## 7. 开发指南

### 7.1 开发环境
- TypeScript
- Webpack
- Chrome Extension APIs

### 7.2 调试工具
- Chrome DevTools
- 日志系统
- 性能监控

### 7.3 测试策略
- 单元测试
- 集成测试
- E2E 测试

## 8. 部署流程

### 8.1 构建
1. 代码检查
2. 依赖安装
3. TypeScript 编译
4. 资源打包

### 8.2 发布
1. 版本管理
2. 打包发布
3. 商店上传

### 8.3 更新
1. 自动更新
2. 版本检查
3. 配置迁移
