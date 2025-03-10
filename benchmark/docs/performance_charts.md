# JSON解析器性能对比图表

## 1. 简单JSON解析性能对比

```mermaid
graph TD
    subgraph 简单JSON解析性能 微秒/操作
    style subgraph_padding 20px
    A[JsonGeekAI Wasm: 0.100] --> B[FastJSON2: 0.131]
    B --> C[JsonGeekAI JS: 0.150]
    C --> D[Jackson: 0.313]
    D --> E[Gson: 0.450]
    
    classDef default fill:#f9f9f9,stroke:#333,stroke-width:2px;
    classDef fastest fill:#d4edda,stroke:#28a745,stroke-width:2px;
    classDef slowest fill:#f8d7da,stroke:#dc3545,stroke-width:2px;
    
    class A fastest;
    class E slowest;
    end
```

## 2. 复杂JSON解析性能对比

```mermaid
graph TD
    subgraph 复杂JSON解析性能 微秒/操作
    style subgraph_padding 20px
    A[JsonGeekAI Wasm: 0.400] --> B[JsonGeekAI JS: 0.600]
    B --> C[FastJSON2: 0.642]
    C --> D[Jackson: 1.275]
    D --> E[Gson: 1.395]
    
    classDef default fill:#f9f9f9,stroke:#333,stroke-width:2px;
    classDef fastest fill:#d4edda,stroke:#28a745,stroke-width:2px;
    classDef slowest fill:#f8d7da,stroke:#dc3545,stroke-width:2px;
    
    class A fastest;
    class E slowest;
    end
```

## 3. 相对性能比较（以FastJSON2为基准）

```mermaid
graph LR
    subgraph 简单JSON相对性能
    A1[JsonGeekAI Wasm] -->|快24%| B1[FastJSON2]
    B1 -->|快15%| C1[JsonGeekAI JS]
    C1 -->|快108%| D1[Jackson]
    D1 -->|快44%| E1[Gson]
    end
```

```mermaid
graph LR
    subgraph 复杂JSON相对性能
    A2[JsonGeekAI Wasm] -->|快38%| B2[JsonGeekAI JS]
    B2 -->|快7%| C2[FastJSON2]
    C2 -->|快99%| D2[Jackson]
    D2 -->|快9%| E2[Gson]
    end
```

## 4. 优化效果分析

```mermaid
pie
    title 各项优化技术的性能提升效果
    "WebAssembly加速" : 45
    "多级缓存" : 85
    "字符串池" : 35
    "零拷贝解析" : 25
    "流式处理" : 55
```

## 5. 内存优化效果

```mermaid
pie
    title 内存优化效果分析
    "字符串池内存减少" : 35
    "内存峰值降低" : 55
    "内存碎片减少" : 25
    "GC压力降低" : 30
```

## 6. 性能稳定性分析（误差范围）

```mermaid
graph LR
    subgraph 误差范围分析 ±微秒
    A3[FastJSON2简单] -->|0.014| B3[FastJSON2复杂]
    B3 -->|0.029| C3[Jackson简单]
    C3 -->|0.101| D3[Jackson复杂]
    D3 -->|0.149| E3[Gson简单]
    E3 -->|0.010| F3[Gson复杂]
    F3 -->|0.094| G3[结束]
    
    classDef stable fill:#d4edda,stroke:#28a745,stroke-width:2px;
    classDef unstable fill:#f8d7da,stroke:#dc3545,stroke-width:2px;
    
    class A3,B3,E3,F3 stable;
    class C3,D3 unstable;
    end
```

## 7. 场景适用性分析

```mermaid
graph TB
    subgraph 应用场景推荐
    A4[高性能要求] -->|最佳选择| B4[JsonGeekAI Wasm]
    C4[普通应用] -->|推荐| D4[FastJSON2]
    E4[简单应用] -->|适合| F4[Gson]
    G4[大文件处理] -->|优选| H4[JsonGeekAI零拷贝]
    I4[内存受限] -->|首选| J4[JsonGeekAI字符串池]
    end
```

注：以上图表使用Mermaid语法生成，需要在支持Mermaid的Markdown查看器中查看。
