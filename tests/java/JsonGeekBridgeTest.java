package ai.jsongeek.test;

import ai.jsongeek.JsonGeekBridge;
import ai.jsongeek.JsonGeekException;
import ai.jsongeek.JsonGeekMetrics;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Java API兼容性测试套件
 * 实现P0-P1-P2测试分类策略
 */
public class JsonGeekBridgeTest {
    private JsonGeekBridge parser;

    @BeforeEach
    void setUp() {
        parser = new JsonGeekBridge();
    }

    @Test
    @DisplayName("P0: 基本JSON解析测试")
    void testBasicParsing() {
        String json = "{\"name\": \"JsonGeekAI\", \"version\": \"0.1.1\"}";
        long startTime = System.nanoTime();
        
        Object result = parser.parse(json);
        long parseTime = (System.nanoTime() - startTime) / 1_000_000; // 转换为毫秒
        
        JsonGeekMetrics metrics = parser.getMetrics();
        assertTrue(parseTime < 50, "P0要求：解析时间应小于50ms");
        assertEquals("P0", metrics.getPerformanceGrade());
    }

    @Test
    @DisplayName("P0: SIMD优化验证")
    void testSIMDSupport() {
        assertTrue(parser.hasSIMDSupport(), "应支持SIMD优化");
        
        String json = "[1, 2, 3, 4, 5]";
        Object result = parser.parse(json);
        
        JsonGeekMetrics metrics = parser.getMetrics();
        assertTrue(metrics.isSimdEnabled(), "应启用SIMD优化");
    }

    @Test
    @DisplayName("P1: 大型JSON处理测试")
    void testLargeJsonProcessing() {
        StringBuilder jsonBuilder = new StringBuilder();
        jsonBuilder.append("{\"data\": [");
        for (int i = 0; i < 10000; i++) {
            if (i > 0) jsonBuilder.append(",");
            jsonBuilder.append(i);
        }
        jsonBuilder.append("]}");
        
        String json = jsonBuilder.toString();
        long startTime = System.nanoTime();
        
        Object result = parser.parse(json);
        long parseTime = (System.nanoTime() - startTime) / 1_000_000;
        
        JsonGeekMetrics metrics = parser.getMetrics();
        assertTrue(parseTime < 200, "P1要求：解析时间应小于200ms");
        assertTrue(metrics.getMemoryUsed() < 500 * 1024 * 1024, "P1要求：内存使用应小于500MB");
    }

    @Test
    @DisplayName("P1: 压缩JSON处理测试")
    void testCompressedJsonProcessing() {
        String json = "{\"name\": \"test\", \"data\": \"" + "x".repeat(1000) + "\"}";
        
        Object result = parser.parseCompressed(json, true);
        JsonGeekMetrics metrics = parser.getMetrics();
        
        assertTrue(metrics.getCompressionRatio() < 1.0, "压缩应该有效");
        assertEquals("P1", metrics.getPerformanceGrade());
    }

    @Test
    @DisplayName("P2: Unicode处理测试")
    void testUnicodeHandling() {
        String json = "{\"text\": \"Hello, 世界! 🌍\"}";
        Object result = parser.parse(json);
        
        // P2测试不强制性能要求
        JsonGeekMetrics metrics = parser.getMetrics();
        System.out.println("Unicode处理时间: " + metrics.getParseTime() + "ms");
    }

    @Test
    @DisplayName("P2: 错误处理测试")
    void testErrorHandling() {
        String invalidJson = "{\"name\": }";
        
        assertThrows(JsonGeekException.class, () -> {
            parser.parse(invalidJson);
        });
    }

    @Test
    @DisplayName("性能分级验证")
    void testPerformanceGrading() {
        // P0级测试
        String smallJson = "{\"id\": 1}";
        parser.parse(smallJson);
        JsonGeekMetrics p0Metrics = parser.getMetrics();
        assertEquals("P0", p0Metrics.getPerformanceGrade());

        // P1级测试
        StringBuilder mediumJson = new StringBuilder();
        mediumJson.append("{\"data\": [");
        for (int i = 0; i < 5000; i++) {
            if (i > 0) mediumJson.append(",");
            mediumJson.append(i);
        }
        mediumJson.append("]}");
        
        parser.parse(mediumJson.toString());
        JsonGeekMetrics p1Metrics = parser.getMetrics();
        assertTrue(
            p1Metrics.getPerformanceGrade().equals("P0") || 
            p1Metrics.getPerformanceGrade().equals("P1")
        );

        // P2级测试
        StringBuilder largeJson = new StringBuilder();
        largeJson.append("{\"data\": [");
        for (int i = 0; i < 50000; i++) {
            if (i > 0) largeJson.append(",");
            largeJson.append(i);
        }
        largeJson.append("]}");
        
        parser.parse(largeJson.toString());
        JsonGeekMetrics p2Metrics = parser.getMetrics();
        assertNotNull(p2Metrics.getPerformanceGrade());
    }
}
