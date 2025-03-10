package com.jsongeek.benchmark.bridge;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.concurrent.TimeUnit;

/**
 * JsonGeekAI的Java桥接类
 * 通过进程间通信调用Node.js中的JsonGeekAI
 */
public class JsonGeekBridge implements AutoCloseable {
    private Process nodeProcess;
    private OutputStreamWriter writer;
    private BufferedReader reader;
    private static final int TIMEOUT_SECONDS = 30;

    public JsonGeekBridge() throws IOException {
        // 启动Node.js进程
        ProcessBuilder pb = new ProcessBuilder("node", "jsongeek-bridge.js");
        pb.directory(new java.io.File("bridge"));
        nodeProcess = pb.start();
        
        writer = new OutputStreamWriter(nodeProcess.getOutputStream());
        reader = new BufferedReader(new InputStreamReader(nodeProcess.getInputStream()));
    }

    /**
     * 解析JSON字符串
     * @param json 要解析的JSON字符串
     * @return 解析结果（JSON字符串）
     */
    public String parse(String json) throws IOException {
        // 发送JSON到Node.js进程
        writer.write(json + "\n");
        writer.flush();

        // 等待结果
        String result = reader.readLine();
        if (result == null) {
            throw new IOException("Node.js process terminated unexpectedly");
        }
        return result;
    }

    @Override
    public void close() {
        try {
            writer.close();
            reader.close();
            nodeProcess.destroy();
            // 等待进程结束
            if (!nodeProcess.waitFor(TIMEOUT_SECONDS, TimeUnit.SECONDS)) {
                nodeProcess.destroyForcibly();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
