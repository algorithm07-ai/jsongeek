package ai.jsongeek;

/**
 * Exception class for JsonGeekAI Java API
 */
public class JsonGeekException extends Exception {
    public JsonGeekException(String message) {
        super(message);
    }

    public JsonGeekException(String message, Throwable cause) {
        super(message, cause);
    }
}
