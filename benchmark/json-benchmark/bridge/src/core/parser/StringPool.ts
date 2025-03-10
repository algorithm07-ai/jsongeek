/**
 * 字符串池
 * 用于减少重复字符串的内存占用
 */
export class StringPool {
    private pool: Map<string, string>;

    constructor() {
        this.pool = new Map();
    }

    /**
     * 获取或添加字符串到池中
     */
    intern(str: string): string {
        let pooled = this.pool.get(str);
        if (!pooled) {
            this.pool.set(str, str);
            pooled = str;
        }
        return pooled;
    }

    /**
     * 清空字符串池
     */
    clear(): void {
        this.pool.clear();
    }

    /**
     * 获取池中字符串数量
     */
    size(): number {
        return this.pool.size;
    }
}
