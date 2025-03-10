import * as readline from 'readline';
import { OptimizedParser } from './src/core/parser/OptimizedParser';

class JsonGeekBridge {
    private parser: OptimizedParser;
    private rl: readline.Interface;

    constructor() {
        this.parser = new OptimizedParser();
        this.rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });
    }

    async initialize(): Promise<void> {
        try {
            await this.parser.initialize();
            console.error('JsonGeekAI bridge initialized');
        } catch (error) {
            console.error('Failed to initialize JsonGeekAI:', error);
            process.exit(1);
        }
    }

    start(): void {
        this.rl.on('line', async (input: string) => {
            try {
                const result = await this.parser.parse(input);
                console.log(JSON.stringify(result));
            } catch (error) {
                console.error('Parse error:', error);
                process.exit(1);
            }
        });

        this.rl.on('close', () => {
            process.exit(0);
        });
    }
}

// 启动桥接程序
const bridge = new JsonGeekBridge();
bridge.initialize().then(() => {
    bridge.start();
}).catch(error => {
    console.error('Bridge initialization failed:', error);
    process.exit(1);
});
