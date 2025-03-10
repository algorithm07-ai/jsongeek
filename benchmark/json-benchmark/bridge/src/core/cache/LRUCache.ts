/**
 * LRU (Least Recently Used) 缓存实现
 */
export class LRUCache<K, V> {
  private cache: Map<K, V>;
  private keyOrder: K[];
  private readonly maxSize: number;
  private readonly maxMemory: number;
  private currentMemory: number;
  private hits: number;
  private misses: number;

  constructor(maxSize: number = 1000, maxMemory: number = 100 * 1024 * 1024) { // 默认100MB
    this.cache = new Map();
    this.keyOrder = [];
    this.maxSize = maxSize;
    this.maxMemory = maxMemory;
    this.currentMemory = 0;
    this.hits = 0;
    this.misses = 0;
  }

  /**
   * 获取缓存项
   */
  get(key: K): V | undefined {
    const value = this.cache.get(key);
    
    if (value !== undefined) {
      // 更新访问顺序
      this.updateOrder(key);
      this.hits++;
      return value;
    }
    
    this.misses++;
    return undefined;
  }

  /**
   * 设置缓存项
   */
  set(key: K, value: V, size: number = 0): void {
    // 检查内存限制
    if (size > this.maxMemory) {
      throw new Error('Item size exceeds maximum memory limit');
    }

    // 如果键已存在，先移除
    if (this.cache.has(key)) {
      this.removeItem(key);
    }

    // 确保有足够空间
    while (
      (this.cache.size >= this.maxSize || this.currentMemory + size > this.maxMemory) &&
      this.keyOrder.length > 0
    ) {
      const oldestKey = this.keyOrder[0];
      this.removeItem(oldestKey);
    }

    // 添加新项
    this.cache.set(key, value);
    this.keyOrder.push(key);
    this.currentMemory += size;
  }

  /**
   * 移除缓存项
   */
  remove(key: K): boolean {
    return this.removeItem(key);
  }

  /**
   * 清空缓存
   */
  clear(): void {
    this.cache.clear();
    this.keyOrder = [];
    this.currentMemory = 0;
    this.hits = 0;
    this.misses = 0;
  }

  /**
   * 获取缓存统计信息
   */
  getStats(): CacheStats {
    return {
      size: this.cache.size,
      maxSize: this.maxSize,
      currentMemory: this.currentMemory,
      maxMemory: this.maxMemory,
      hits: this.hits,
      misses: this.misses,
      hitRate: this.hits / (this.hits + this.misses || 1)
    };
  }

  /**
   * 预热缓存
   */
  async warmup(items: Array<[K, V, number]>): Promise<void> {
    for (const [key, value, size] of items) {
      this.set(key, value, size);
    }
  }

  /**
   * 更新访问顺序
   */
  private updateOrder(key: K): void {
    const index = this.keyOrder.indexOf(key);
    if (index > -1) {
      this.keyOrder.splice(index, 1);
      this.keyOrder.push(key);
    }
  }

  /**
   * 移除缓存项
   */
  private removeItem(key: K): boolean {
    const index = this.keyOrder.indexOf(key);
    if (index > -1) {
      this.keyOrder.splice(index, 1);
      this.cache.delete(key);
      return true;
    }
    return false;
  }
}

interface CacheStats {
  size: number;
  maxSize: number;
  currentMemory: number;
  maxMemory: number;
  hits: number;
  misses: number;
  hitRate: number;
}
