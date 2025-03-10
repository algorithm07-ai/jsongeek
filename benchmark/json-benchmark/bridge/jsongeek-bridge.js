const readline = require('readline');
const { OptimizedParser } = require('../../extension/src/core/parser/OptimizedParser');

// 创建解析器实例
const parser = new OptimizedParser();

// 初始化解析器
(async () => {
    await parser.initialize();
    
    // 创建readline接口
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    // 处理输入
    rl.on('line', async (input) => {
        try {
            // 解析JSON
            const result = await parser.parse(input);
            // 将结果转换回JSON字符串并输出
            console.log(JSON.stringify(result));
        } catch (error) {
            console.error(error.message);
            process.exit(1);
        }
    });

    // 处理关闭
    rl.on('close', () => {
        process.exit(0);
    });
})();
