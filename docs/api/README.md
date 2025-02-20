# JsonGeek API 文档

## 安装

```bash
npm install jsongeek
```

## 基本用法

```typescript
import { WasmParser, SIMDParser, HybridParser } from 'jsongeek';

// 创建解析器实例
const parser = new HybridParser(); // 推荐使用混合解析器

// 解析JSON
const json = '{"name": "John", "age": 30}';
const result = parser.parse(json);
console.log(result); // { name: 'John', age: 30 }
```

## 解析器类型

### 1. 基础解析器 (WasmParser)

基于WebAssembly的基础JSON解析器，适用于小型JSON数据。

```typescript
import { WasmParser } from 'jsongeek';

const parser = new WasmParser();
const result = parser.parse('{"key": "value"}');
```

特点：
- 内存占用小
- 适合简单JSON
- 稳定可靠

### 2. SIMD解析器 (SIMDParser)

使用SIMD优化的解析器，适用于大型数组和规则数据。

```typescript
import { SIMDParser } from 'jsongeek';

const parser = new SIMDParser();
const result = parser.parse('[1,2,3,4,5,6,7,8]');
```

特点：
- 并行处理
- 高性能
- 适合大型数组

### 3. 混合解析器 (HybridParser)

智能选择最佳解析策略的解析器，推荐使用。

```typescript
import { HybridParser } from 'jsongeek';

const parser = new HybridParser();
const result = parser.parse(jsonString);
```

特点：
- 自适应选择
- 综合性能最佳
- 通用性强

## 性能指标

| 测试用例 | 数据大小 | 混合解析器 | SIMD解析器 | 基础解析器 |
|---------|---------|------------|------------|------------|
| 简单对象 | 0.04 KB | 867K ops/s | 981K ops/s | 747K ops/s |
| 简单数组 | 0.01 KB | 1.27M ops/s| 1.28M ops/s| 1.15M ops/s|
| 嵌套对象 | 0.11 KB | 1.00M ops/s| 985K ops/s | 1.00M ops/s|
| 字符串数组| 0.08 KB | 1.32M ops/s| 1.22M ops/s| 867K ops/s |
| 复杂数据 | 0.15 KB | 1.23M ops/s| 790K ops/s | 992K ops/s |

## 错误处理

所有解析器都会在遇到无效JSON时抛出错误：

```typescript
try {
  parser.parse('{"invalid": json}');
} catch (error) {
  console.error('解析错误:', error.message);
}
```

常见错误类型：
- 语法错误
- 未闭合的字符串
- 无效的数字格式
- 未闭合的数组或对象

## 最佳实践

1. **选择合适的解析器**
   - 小型JSON（<1KB）：使用基础解析器
   - 大型数组：使用SIMD解析器
   - 不确定场景：使用混合解析器

2. **性能优化**
   - 重复使用解析器实例
   - 避免不必要的JSON序列化/反序列化
   - 考虑数据大小选择合适的解析器

3. **错误处理**
   - 始终使用try-catch包装解析操作
   - 在生产环境中记录解析错误
   - 提供用户友好的错误信息

## 版本兼容性

- Node.js: >=14.0.0
- 浏览器: 支持WebAssembly的现代浏览器
- TypeScript: >=4.0.0

## 限制说明

1. **内存使用**
   - SIMD解析器可能需要更多内存
   - 处理超大JSON时注意内存限制

2. **浏览器兼容性**
   - 需要WebAssembly支持
   - SIMD功能可能需要更新的浏览器

3. **性能考虑**
   - 小数据可能有额外开销
   - 首次加载需要编译WebAssembly

## 贡献指南

1. Fork 项目
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建Pull Request

## 许可证

MIT License
