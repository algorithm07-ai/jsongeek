"""
SIMD support detection for WebAssembly
"""
from wasmer import Store, Module, ImportObject
import os

def has_simd_support() -> bool:
    """
    Check if the current environment supports WebAssembly SIMD
    
    Returns:
        bool: True if SIMD is supported, False otherwise
    """
    try:
        store = Store()
        # Simple WASM module with SIMD instructions
        wasm_bytes = (
            b'\x00\x61\x73\x6D\x01\x00\x00\x00'  # magic + version
            b'\x01\x05\x01\x60\x00\x01\x7B'      # type section
            b'\x03\x02\x01\x00'                  # func section
            b'\x07\x07\x01\x03\x73\x69\x6D\x64\x00\x00'  # export section
            b'\x0A\x09\x01\x07\x00\xFD\x0C\x00\x00\x00\x0B'  # code section with v128.const
        )
        
        Module(store, wasm_bytes)
        return True
    except Exception:
        return False
