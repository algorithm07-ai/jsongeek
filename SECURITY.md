# Security Policy

## Supported Versions

| Version | Supported          | P0 Tests | P1 Tests | P2 Tests |
|---------|-------------------|-----------|-----------|-----------|
| 0.1.1   | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| 0.1.0   | :x:               | :white_check_mark: | :white_check_mark: | :x: |

## Security Testing

JsonGeekAI follows a strict P0-P1-P2 testing classification:

### P0 (Critical) Tests
- JSONTestSuite: 语法和边界测试
- Memory safety checks
- Input validation
- WebAssembly sandbox integrity

### P1 (Standard) Tests
- JSON Schema Test Suite: 结构和语义验证
- RFC 8259 / ECMA-404: 标准合规性测试
- UTF-8 validation
- API security checks

### P2 (Extended) Tests
- RFC 8259 Test Cases: 标准合规性扩展测试
- ECMA-404 Test Cases: 数据格式验证测试
- Performance boundary tests
- Edge case handling

## Reporting a Vulnerability

We take security seriously at JsonGeekAI. Please follow these steps to report a vulnerability:

1. **DO NOT** create a public GitHub issue for security vulnerabilities
2. Email your findings to security@jsongeek.ai
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

## Security Features

JsonGeekAI implements several security measures:

### Memory Safety
- WebAssembly sandbox isolation
- Strict memory bounds checking
- Automatic memory management

### Input Validation
- UTF-8 validation
- Schema validation
- Depth limit enforcement
- Size restrictions

### Java API Security
- Type safety checks
- Memory isolation
- Exception handling
- Resource cleanup

### SIMD Safety
- Hardware capability detection
- Fallback mechanisms
- Boundary checks

## Response Timeline

We aim to respond to security reports within these timeframes:

- **Initial Response**: 24 hours
- **Vulnerability Confirmation**: 72 hours
- **Fix Timeline Communication**: 1 week
- **Fix Implementation**: Based on severity
  - Critical (P0): 1-2 weeks
  - High (P1): 2-4 weeks
  - Moderate (P2): Next release cycle

## Secure Development

Our security practices include:

1. Regular security audits
2. Automated testing
3. Code review requirements
4. Dependency scanning
5. Static analysis

## Contact

- Security Email: security@jsongeek.ai
- PGP Key: [security-key.asc](https://jsongeek.ai/security-key.asc)
- Security Advisory: [https://github.com/algorithm07-ai/jsongeek/security](https://github.com/algorithm07-ai/jsongeek/security)
