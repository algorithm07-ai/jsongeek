package ai.jsongeek;

/**
 * Java API Bridge for JsonGeekAI
 * Provides Java compatibility layer for the SIMD-optimized JSON parser
 */
public class JsonGeekBridge {
    static {
        System.loadLibrary("jsongeekai");
    }

    /**
     * Parse JSON string using SIMD optimization
     * @param jsonStr JSON string to parse
     * @return Parsed Java object
     * @throws JsonGeekException if parsing fails
     */
    public native Object parse(String jsonStr) throws JsonGeekException;

    /**
     * Parse JSON string with compression
     * @param jsonStr JSON string to parse
     * @param useCompression whether to use smart compression
     * @return Parsed Java object
     * @throws JsonGeekException if parsing fails
     */
    public native Object parseCompressed(String jsonStr, boolean useCompression) throws JsonGeekException;

    /**
     * Get performance metrics from the last parse operation
     * @return Performance metrics as a JsonGeekMetrics object
     */
    public native JsonGeekMetrics getMetrics();

    /**
     * Check if SIMD is supported on the current platform
     * @return true if SIMD is supported
     */
    public native boolean hasSIMDSupport();
}
