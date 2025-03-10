import { JSONType, TokenType, ParseResult, ErrorCode } from './types';

// SIMD constants for JSON parsing
const QUOTE: v128 = v128.splat<u8>(0x22);  // '"'
const ESCAPE: v128 = v128.splat<u8>(0x5C); // '\'
const SPACE: v128 = v128.splat<u8>(0x20);  // ' '
const DIGIT_0: v128 = v128.splat<u8>(0x30); // '0'
const DIGIT_9: v128 = v128.splat<u8>(0x39); // '9'

@external("env", "memory")
declare const memory: ArrayBuffer;

// Fast SIMD-based string scanning
function findQuoteSimd(start: i32, end: i32): i32 {
  let ptr = start;
  const step = 16; // v128 is 16 bytes

  // Process 16 bytes at a time using SIMD
  while (ptr + step <= end) {
    const block = v128.load(ptr);
    const quotes = v128.eq<u8>(block, QUOTE);
    const escapes = v128.eq<u8>(block, ESCAPE);
    
    // Check for unescaped quotes
    const mask = v128.and(quotes, v128.not(escapes));
    const matches = v128.bitmask<i32>(mask);
    
    if (matches != 0) {
      // Found a quote, find its exact position
      for (let i = 0; i < step; i++) {
        if (load<u8>(ptr + i) == 0x22 && (i == 0 || load<u8>(ptr + i - 1) != 0x5C)) {
          return ptr + i;
        }
      }
    }
    ptr += step;
  }

  // Handle remaining bytes
  while (ptr < end) {
    if (load<u8>(ptr) == 0x22 && (ptr == start || load<u8>(ptr - 1) != 0x5C)) {
      return ptr;
    }
    ptr++;
  }

  return -1;
}

// SIMD-optimized number parsing
function parseNumberSimd(start: i32, end: i32): f64 {
  let ptr = start;
  let sign: f64 = 1.0;
  let result: f64 = 0.0;
  let decimal: f64 = 0.0;
  let decimalPlaces: i32 = 0;
  let exponent: i32 = 0;
  let hasExponent: bool = false;

  // Handle sign
  if (load<u8>(ptr) == 0x2D) { // '-'
    sign = -1.0;
    ptr++;
  }

  // Use SIMD to process digits in chunks
  const step = 16;
  while (ptr + step <= end) {
    const block = v128.load(ptr);
    const digits = v128.sub<u8>(block, DIGIT_0);
    const valid = v128.and(
      v128.ge<u8>(digits, v128.splat<u8>(0)),
      v128.le<u8>(digits, v128.splat<u8>(9))
    );
    
    const validMask = v128.bitmask<i32>(valid);
    if (validMask == 0) break;

    // Process valid digits
    let breakLoop = false;
    for (let i = 0; i < step; i++) {
      if (validMask & (1 << i)) {
        const digit = load<u8>(ptr + i) - 0x30;
        if (decimal == 0.0) {
          result = result * 10.0 + f64(digit);
        } else {
          decimal = decimal * 10.0 + f64(digit);
          decimalPlaces++;
        }
      } else {
        ptr += i;
        breakLoop = true;
        break;
      }
    }
    if (breakLoop) break;
    ptr += step;
  }

  // Handle remaining digits and special cases
  while (ptr < end) {
    const c = load<u8>(ptr);
    if (c >= 0x30 && c <= 0x39) {
      const digit = c - 0x30;
      if (decimal == 0.0) {
        result = result * 10.0 + f64(digit);
      } else {
        decimal = decimal * 10.0 + f64(digit);
        decimalPlaces++;
      }
    } else if (c == 0x2E && !hasExponent) { // '.'
      decimal = 0.0;
    } else if ((c == 0x45 || c == 0x65) && !hasExponent) { // 'E' or 'e'
      hasExponent = true;
      ptr++;
      let expSign: i32 = 1;
      if (ptr < end) {
        if (load<u8>(ptr) == 0x2D) { // '-'
          expSign = -1;
          ptr++;
        } else if (load<u8>(ptr) == 0x2B) { // '+'
          ptr++;
        }
      }
      while (ptr < end) {
        const c = load<u8>(ptr);
        if (c >= 0x30 && c <= 0x39) {
          exponent = exponent * 10 + (c - 0x30);
        } else {
          break;
        }
        ptr++;
      }
      exponent *= expSign;
      break;
    } else {
      break;
    }
    ptr++;
  }

  // Combine integer and decimal parts
  let value = result;
  if (decimal > 0.0) {
    value += decimal / Math.pow(10.0, f64(decimalPlaces));
  }
  if (exponent != 0) {
    value *= Math.pow(10.0, f64(exponent));
  }
  return sign * value;
}

// Main parse function
export function parse(input: string): ParseResult {
  const length = input.length;
  let pos = 0;

  // Skip whitespace
  while (pos < length && (input.charCodeAt(pos) <= 0x20 || input.charCodeAt(pos) == 0x2C)) {
    pos++;
  }

  if (pos >= length) {
    return new ParseResult(JSONType.NULL, 0, 0, ErrorCode.UNEXPECTED_EOF);
  }

  const result = parseValue(input, pos, length);
  if (result.error != ErrorCode.NONE) {
    return result;
  }

  // Skip trailing whitespace
  pos = result.end;
  while (pos < length && (input.charCodeAt(pos) <= 0x20 || input.charCodeAt(pos) == 0x2C)) {
    pos++;
  }

  if (pos < length) {
    return new ParseResult(JSONType.NULL, 0, 0, ErrorCode.INVALID_TOKEN);
  }

  return result;
}

function parseValue(input: string, start: i32, end: i32): ParseResult {
  if (start >= end) {
    return new ParseResult(JSONType.NULL, start, start, ErrorCode.UNEXPECTED_EOF);
  }

  const c = input.charCodeAt(start);
  switch (c) {
    case 0x22: // '"'
      return parseString(input, start, end);
    case 0x7B: // '{'
      return new ParseResult(JSONType.OBJECT, start, start + 1, ErrorCode.NONE); // TODO: Implement object parsing
    case 0x5B: // '['
      return new ParseResult(JSONType.ARRAY, start, start + 1, ErrorCode.NONE);  // TODO: Implement array parsing
    case 0x74: // 't'
      return parseTrue(input, start, end);
    case 0x66: // 'f'
      return parseFalse(input, start, end);
    case 0x6E: // 'n'
      return parseNull(input, start, end);
    case 0x2D: // '-'
    case 0x30: // '0'
    case 0x31: // '1'
    case 0x32: // '2'
    case 0x33: // '3'
    case 0x34: // '4'
    case 0x35: // '5'
    case 0x36: // '6'
    case 0x37: // '7'
    case 0x38: // '8'
    case 0x39: // '9'
      return parseNumber(input, start, end);
    default:
      return new ParseResult(JSONType.NULL, start, start, ErrorCode.INVALID_TOKEN);
  }
}

// Helper functions for parsing specific types
function parseString(input: string, start: i32, end: i32): ParseResult {
  const quoteEnd = findQuoteSimd(start + 1, end);
  if (quoteEnd == -1) {
    return new ParseResult(JSONType.NULL, start, start, ErrorCode.INVALID_STRING);
  }
  return new ParseResult(JSONType.STRING, start, quoteEnd + 1, ErrorCode.NONE);
}

function parseNumber(input: string, start: i32, end: i32): ParseResult {
  const value = parseNumberSimd(start, end);
  if (isNaN(value)) {
    return new ParseResult(JSONType.NULL, start, start, ErrorCode.INVALID_NUMBER);
  }
  let pos = start;
  while (pos < end && isNumberChar(input.charCodeAt(pos))) {
    pos++;
  }
  return new ParseResult(JSONType.NUMBER, start, pos, ErrorCode.NONE);
}

function parseTrue(input: string, start: i32, end: i32): ParseResult {
  if (start + 4 > end || 
      input.charCodeAt(start + 1) != 0x72 || // 'r'
      input.charCodeAt(start + 2) != 0x75 || // 'u'
      input.charCodeAt(start + 3) != 0x65) { // 'e'
    return new ParseResult(JSONType.NULL, start, start, ErrorCode.INVALID_TOKEN);
  }
  return new ParseResult(JSONType.BOOLEAN, start, start + 4, ErrorCode.NONE);
}

function parseFalse(input: string, start: i32, end: i32): ParseResult {
  if (start + 5 > end ||
      input.charCodeAt(start + 1) != 0x61 || // 'a'
      input.charCodeAt(start + 2) != 0x6C || // 'l'
      input.charCodeAt(start + 3) != 0x73 || // 's'
      input.charCodeAt(start + 4) != 0x65) { // 'e'
    return new ParseResult(JSONType.NULL, start, start, ErrorCode.INVALID_TOKEN);
  }
  return new ParseResult(JSONType.BOOLEAN, start, start + 5, ErrorCode.NONE);
}

function parseNull(input: string, start: i32, end: i32): ParseResult {
  if (start + 4 > end ||
      input.charCodeAt(start + 1) != 0x75 || // 'u'
      input.charCodeAt(start + 2) != 0x6C || // 'l'
      input.charCodeAt(start + 3) != 0x6C) { // 'l'
    return new ParseResult(JSONType.NULL, start, start, ErrorCode.INVALID_TOKEN);
  }
  return new ParseResult(JSONType.NULL, start, start + 4, ErrorCode.NONE);
}

// Helper function for number parsing
function isNumberChar(c: i32): bool {
  return (
    (c >= 0x30 && c <= 0x39) || // 0-9
    c == 0x2E || // .
    c == 0x2D || // -
    c == 0x2B || // +
    c == 0x45 || // E
    c == 0x65    // e
  );
}

// Export functions
export function malloc(size: i32): i32 {
  return heap.alloc(size) as i32;
}

export function free(ptr: i32): void {
  heap.free(ptr);
}
