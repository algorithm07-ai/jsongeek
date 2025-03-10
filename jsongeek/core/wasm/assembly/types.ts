// JSON value types
export enum JSONType {
  NULL,
  BOOLEAN,
  NUMBER,
  STRING,
  ARRAY,
  OBJECT
}

// Token types for lexer
export enum TokenType {
  EOF = 0,
  NULL = 1,
  BOOLEAN = 2,
  NUMBER = 3,
  STRING = 4,
  ARRAY_START = 5,
  ARRAY_END = 6,
  OBJECT_START = 7,
  OBJECT_END = 8,
  COMMA = 9,
  COLON = 10,
  ERROR = 11
}

// Result structure for parser
@unmanaged
export class ParseResult {
  constructor(
    public type: JSONType,
    public start: i32,
    public end: i32,
    public error: ErrorCode
  ) {}
}

// Error codes
export enum ErrorCode {
  NONE,
  UNEXPECTED_EOF,
  INVALID_TOKEN,
  UNTERMINATED_STRING,
  INVALID_STRING,
  INVALID_NUMBER,
  INVALID_ARRAY,
  INVALID_OBJECT
}
