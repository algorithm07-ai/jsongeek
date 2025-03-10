# JsonGeekAI 性能基准测试设置指南

## 1. 环境准备

### 1.1 Java JDK 安装
1. 下载 JDK：
   - 访问：https://www.oracle.com/java/technologies/downloads/#jdk17-windows
   - 下载 JDK 17 Windows x64 Installer
   - 运行安装程序，按照提示完成安装

2. 配置环境变量：
   - 右键"此电脑" -> 属性 -> 高级系统设置 -> 环境变量
   - 新建系统变量 JAVA_HOME：`C:\Program Files\Java\jdk-17`
   - 编辑系统变量 Path，添加：`%JAVA_HOME%\bin`
   - 验证安装：打开命令提示符，运行 `java -version`

### 1.2 Maven 安装
1. 下载 Maven：
   - 访问：https://maven.apache.org/download.cgi
   - 下载最新的 Binary zip archive
   - 解压到合适目录（如：`C:\Program Files\Apache\maven`）

2. 配置环境变量：
   - 新建系统变量 MAVEN_HOME：`C:\Program Files\Apache\maven`
   - 编辑系统变量 Path，添加：`%MAVEN_HOME%\bin`
   - 验证安装：打开命令提示符，运行 `mvn -version`

## 2. 项目结构
```
jsongeek/benchmark/
├── pom.xml                                 # Maven 配置文件
├── src/
│   └── main/
│       └── java/
│           └── com/
│               └── jsongeek/
│                   ├── JsonGeekAI.java     # 核心实现
│                   └── benchmark/
│                       ├── model/
│                       │   └── Order.java   # 测试模型
│                       └── JsonBenchmark.java # 基准测试类
└── docs/
    └── benchmark_setup.md                  # 本文档
```

## 3. 基准测试内容

### 3.1 测试场景
1. 序列化测试：
   - 小型对象（5个订单项）
   - 中型对象（50个订单项）
   - 大型对象（500个订单项）

2. 反序列化测试：
   - 小型JSON
   - 中型JSON
   - 大型JSON

### 3.2 对比库
- FastJson2
- Jackson
- Gson
- JsonGeekAI

### 3.3 测试配置
- 预热：3轮
- 测量：8轮
- Fork：2次（每次测试运行2个独立的JVM）
- 堆内存：2GB
- 测量模式：平均时间
- 时间单位：微秒

## 4. 运行测试

### 4.1 编译项目
```bash
cd jsongeek/benchmark
mvn clean package
```

### 4.2 运行基准测试
```bash
java -jar target/benchmarks.jar
```

### 4.3 查看结果
测试完成后，将生成详细的性能报告，包括：
- 每个测试场景的平均执行时间
- 标准偏差
- 置信区间
- GC信息

## 5. JsonGeekAI 优化特性

### 5.1 性能优化
- 自定义 FastStringBuilder
- 类型缓存
- 字符串池化
- 直接字符操作

### 5.2 内存优化
- 预分配缓冲区
- 对象重用
- 延迟加载
- 字段缓存

### 5.3 功能特性
- 支持所有基本类型
- 支持复杂对象
- 支持集合和数组
- 支持日期类型
- 支持嵌套对象

## 6. 注意事项

### 6.1 测试环境要求
- 确保测试机器负载较低
- 关闭不必要的后台程序
- 保持稳定的系统温度
- 使用性能模式的电源计划

### 6.2 测试建议
- 每次测试前重启JVM
- 多次运行测试以获得稳定结果
- 记录测试环境信息
- 保存详细的测试日志

## 7. 结果分析

### 7.1 性能指标
- 吞吐量（ops/s）
- 平均响应时间
- 95/99百分位延迟
- GC开销

### 7.2 对比维度
- 序列化性能
- 反序列化性能
- 内存使用
- CPU使用率
- GC压力

## 8. 后续优化方向
1. SIMD 优化
2. 内存池优化
3. 并行处理优化
4. 缓存优化
5. 编码优化
