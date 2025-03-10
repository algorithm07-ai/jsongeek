"""
Test configuration for JSONGeek
Defines test categories and requirements according to P0-P2 classification
"""

# P0 Tests (Mandatory) - Must pass for every commit
P0_REQUIREMENTS = {
    'syntax': {
        'description': 'Core syntax and boundary tests',
        'pass_threshold': 1.0  # 100% pass required
    },
    'simd': {
        'description': 'SIMD optimization verification',
        'performance_threshold': 1.5  # Minimum 1.5x speedup required
    },
    'memory': {
        'description': 'Memory usage benchmarks',
        'max_memory_mb': 100
    }
}

# P1 Tests (Regular) - Run during development cycle
P1_REQUIREMENTS = {
    'structure': {
        'description': 'Structure and semantic validation',
        'pass_threshold': 0.95  # 95% pass required
    },
    'api': {
        'description': 'API compatibility tests',
        'response_time_ms': 200  # Maximum response time
    },
    'performance': {
        'description': 'Performance regression tests',
        'regression_threshold': 0.1  # Max 10% performance regression
    }
}

# P2 Tests (Optional) - Extended test suite
P2_REQUIREMENTS = {
    'edge_cases': {
        'description': 'Edge case scenarios',
        'coverage_threshold': 0.8  # 80% coverage target
    },
    'stress': {
        'description': 'Stress testing',
        'duration_minutes': 60
    },
    'integration': {
        'description': 'Integration tests',
        'service_coverage': 0.7  # 70% service coverage
    }
}

# SIMD Optimization Requirements
SIMD_CONFIG = {
    'min_data_size': 1000,  # Minimum data size for SIMD optimization
    'target_speedup': 1.5,  # Target speedup factor
    'memory_efficiency': 0.8  # Target memory efficiency score
}

# Smart Compression Features
COMPRESSION_CONFIG = {
    'min_ratio': 0.5,  # Minimum compression ratio
    'max_ratio': 0.8,  # Maximum compression ratio
    'lossless_required': True  # Require lossless compression
}
