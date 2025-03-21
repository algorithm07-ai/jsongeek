# JsonGeek 开发者指南

## 1. 开发环境搭建

### 1.1 环境要求
- Node.js >= 16
- npm >= 7
- Chrome >= 88
- TypeScript >= 4.5

### 1.2 初始化项目
```bash
# 克隆仓库
git clone https://github.com/your-username/jsongeek.git

# 安装依赖
cd jsongeek
npm install

# 启动开发服务器
npm run dev
```

### 1.3 目录结构
```
jsongeek/
├── src/            # 源代码
├── tests/          # 测试文件
├── docs/           # 文档
└── public/         # 静态资源
```

## 2. 核心模块开发

### 2.1 上下文管理
```typescript
// src/core/context/ConversationContext.ts
class ConversationContext {
  // 实现会话管理
}
```

### 2.2 数据处理
```typescript
// src/core/processor/StreamProcessor.ts
class StreamProcessor {
  // 实现流处理
}
```

### 2.3 Schema 处理
```typescript
// src/core/schema/SchemaInference.ts
class SchemaInference {
  // 实现 Schema 推断
}
```

## 3. 扩展开发

### 3.1 添加检测器
```typescript
// src/core/detector/CustomDetector.ts
class CustomDetector implements Detector {
  name = 'custom';
  description = '自定义检测器';
  priority = 100;

  check(value: any): DetectorResult {
    // 实现检测逻辑
    return {
      valid: true,
      confidence: 0.9
    };
  }
}
```

### 3.2 添加可视化
```typescript
// src/core/visualization/CustomView.ts
class CustomView {
  constructor(container: HTMLElement) {
    // 初始化视图
  }

  render(data: any) {
    // 实现渲染逻辑
  }
}
```

## 4. 测试指南

### 4.1 单元测试
```typescript
// tests/unit/schema.test.ts
describe('SchemaInference', () => {
  it('should infer correct type', () => {
    const inference = new SchemaInference();
    inference.addSample({ name: 'test' });
    const schema = inference.getSchema();
    expect(schema.type).toBe('object');
  });
});
```

### 4.2 集成测试
```typescript
// tests/integration/processor.test.ts
describe('StreamProcessor', () => {
  it('should process large files', async () => {
    const processor = new StreamProcessor();
    const stream = createTestStream();
    const results = [];
    
    for await (const chunk of processor.processStream(stream)) {
      results.push(chunk);
    }
    
    expect(results).toHaveLength(10);
  });
});
```

## 5. 性能优化

### 5.1 内存管理
```typescript
class MemoryManager {
  private maxMemory: number;
  private used: number = 0;

  constructor(maxMemory: number) {
    this.maxMemory = maxMemory;
  }

  allocate(size: number): boolean {
    if (this.used + size > this.maxMemory) {
      return false;
    }
    this.used += size;
    return true;
  }

  release(size: number): void {
    this.used -= size;
  }
}
```

### 5.2 缓存策略
```typescript
class Cache<T> {
  private items = new Map<string, T>();
  private maxSize: number;

  constructor(maxSize: number) {
    this.maxSize = maxSize;
  }

  set(key: string, value: T): void {
    if (this.items.size >= this.maxSize) {
      const firstKey = this.items.keys().next().value;
      this.items.delete(firstKey);
    }
    this.items.set(key, value);
  }

  get(key: string): T | undefined {
    return this.items.get(key);
  }
}
```

## 6. 发布流程

### 6.1 版本管理
```bash
# 更新版本号
npm version patch|minor|major

# 构建项目
npm run build

# 打包扩展
npm run pack
```

### 6.2 发布检查清单
1. 更新版本号
2. 更新 CHANGELOG.md
3. 运行测试套件
4. 构建生产版本
5. 提交代码审查
6. 创建发布标签
7. 发布到商店

## 7. 调试技巧

### 7.1 Chrome DevTools
1. 打开扩展开发者工具
2. 使用 Sources 面板调试
3. 查看 Console 输出
4. 分析性能问题

### 7.2 日志记录
```typescript
class Logger {
  static debug(message: string, ...args: any[]) {
    if (process.env.NODE_ENV !== 'production') {
      console.debug(`[JsonGeek] ${message}`, ...args);
    }
  }

  static error(error: Error) {
    console.error(`[JsonGeek] Error:`, error);
  }
}
```

## 8. 代码规范

### 8.1 TypeScript 规范
- 使用严格模式
- 添加类型注解
- 避免 any 类型
- 使用接口定义

### 8.2 命名规范
- 类名：PascalCase
- 方法名：camelCase
- 常量：UPPER_CASE
- 私有成员：_prefixed

### 8.3 注释规范
```typescript
/**
 * 类描述
 */
class Example {
  /**
   * 方法描述
   * @param param 参数描述
   * @returns 返回值描述
   * @throws 异常描述
   */
  method(param: string): number {
    // 实现逻辑
  }
}
```

## 9. 常见问题

### 9.1 开发问题
Q: 热重载不生效？
A: 检查 webpack 配置和文件监听。

Q: 类型错误？
A: 确保 tsconfig.json 配置正确。

### 9.2 调试问题
Q: 断点不触发？
A: 检查 source map 配置。

Q: 控制台报错？
A: 查看权限配置和 CSP 策略。

## 10. 参考资源

- [TypeScript 文档](https://www.typescriptlang.org/docs)
- [Chrome 扩展开发](https://developer.chrome.com/docs/extensions)
- [D3.js 文档](https://d3js.org/)
