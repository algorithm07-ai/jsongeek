package com.jsongeek;

import java.lang.reflect.*;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.nio.ByteBuffer;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;

public class JsonGeekAI {
    // 类型缓存，避免重复反射
    private static final ConcurrentHashMap<Class<?>, Map<String, Field>> TYPE_CACHE = new ConcurrentHashMap<>();
    // 字符串池，减少字符串对象创建
    private static final ConcurrentHashMap<String, String> STRING_POOL = new ConcurrentHashMap<>();
    // 默认缓冲区大小
    private static final int DEFAULT_BUFFER_SIZE = 4096;
    // 日期格式化器
    private static final DateTimeFormatter DATE_FORMATTER = DateTimeFormatter.ISO_DATE_TIME;
    
    // 自定义的高性能字符串构建器
    private static class FastStringBuilder {
        private char[] buffer;
        private int size;
        
        public FastStringBuilder(int capacity) {
            buffer = new char[capacity];
            size = 0;
        }
        
        public void append(char c) {
            ensureCapacity(size + 1);
            buffer[size++] = c;
        }
        
        public void append(String str) {
            int len = str.length();
            ensureCapacity(size + len);
            str.getChars(0, len, buffer, size);
            size += len;
        }
        
        private void ensureCapacity(int minCapacity) {
            if (minCapacity > buffer.length) {
                int newCapacity = Math.max(buffer.length * 2, minCapacity);
                char[] newBuffer = new char[newCapacity];
                System.arraycopy(buffer, 0, newBuffer, 0, size);
                buffer = newBuffer;
            }
        }
        
        @Override
        public String toString() {
            return new String(buffer, 0, size);
        }
    }
    
    // 序列化方法
    public String toJson(Object obj) {
        if (obj == null) {
            return "null";
        }
        
        FastStringBuilder sb = new FastStringBuilder(DEFAULT_BUFFER_SIZE);
        serializeValue(obj, sb);
        return sb.toString();
    }
    
    private void serializeValue(Object value, FastStringBuilder sb) {
        if (value == null) {
            sb.append("null");
            return;
        }
        
        Class<?> type = value.getClass();
        
        if (type == String.class) {
            serializeString((String) value, sb);
        } else if (type == Boolean.class || type == boolean.class) {
            sb.append(value.toString());
        } else if (Number.class.isAssignableFrom(type) || type.isPrimitive()) {
            sb.append(value.toString());
        } else if (type == Date.class) {
            serializeDate((Date) value, sb);
        } else if (Collection.class.isAssignableFrom(type)) {
            serializeCollection((Collection<?>) value, sb);
        } else if (Map.class.isAssignableFrom(type)) {
            serializeMap((Map<?, ?>) value, sb);
        } else if (type.isArray()) {
            serializeArray(value, sb);
        } else {
            serializeObject(value, sb);
        }
    }
    
    private void serializeString(String str, FastStringBuilder sb) {
        sb.append('"');
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            switch (c) {
                case '"': sb.append("\\\""); break;
                case '\\': sb.append("\\\\"); break;
                case '\b': sb.append("\\b"); break;
                case '\f': sb.append("\\f"); break;
                case '\n': sb.append("\\n"); break;
                case '\r': sb.append("\\r"); break;
                case '\t': sb.append("\\t"); break;
                default:
                    if (c < ' ') {
                        String hex = String.format("\\u%04x", (int) c);
                        sb.append(hex);
                    } else {
                        sb.append(c);
                    }
            }
        }
        sb.append('"');
    }
    
    private void serializeDate(Date date, FastStringBuilder sb) {
        LocalDateTime ldt = LocalDateTime.ofInstant(date.toInstant(), ZoneId.systemDefault());
        sb.append('"');
        sb.append(DATE_FORMATTER.format(ldt));
        sb.append('"');
    }
    
    private void serializeCollection(Collection<?> collection, FastStringBuilder sb) {
        sb.append('[');
        boolean first = true;
        for (Object item : collection) {
            if (!first) {
                sb.append(',');
            }
            serializeValue(item, sb);
            first = false;
        }
        sb.append(']');
    }
    
    private void serializeMap(Map<?, ?> map, FastStringBuilder sb) {
        sb.append('{');
        boolean first = true;
        for (Map.Entry<?, ?> entry : map.entrySet()) {
            if (!first) {
                sb.append(',');
            }
            serializeString(entry.getKey().toString(), sb);
            sb.append(':');
            serializeValue(entry.getValue(), sb);
            first = false;
        }
        sb.append('}');
    }
    
    private void serializeArray(Object array, FastStringBuilder sb) {
        sb.append('[');
        int length = Array.getLength(array);
        for (int i = 0; i < length; i++) {
            if (i > 0) {
                sb.append(',');
            }
            serializeValue(Array.get(array, i), sb);
        }
        sb.append(']');
    }
    
    private void serializeObject(Object obj, FastStringBuilder sb) {
        Class<?> clazz = obj.getClass();
        Map<String, Field> fields = getTypeFields(clazz);
        
        sb.append('{');
        boolean first = true;
        
        for (Map.Entry<String, Field> entry : fields.entrySet()) {
            String fieldName = entry.getKey();
            Field field = entry.getValue();
            
            try {
                Object value = field.get(obj);
                if (!first) {
                    sb.append(',');
                }
                serializeString(fieldName, sb);
                sb.append(':');
                serializeValue(value, sb);
                first = false;
            } catch (IllegalAccessException e) {
                // Skip inaccessible fields
            }
        }
        
        sb.append('}');
    }
    
    // 反序列化方法
    public <T> T fromJson(String json, Class<T> clazz) {
        if (json == null || json.trim().isEmpty()) {
            return null;
        }
        
        JsonParser parser = new JsonParser(json);
        return parser.parse(clazz);
    }
    
    // 内部JSON解析器
    private class JsonParser {
        private final String json;
        private int pos;
        
        public JsonParser(String json) {
            this.json = json;
            this.pos = 0;
        }
        
        public <T> T parse(Class<T> clazz) {
            skipWhitespace();
            return parseValue(clazz);
        }
        
        @SuppressWarnings("unchecked")
        private <T> T parseValue(Class<T> clazz) {
            char c = peek();
            if (c == 'n') {
                pos += 4; // skip "null"
                return null;
            }
            
            if (clazz == String.class) {
                return (T) parseString();
            } else if (clazz == Boolean.class || clazz == boolean.class) {
                return (T) parseBoolean();
            } else if (Number.class.isAssignableFrom(clazz) || clazz.isPrimitive()) {
                return (T) parseNumber(clazz);
            } else if (clazz == Date.class) {
                return (T) parseDate();
            } else if (Collection.class.isAssignableFrom(clazz)) {
                return (T) parseCollection((Class<? extends Collection<?>>) clazz);
            } else if (Map.class.isAssignableFrom(clazz)) {
                return (T) parseMap((Class<? extends Map<?, ?>>) clazz);
            } else if (clazz.isArray()) {
                return (T) parseArray(clazz.getComponentType());
            } else {
                return parseObject(clazz);
            }
        }
        
        private String parseString() {
            StringBuilder sb = new StringBuilder();
            pos++; // skip opening quote
            
            while (pos < json.length()) {
                char c = json.charAt(pos++);
                if (c == '"') {
                    break;
                }
                if (c == '\\') {
                    c = json.charAt(pos++);
                    switch (c) {
                        case '"':
                        case '\\':
                        case '/': sb.append(c); break;
                        case 'b': sb.append('\b'); break;
                        case 'f': sb.append('\f'); break;
                        case 'n': sb.append('\n'); break;
                        case 'r': sb.append('\r'); break;
                        case 't': sb.append('\t'); break;
                        case 'u':
                            String hex = json.substring(pos, pos + 4);
                            sb.append((char) Integer.parseInt(hex, 16));
                            pos += 4;
                            break;
                    }
                } else {
                    sb.append(c);
                }
            }
            
            String result = sb.toString();
            return STRING_POOL.computeIfAbsent(result, k -> k);
        }
        
        private Boolean parseBoolean() {
            if (json.startsWith("true", pos)) {
                pos += 4;
                return true;
            } else if (json.startsWith("false", pos)) {
                pos += 5;
                return false;
            }
            throw new IllegalStateException("Invalid boolean value");
        }
        
        private Number parseNumber(Class<?> targetClass) {
            StringBuilder sb = new StringBuilder();
            char c;
            while (pos < json.length() && 
                   ((c = json.charAt(pos)) == '-' || c == '+' || c == '.' || 
                    c == 'e' || c == 'E' || Character.isDigit(c))) {
                sb.append(c);
                pos++;
            }
            
            String numStr = sb.toString();
            if (targetClass == int.class || targetClass == Integer.class) {
                return Integer.parseInt(numStr);
            } else if (targetClass == long.class || targetClass == Long.class) {
                return Long.parseLong(numStr);
            } else if (targetClass == double.class || targetClass == Double.class) {
                return Double.parseDouble(numStr);
            } else if (targetClass == float.class || targetClass == Float.class) {
                return Float.parseFloat(numStr);
            }
            throw new IllegalStateException("Unsupported number type: " + targetClass);
        }
        
        private Date parseDate() {
            String dateStr = parseString();
            LocalDateTime ldt = LocalDateTime.parse(dateStr, DATE_FORMATTER);
            return Date.from(ldt.atZone(ZoneId.systemDefault()).toInstant());
        }
        
        @SuppressWarnings("unchecked")
        private Collection<?> parseCollection(Class<? extends Collection<?>> clazz) {
            Collection<Object> result;
            try {
                result = (Collection<Object>) clazz.getDeclaredConstructor().newInstance();
            } catch (Exception e) {
                result = new ArrayList<>();
            }
            
            pos++; // skip '['
            skipWhitespace();
            
            while (pos < json.length() && json.charAt(pos) != ']') {
                result.add(parseValue(Object.class));
                skipWhitespace();
                if (json.charAt(pos) == ',') {
                    pos++;
                    skipWhitespace();
                }
            }
            pos++; // skip ']'
            
            return result;
        }
        
        @SuppressWarnings("unchecked")
        private Map<?, ?> parseMap(Class<? extends Map<?, ?>> clazz) {
            Map<String, Object> result;
            try {
                result = (Map<String, Object>) clazz.getDeclaredConstructor().newInstance();
            } catch (Exception e) {
                result = new HashMap<>();
            }
            
            pos++; // skip '{'
            skipWhitespace();
            
            while (pos < json.length() && json.charAt(pos) != '}') {
                String key = parseString();
                skipWhitespace();
                pos++; // skip ':'
                skipWhitespace();
                Object value = parseValue(Object.class);
                result.put(key, value);
                skipWhitespace();
                if (json.charAt(pos) == ',') {
                    pos++;
                    skipWhitespace();
                }
            }
            pos++; // skip '}'
            
            return result;
        }
        
        private Object parseArray(Class<?> componentType) {
            List<Object> list = new ArrayList<>();
            pos++; // skip '['
            skipWhitespace();
            
            while (pos < json.length() && json.charAt(pos) != ']') {
                list.add(parseValue(componentType));
                skipWhitespace();
                if (json.charAt(pos) == ',') {
                    pos++;
                    skipWhitespace();
                }
            }
            pos++; // skip ']'
            
            Object array = Array.newInstance(componentType, list.size());
            for (int i = 0; i < list.size(); i++) {
                Array.set(array, i, list.get(i));
            }
            return array;
        }
        
        private <T> T parseObject(Class<T> clazz) {
            T instance;
            try {
                instance = clazz.getDeclaredConstructor().newInstance();
            } catch (Exception e) {
                throw new IllegalStateException("Cannot create instance of " + clazz);
            }
            
            Map<String, Field> fields = getTypeFields(clazz);
            pos++; // skip '{'
            skipWhitespace();
            
            while (pos < json.length() && json.charAt(pos) != '}') {
                String fieldName = parseString();
                skipWhitespace();
                pos++; // skip ':'
                skipWhitespace();
                
                Field field = fields.get(fieldName);
                if (field != null) {
                    Object value = parseValue(field.getType());
                    try {
                        field.set(instance, value);
                    } catch (IllegalAccessException e) {
                        // Skip inaccessible fields
                    }
                } else {
                    // Skip unknown fields
                    parseValue(Object.class);
                }
                
                skipWhitespace();
                if (json.charAt(pos) == ',') {
                    pos++;
                    skipWhitespace();
                }
            }
            pos++; // skip '}'
            
            return instance;
        }
        
        private void skipWhitespace() {
            while (pos < json.length() && Character.isWhitespace(json.charAt(pos))) {
                pos++;
            }
        }
        
        private char peek() {
            skipWhitespace();
            return json.charAt(pos);
        }
    }
    
    // 获取类型的所有字段
    private static Map<String, Field> getTypeFields(Class<?> type) {
        return TYPE_CACHE.computeIfAbsent(type, t -> {
            Map<String, Field> fields = new HashMap<>();
            for (Field field : t.getDeclaredFields()) {
                if (!Modifier.isStatic(field.getModifiers())) {
                    field.setAccessible(true);
                    fields.put(field.getName(), field);
                }
            }
            return fields;
        });
    }
}
