import { LRUCache } from './LRUCache';

/**
 * 多级缓存系统
 * 实现类似 CPU 缓存的多级结构
 */
export class MultiLevelCache<K, V> {
  private readonly l1Cache: LRUCache<K, V>; // 最快，容量最小
  private readonly l2Cache: LRUCache<K, V>; // 中等速度和容量
  private readonly l3Cache: LRUCache<K, V>; // 最慢，容量最大
  
  constructor(
    l1Size: number = 100,    // L1: 100 items
    l2Size: number = 1000,   // L2: 1000 items
    l3Size: number = 10000,  // L3: 10000 items
    l1Memory: number = 10 * 1024 * 1024,   // L1: 10MB
    l2Memory: number = 50 * 1024 * 1024,   // L2: 50MB
    l3Memory: number = 200 * 1024 * 1024   // L3: 200MB
  ) {
    this.l1Cache = new LRUCache<K, V>(l1Size, l1Memory);
    this.l2Cache = new LRUCache<K, V>(l2Size, l2Memory);
    this.l3Cache = new LRUCache<K, V>(l3Size, l3Memory);
  }

  /**
   * 获取缓存项
   * 按照 L1 -> L2 -> L3 的顺序查找
   */
  get(key: K): V | undefined {
    // 先查找 L1 缓存
    let value = this.l1Cache.get(key);
    if (value !== undefined) {
      return value;
    }

    // 查找 L2 缓存
    value = this.l2Cache.get(key);
    if (value !== undefined) {
      // 提升到 L1 缓存
      this.l1Cache.set(key, value);
      return value;
    }

    // 查找 L3 缓存
    value = this.l3Cache.get(key);
    if (value !== undefined) {
      // 提升到 L2 缓存
      this.l2Cache.set(key, value);
      // 选择性提升到 L1 缓存（可以根据访问频率决定）
      if (this.shouldPromoteToL1(key)) {
        this.l1Cache.set(key, value);
      }
      return value;
    }

    return undefined;
  }

  /**
   * 设置缓存项
   * 同时更新所有级别的缓存
   */
  set(key: K, value: V, size: number = 0): void {
    // 设置 L3 缓存
    this.l3Cache.set(key, value, size);

    // 根据策略决定是否设置 L2 缓存
    if (this.shouldSetL2(size)) {
      this.l2Cache.set(key, value, size);
    }

    // 根据策略决定是否设置 L1 缓存
    if (this.shouldSetL1(size)) {
      this.l1Cache.set(key, value, size);
    }
  }

  /**
   * 移除缓存项
   * 从所有级别移除
   */
  remove(key: K): void {
    this.l1Cache.remove(key);
    this.l2Cache.remove(key);
    this.l3Cache.remove(key);
  }

  /**
   * 清空所有缓存
   */
  clear(): void {
    this.l1Cache.clear();
    this.l2Cache.clear();
    this.l3Cache.clear();
  }

  /**
   * 获取缓存统计信息
   */
  getStats(): MultiLevelCacheStats {
    return {
      l1: this.l1Cache.getStats(),
      l2: this.l2Cache.getStats(),
      l3: this.l3Cache.getStats()
    };
  }

  /**
   * 预热缓存
   * @param items 预热数据
   * @param level 预热到哪个级别 (1-3)
   */
  async warmup(items: Array<[K, V, number]>, level: number = 3): Promise<void> {
    for (const [key, value, size] of items) {
      if (level >= 3) {
        this.l3Cache.set(key, value, size);
      }
      if (level >= 2 && this.shouldSetL2(size)) {
        this.l2Cache.set(key, value, size);
      }
      if (level >= 1 && this.shouldSetL1(size)) {
        this.l1Cache.set(key, value, size);
      }
    }
  }

  /**
   * 判断是否应该提升到 L1 缓存
   */
  private shouldPromoteToL1(key: K): boolean {
    // 实现提升策略，例如基于访问频率
    return true; // 简化实现
  }

  /**
   * 判断是否应该设置 L2 缓存
   */
  private shouldSetL2(size: number): boolean {
    // 实现 L2 缓存策略
    return size <= 1024 * 1024; // 小于 1MB 的数据
  }

  /**
   * 判断是否应该设置 L1 缓存
   */
  private shouldSetL1(size: number): boolean {
    // 实现 L1 缓存策略
    return size <= 100 * 1024; // 小于 100KB 的数据
  }
}

interface MultiLevelCacheStats {
  l1: CacheStats;
  l2: CacheStats;
  l3: CacheStats;
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
