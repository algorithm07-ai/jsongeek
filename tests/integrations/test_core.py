"""
Test core integration components
"""
import os
import json
import asyncio
import pytest
import numpy as np
from jsongeekai.integrations.wasm.worker_pool import WasmWorkerPool
from jsongeekai.integrations.json.stream_reader import (
    JsonStreamReader,
    JsonArrayReader
)
from jsongeekai.integrations.json.optimized_reader import (
    OptimizedReader,
    ParallelProcessor
)

@pytest.fixture
def sample_json_file(tmp_path):
    """创建示例 JSON 文件"""
    data = [
        {
            "id": i,
            "name": f"item_{i}",
            "value": np.random.rand(),
            "nested": {
                "a": 1,
                "b": "test",
                "c": [1, 2, 3]
            }
        }
        for i in range(1000)
    ]
    
    file_path = tmp_path / "test.json"
    with open(file_path, 'w') as f:
        json.dump(data, f)
    
    return str(file_path)

@pytest.mark.asyncio
async def test_wasm_worker_pool():
    """测试 WebAssembly 工作线程池"""
    pool = WasmWorkerPool(workers=2)
    
    # 测试简单的 JSON 解析
    data = b'{"test": 123}'
    result = await pool.parse(data)
    assert result == {"test": 123}
    
    # 测试并行解析
    data_list = [
        b'{"id": 1}',
        b'{"id": 2}',
        b'{"id": 3}'
    ]
    
    results = await asyncio.gather(*[
        pool.parse(d) for d in data_list
    ])
    
    assert len(results) == 3
    assert all(r["id"] == i + 1 for i, r in enumerate(results))
    
    pool.stop()

def test_json_stream_reader(sample_json_file):
    """测试 JSON 流式读取器"""
    # 测试基本读取
    with JsonStreamReader(sample_json_file) as reader:
        objects = list(reader.read_objects())
        assert len(objects) == 1000
        assert all(isinstance(obj, dict) for obj in objects)
    
    # 测试数组读取
    with JsonArrayReader(sample_json_file) as reader:
        items = list(reader.read_array_items())
        assert len(items) == 1000
        assert all(isinstance(item, dict) for item in items)

@pytest.mark.asyncio
async def test_optimized_reader(sample_json_file):
    """测试内存优化的读取器"""
    # 测试原生模式
    reader = OptimizedReader(
        sample_json_file,
        memory_limit_mb=100,
        use_wasm=False
    )
    results = await reader.read()
    assert len(results) == 1000
    
    # 测试 WebAssembly 模式
    reader = OptimizedReader(
        sample_json_file,
        memory_limit_mb=100,
        use_wasm=True
    )
    results = await reader.read()
    assert len(results) == 1000

def test_parallel_processor():
    """测试并行处理器"""
    # 准备测试数据
    data = [
        json.dumps({"id": i, "value": i * 2})
        for i in range(1000)
    ]
    
    # 测试原生模式
    with ParallelProcessor(use_wasm=False) as processor:
        results = processor.process_batch(data)
        assert len(results) == 1000
        assert all(r["value"] == r["id"] * 2 for r in results)
    
    # 测试带回调的处理
    def callback(obj):
        obj["processed"] = True
        return obj
    
    with ParallelProcessor(use_wasm=False) as processor:
        results = processor.process_batch(data, callback)
        assert len(results) == 1000
        assert all(r["processed"] for r in results)

@pytest.mark.benchmark
def test_performance(sample_json_file, benchmark):
    """性能基准测试"""
    def read_with_native():
        with open(sample_json_file) as f:
            return json.load(f)
    
    def read_with_optimized():
        reader = OptimizedReader(sample_json_file, use_wasm=True)
        return asyncio.run(reader.read())
    
    # 原生 JSON 解析
    native_result = benchmark(read_with_native)
    assert len(native_result) == 1000
    
    # 优化的解析
    optimized_result = benchmark(read_with_optimized)
    assert len(optimized_result) == 1000
