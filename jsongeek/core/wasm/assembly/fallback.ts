import { JSONType, ParseResult, ErrorCode } from './types';

// Memory management
let heap: ArrayBuffer | null = null;
let dataView: DataView | null = null;

// Helper functions
function isWhitespace(c: u8): bool {
  return c <= 0x20 || c == 0x2C;
}

function isDigit(c: u8): bool {
  return c >= 0x30 && c <= 0x39;
}

function parseNumber(bytes: Uint8Array, start: i32, end: i32): ParseResult {
  let pos = start;
  let isNegative = false;
  let hasDecimal = false;
  let value = 0;

  // Handle sign
  if (bytes[pos] == 0x2D) { // -
    isNegative = true;
    pos++;
  } else if (bytes[pos] == 0x2B) { // +
    pos++;
  }

  // Parse digits
  while (pos < end && isDigit(bytes[pos])) {
    value = value * 10 + (bytes[pos] - 0x30);
    pos++;
  }

  if (isNegative) {
    value = -value;
  }

  return new ParseResult(JSONType.NUMBER, start, pos, ErrorCode.NONE);
}

function parseString(bytes: Uint8Array, start: i32, end: i32): ParseResult {
  let pos = start + 1; // Skip opening quote
  
  while (pos < end && bytes[pos] != 0x22) { // "
    if (bytes[pos] == 0x5C) { // \
      pos++; // Skip escape character
    }
    pos++;
  }
  
  if (pos >= end || bytes[pos] != 0x22) {
    return new ParseResult(JSONType.NULL, start, pos, ErrorCode.INVALID_STRING);
  }
  
  return new ParseResult(JSONType.STRING, start, pos + 1, ErrorCode.NONE);
}

function parseTrue(bytes: Uint8Array, start: i32, end: i32): ParseResult {
  if (end - start < 4 ||
      bytes[start] != 0x74 || // t
      bytes[start + 1] != 0x72 || // r
      bytes[start + 2] != 0x75 || // u
      bytes[start + 3] != 0x65) { // e
    return new ParseResult(JSONType.NULL, start, start, ErrorCode.INVALID_TOKEN);
  }
  return new ParseResult(JSONType.BOOLEAN, start, start + 4, ErrorCode.NONE);
}

function parseFalse(bytes: Uint8Array, start: i32, end: i32): ParseResult {
  if (end - start < 5 ||
      bytes[start] != 0x66 || // f
      bytes[start + 1] != 0x61 || // a
      bytes[start + 2] != 0x6C || // l
      bytes[start + 3] != 0x73 || // s
      bytes[start + 4] != 0x65) { // e
    return new ParseResult(JSONType.NULL, start, start, ErrorCode.INVALID_TOKEN);
  }
  return new ParseResult(JSONType.BOOLEAN, start, start + 5, ErrorCode.NONE);
}

function parseNull(bytes: Uint8Array, start: i32, end: i32): ParseResult {
  if (end - start < 4 ||
      bytes[start] != 0x6E || // n
      bytes[start + 1] != 0x75 || // u
      bytes[start + 2] != 0x6C || // l
      bytes[start + 3] != 0x6C) { // l
    return new ParseResult(JSONType.NULL, start, start, ErrorCode.INVALID_TOKEN);
  }
  return new ParseResult(JSONType.NULL, start, start + 4, ErrorCode.NONE);
}

function parseValue(bytes: Uint8Array, start: i32, end: i32): ParseResult {
  if (start >= end) {
    return new ParseResult(JSONType.NULL, start, start, ErrorCode.UNEXPECTED_EOF);
  }

  const c = bytes[start];
  
  // Skip whitespace
  if (isWhitespace(c)) {
    let pos = start;
    while (pos < end && isWhitespace(bytes[pos])) {
      pos++;
    }
    if (pos >= end) {
      return new ParseResult(JSONType.NULL, start, pos, ErrorCode.UNEXPECTED_EOF);
    }
    return parseValue(bytes, pos, end);
  }

  // Parse based on first character
  switch (c) {
    case 0x22: // "
      return parseString(bytes, start, end);
    case 0x74: // t
      return parseTrue(bytes, start, end);
    case 0x66: // f
      return parseFalse(bytes, start, end);
    case 0x6E: // n
      return parseNull(bytes, start, end);
    case 0x2D: // -
    case 0x30: // 0
    case 0x31: // 1
    case 0x32: // 2
    case 0x33: // 3
    case 0x34: // 4
    case 0x35: // 5
    case 0x36: // 6
    case 0x37: // 7
    case 0x38: // 8
    case 0x39: // 9
      return parseNumber(bytes, start, end);
    default:
      return new ParseResult(JSONType.NULL, start, start, ErrorCode.INVALID_TOKEN);
  }
}

// Export functions
export function malloc(size: i32): i32 {
  const buffer = new ArrayBuffer(size);
  heap = buffer;
  dataView = new DataView(buffer);
  return changetype<i32>(buffer);
}

export function free(ptr: i32): void {
  heap = null;
  dataView = null;
}

export function parse(input: Uint8Array): ParseResult {
  const length = input.length;
  let pos = 0;

  // Skip whitespace
  while (pos < length && isWhitespace(input[pos])) {
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
  while (pos < length && isWhitespace(input[pos])) {
    pos++;
  }

  if (pos < length) {
    return new ParseResult(JSONType.NULL, 0, 0, ErrorCode.INVALID_TOKEN);
  }

  return result;
}
