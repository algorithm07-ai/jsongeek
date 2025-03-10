import { Suite } from 'benchmark';
import { StreamProcessor } from '../../extension/src/core/processor/StreamProcessor';
import FastJson2 from 'fastjson2';

export class JsonBenchmark {
  private static generateLargeJson(size: number): string {
    const obj = {
      id: 1,
      name: 'test',
      numbers: Array.from({ length: size }, (_, i) => i),
      nested: {
        field1: 'value1',
        field2: 'value2',
        array: Array.from({ length: size }, (_, i) => ({
          id: i,
          value: `value${i}`
        }))
      }
    };
    return JSON.stringify(obj);
  }

  static async runBenchmarks() {
    const suite = new Suite();
    
    // 准备测试数据
    const smallJson = this.generateLargeJson(100);
    const mediumJson = this.generateLargeJson(10000);
    const largeJson = this.generateLargeJson(100000);

    // 小数据集测试
    suite.add('FastJson2 - Small', () => {
      FastJson2.parse(smallJson);
    })
    .add('JsonGeek - Small', async () => {
      const processor = new StreamProcessor();
      const stream = new ReadableStream({
        start(controller) {
          controller.enqueue(new TextEncoder().encode(smallJson));
          controller.close();
        }
      });
      for await (const _ of processor.processStream(stream)) {
        // 处理数据
      }
    });

    // 中等数据集测试
    suite.add('FastJson2 - Medium', () => {
      FastJson2.parse(mediumJson);
    })
    .add('JsonGeek - Medium', async () => {
      const processor = new StreamProcessor();
      const stream = new ReadableStream({
        start(controller) {
          controller.enqueue(new TextEncoder().encode(mediumJson));
          controller.close();
        }
      });
      for await (const _ of processor.processStream(stream)) {
        // 处理数据
      }
    });

    // 大数据集测试
    suite.add('FastJson2 - Large', () => {
      FastJson2.parse(largeJson);
    })
    .add('JsonGeek - Large', async () => {
      const processor = new StreamProcessor();
      const stream = new ReadableStream({
        start(controller) {
          controller.enqueue(new TextEncoder().encode(largeJson));
          controller.close();
        }
      });
      for await (const _ of processor.processStream(stream)) {
        // 处理数据
      }
    });

    // 运行基准测试
    suite.on('cycle', (event: any) => {
      console.log(String(event.target));
    })
    .on('complete', function(this: any) {
      console.log('Fastest is ' + this.filter('fastest').map('name'));
    })
    .run({ async: true });
  }
}
