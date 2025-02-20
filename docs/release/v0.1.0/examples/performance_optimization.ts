import { HybridParser, SIMDParser, WasmParser, StreamParser } from '../src';
import { performance } from 'perf_hooks';

// 示例1：解析器预热
function parserWarmup() {
  console.log('示例1：解析器预热');
  const parser = new HybridParser();
  
  // 不预热的情况
  const start1 = performance.now();
  const result1 = parser.parse('{"name": "test"}');
  const end1 = performance.now();
  console.log(`不预热耗时: ${end1 - start1}ms`);
  
  // 预热
  for (let i = 0; i < 5; i++) {
    parser.parse('{"test": true}');
  }
  
  // 预热后的性能
  const start2 = performance.now();
  const result2 = parser.parse('{"name": "test"}');
  const end2 = performance.now();
  console.log(`预热后耗时: ${end2 - start2}ms\n`);
}

// 示例2：解析器实例重用
function parserReuse() {
  console.log('示例2：解析器实例重用');
  const jsonArray = Array(1000).fill('{"test": true}');
  
  // 不重用实例
  const start1 = performance.now();
  for (const json of jsonArray) {
    const parser = new HybridParser();
    const result = parser.parse(json);
  }
  const end1 = performance.now();
  console.log(`不重用实例耗时: ${end1 - start1}ms`);
  
  // 重用实例
  const start2 = performance.now();
  const parser = new HybridParser();
  for (const json of jsonArray) {
    const result = parser.parse(json);
  }
  const end2 = performance.now();
  console.log(`重用实例耗时: ${end2 - start2}ms\n`);
}

// 示例3：不同解析器性能对比
async function parserComparison() {
  console.log('示例3：不同解析器性能对比');
  const smallJson = '{"name": "test", "value": 123}';
  const mediumJson = JSON.stringify({ data: Array(1000).fill({ test: true }) });
  const largeJson = JSON.stringify({ data: Array(10000).fill({ test: true }) });
  
  const parsers = {
    WasmParser: new WasmParser(),
    SIMDParser: new SIMDParser(),
    HybridParser: new HybridParser()
  };
  
  const testCases = {
    'Small JSON (< 1KB)': smallJson,
    'Medium JSON (~100KB)': mediumJson,
    'Large JSON (~1MB)': largeJson
  };
  
  for (const [caseName, json] of Object.entries(testCases)) {
    console.log(`\n测试场景: ${caseName}`);
    for (const [parserName, parser] of Object.entries(parsers)) {
      const start = performance.now();
      const result = parser.parse(json);
      const end = performance.now();
      console.log(`${parserName} 耗时: ${end - start}ms`);
    }
  }
  console.log();
}

// 示例4：流式解析大文件
function streamParsing() {
  console.log('示例4：流式解析大文件');
  const largeJson = JSON.stringify({ data: Array(10000).fill({ test: true }) });
  
  // 常规解析
  const start1 = performance.now();
  const parser = new HybridParser();
  const result1 = parser.parse(largeJson);
  const end1 = performance.now();
  console.log(`常规解析耗时: ${end1 - start1}ms`);
  
  // 流式解析
  const start2 = performance.now();
  const streamParser = new StreamParser();
  let valueCount = 0;
  streamParser.onValue = () => {
    valueCount++;
  };
  
  // 模拟分块处理
  const chunkSize = 1024;
  for (let i = 0; i < largeJson.length; i += chunkSize) {
    const chunk = largeJson.slice(i, i + chunkSize);
    streamParser.write(chunk);
  }
  streamParser.end();
  
  const end2 = performance.now();
  console.log(`流式解析耗时: ${end2 - start2}ms`);
  console.log(`处理的值数量: ${valueCount}\n`);
}

// 示例5：内存使用优化
function memoryOptimization() {
  console.log('示例5：内存使用优化');
  const json = JSON.stringify({ data: Array(1000).fill({ test: true }) });
  
  // 不优化内存
  const start1 = performance.now();
  const baseHeap1 = process.memoryUsage().heapUsed;
  const parser1 = new HybridParser();
  const result1 = parser1.parse(json);
  const endHeap1 = process.memoryUsage().heapUsed;
  const end1 = performance.now();
  console.log(`不优化内存使用: ${(endHeap1 - baseHeap1) / 1024 / 1024}MB`);
  
  // 优化内存
  const start2 = performance.now();
  const baseHeap2 = process.memoryUsage().heapUsed;
  const parser2 = new HybridParser({ useSharedMemory: true });
  const result2 = parser2.parse(json);
  parser2.dispose(); // 及时释放内存
  const endHeap2 = process.memoryUsage().heapUsed;
  const end2 = performance.now();
  console.log(`优化后内存使用: ${(endHeap2 - baseHeap2) / 1024 / 1024}MB\n`);
}

// 运行所有示例
async function runAllExamples() {
  console.log('JsonGeek 性能优化示例\n');
  parserWarmup();
  parserReuse();
  await parserComparison();
  streamParsing();
  memoryOptimization();
}

runAllExamples().catch(console.error);
