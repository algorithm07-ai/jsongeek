from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="jsongeekai",  # 修改为PyPI包名
    version="0.1.0",
    author="Hongping",
    author_email="hongping1963@example.com",
    description="High-performance JSON parser with SIMD optimization and AI features",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/algorithm07-ai/jsongeek",  # 更新为新的GitHub地址
    packages=find_packages(),
    package_data={
        'jsongeek': ['core/wasm/*.wasm'],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: WebAssembly",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "wasmer>=1.1.0",
        "wasmer-compiler-cranelift>=1.1.0",
        "numpy>=1.20.0",  # 添加SIMD优化依赖
    ],
    extras_require={
        'dev': [
            'pytest>=6.0',
            'pytest-benchmark>=3.4.1',
            'black>=22.3.0',
            'isort>=5.10.1',
            'mypy>=0.950',
        ],
        'ai': [  # 添加AI特性的额外依赖
            'tensorflow>=2.8.0',
            'torch>=1.10.0',
        ]
    }
)
