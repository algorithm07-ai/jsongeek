from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="jsongeek",
    version="0.1.0",
    author="Hongping",
    author_email="hongping1963@example.com",
    description="High-performance JSON parser using WebAssembly SIMD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hongping1963/jsongeek",
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
    ],
    extras_require={
        'dev': [
            'pytest>=6.0',
            'pytest-benchmark>=3.4.1',
            'black>=22.3.0',
            'isort>=5.10.1',
            'mypy>=0.950',
        ],
    }
)
