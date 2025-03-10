import { MultiLevelCache } from '../cache/MultiLevelCache';
import { StringPool } from './StringPool';

/**
 * 优化的 JSON 解析器
 * 结合缓存和字符串优化
 */
export class OptimizedParser {
    private cache: MultiLevelCache<string, any>;
    private stringPool: StringPool;

    constructor() {
        this.cache = new MultiLevelCache();
        this.stringPool = new StringPool();
    }

    /**
     * 初始化解析器
     */
    async initialize(): Promise<void> {
        // 暂时不需要初始化
        return Promise.resolve();
    }

    /**
     * 解析 JSON 字符串
     */
    async parse(json: string): Promise<any> {
        // 1. 检查缓存
        const cached = this.cache.get(json);
        if (cached !== undefined) {
            return cached;
        }

        // 2. 使用字符串池
        const pooledJson = this.stringPool.intern(json);

        // 3. 解析JSON
        const result = JSON.parse(pooledJson);

        // 4. 如果结果是对象或数组，递归处理所有字符串值
        if (typeof result === 'object' && result !== null) {
            this.internObjectStrings(result);
        }

        // 5. 缓存结果
        this.cache.set(json, result);

        return result;
    }

    /**
     * 递归处理对象中的字符串
     */
    private internObjectStrings(obj: any): void {
        if (Array.isArray(obj)) {
            for (let i = 0; i < obj.length; i++) {
                const value = obj[i];
                if (typeof value === 'string') {
                    obj[i] = this.stringPool.intern(value);
                } else if (typeof value === 'object' && value !== null) {
                    this.internObjectStrings(value);
                }
            }
        } else {
            for (const key in obj) {
                const value = obj[key];
                // 处理键
                const internedKey = this.stringPool.intern(key);
                if (key !== internedKey) {
                    obj[internedKey] = obj[key];
                    delete obj[key];
                }
                // 处理值
                if (typeof value === 'string') {
                    obj[internedKey] = this.stringPool.intern(value);
                } else if (typeof value === 'object' && value !== null) {
                    this.internObjectStrings(value);
                }
            }
        }
    }
}
