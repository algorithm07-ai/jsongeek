package ai.jsongeek;

/**
 * Performance metrics for JsonGeekAI Java API
 * Provides detailed performance information for monitoring and optimization
 */
public class JsonGeekMetrics {
    private double parseTime;        // Parsing time in milliseconds
    private double compressionRatio; // Compression ratio (compressed/original)
    private long memoryUsed;        // Memory usage in bytes
    private boolean simdEnabled;     // Whether SIMD was used
    private boolean compressionEnabled; // Whether compression was used

    /**
     * Get the parsing time in milliseconds
     * @return parsing time
     */
    public double getParseTime() {
        return parseTime;
    }

    /**
     * Get the compression ratio
     * @return compression ratio
     */
    public double getCompressionRatio() {
        return compressionRatio;
    }

    /**
     * Get memory usage in bytes
     * @return memory usage
     */
    public long getMemoryUsed() {
        return memoryUsed;
    }

    /**
     * Check if SIMD was enabled for the operation
     * @return true if SIMD was enabled
     */
    public boolean isSimdEnabled() {
        return simdEnabled;
    }

    /**
     * Check if compression was enabled for the operation
     * @return true if compression was enabled
     */
    public boolean isCompressionEnabled() {
        return compressionEnabled;
    }

    /**
     * Get performance grade based on P0-P2 classification
     * P0: Critical performance requirements
     * P1: Regular performance targets
     * P2: Optional performance goals
     * @return performance grade (P0, P1, or P2)
     */
    public String getPerformanceGrade() {
        // P0 requirements
        if (parseTime < 50 && memoryUsed < 1024 * 1024 * 100) { // 50ms, 100MB
            return "P0";
        }
        // P1 requirements
        else if (parseTime < 200 && memoryUsed < 1024 * 1024 * 500) { // 200ms, 500MB
            return "P1";
        }
        // P2 requirements
        else {
            return "P2";
        }
    }

    /**
     * Get detailed performance report
     * @return performance report as string
     */
    @Override
    public String toString() {
        return String.format(
            "JsonGeekMetrics{\n" +
            "  parseTime=%.2fms\n" +
            "  compressionRatio=%.2f\n" +
            "  memoryUsed=%d bytes\n" +
            "  simdEnabled=%b\n" +
            "  compressionEnabled=%b\n" +
            "  performanceGrade=%s\n" +
            "}",
            parseTime,
            compressionRatio,
            memoryUsed,
            simdEnabled,
            compressionEnabled,
            getPerformanceGrade()
        );
    }
}
