package com.jsongeek.benchmark;

import com.alibaba.fastjson2.JSON;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.google.gson.Gson;
import com.jsongeek.benchmark.model.Order;
import com.jsongeek.JsonGeekAI;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.Blackhole;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;

import java.util.*;
import java.util.concurrent.TimeUnit;

@BenchmarkMode(Mode.AverageTime)
@OutputTimeUnit(TimeUnit.MICROSECONDS)
@State(Scope.Benchmark)
@Fork(value = 2, jvmArgs = {"-Xms2G", "-Xmx2G"})
@Warmup(iterations = 3)
@Measurement(iterations = 8)
public class JsonBenchmark {

    private String smallJson;
    private String mediumJson;
    private String largeJson;
    private Order smallOrder;
    private Order mediumOrder;
    private Order largeOrder;

    private ObjectMapper jackson;
    private Gson gson;
    private JsonGeekAI jsonGeekAI;

    @Setup
    public void setup() {
        // 初始化解析器
        jackson = new ObjectMapper();
        gson = new Gson();
        jsonGeekAI = new JsonGeekAI();

        // 生成测试数据
        smallOrder = generateOrder(5);
        mediumOrder = generateOrder(50);
        largeOrder = generateOrder(500);

        // 将对象转换为JSON字符串
        smallJson = JSON.toJSONString(smallOrder);
        mediumJson = JSON.toJSONString(mediumOrder);
        largeJson = JSON.toJSONString(largeOrder);
    }

    // 序列化基准测试 - 小对象
    @Benchmark
    public void serializeSmall_FastJson2(Blackhole blackhole) {
        blackhole.consume(JSON.toJSONString(smallOrder));
    }

    @Benchmark
    public void serializeSmall_Jackson(Blackhole blackhole) throws Exception {
        blackhole.consume(jackson.writeValueAsString(smallOrder));
    }

    @Benchmark
    public void serializeSmall_Gson(Blackhole blackhole) {
        blackhole.consume(gson.toJson(smallOrder));
    }

    @Benchmark
    public void serializeSmall_JsonGeekAI(Blackhole blackhole) {
        blackhole.consume(jsonGeekAI.toJson(smallOrder));
    }

    // 序列化基准测试 - 中等对象
    @Benchmark
    public void serializeMedium_FastJson2(Blackhole blackhole) {
        blackhole.consume(JSON.toJSONString(mediumOrder));
    }

    @Benchmark
    public void serializeMedium_Jackson(Blackhole blackhole) throws Exception {
        blackhole.consume(jackson.writeValueAsString(mediumOrder));
    }

    @Benchmark
    public void serializeMedium_Gson(Blackhole blackhole) {
        blackhole.consume(gson.toJson(mediumOrder));
    }

    @Benchmark
    public void serializeMedium_JsonGeekAI(Blackhole blackhole) {
        blackhole.consume(jsonGeekAI.toJson(mediumOrder));
    }

    // 序列化基准测试 - 大对象
    @Benchmark
    public void serializeLarge_FastJson2(Blackhole blackhole) {
        blackhole.consume(JSON.toJSONString(largeOrder));
    }

    @Benchmark
    public void serializeLarge_Jackson(Blackhole blackhole) throws Exception {
        blackhole.consume(jackson.writeValueAsString(largeOrder));
    }

    @Benchmark
    public void serializeLarge_Gson(Blackhole blackhole) {
        blackhole.consume(gson.toJson(largeOrder));
    }

    @Benchmark
    public void serializeLarge_JsonGeekAI(Blackhole blackhole) {
        blackhole.consume(jsonGeekAI.toJson(largeOrder));
    }

    // 反序列化基准测试 - 小对象
    @Benchmark
    public void deserializeSmall_FastJson2(Blackhole blackhole) {
        blackhole.consume(JSON.parseObject(smallJson, Order.class));
    }

    @Benchmark
    public void deserializeSmall_Jackson(Blackhole blackhole) throws Exception {
        blackhole.consume(jackson.readValue(smallJson, Order.class));
    }

    @Benchmark
    public void deserializeSmall_Gson(Blackhole blackhole) {
        blackhole.consume(gson.fromJson(smallJson, Order.class));
    }

    @Benchmark
    public void deserializeSmall_JsonGeekAI(Blackhole blackhole) {
        blackhole.consume(jsonGeekAI.fromJson(smallJson, Order.class));
    }

    // 反序列化基准测试 - 中等对象
    @Benchmark
    public void deserializeMedium_FastJson2(Blackhole blackhole) {
        blackhole.consume(JSON.parseObject(mediumJson, Order.class));
    }

    @Benchmark
    public void deserializeMedium_Jackson(Blackhole blackhole) throws Exception {
        blackhole.consume(jackson.readValue(mediumJson, Order.class));
    }

    @Benchmark
    public void deserializeMedium_Gson(Blackhole blackhole) {
        blackhole.consume(gson.fromJson(mediumJson, Order.class));
    }

    @Benchmark
    public void deserializeMedium_JsonGeekAI(Blackhole blackhole) {
        blackhole.consume(jsonGeekAI.fromJson(mediumJson, Order.class));
    }

    // 反序列化基准测试 - 大对象
    @Benchmark
    public void deserializeLarge_FastJson2(Blackhole blackhole) {
        blackhole.consume(JSON.parseObject(largeJson, Order.class));
    }

    @Benchmark
    public void deserializeLarge_Jackson(Blackhole blackhole) throws Exception {
        blackhole.consume(jackson.readValue(largeJson, Order.class));
    }

    @Benchmark
    public void deserializeLarge_Gson(Blackhole blackhole) {
        blackhole.consume(gson.fromJson(largeJson, Order.class));
    }

    @Benchmark
    public void deserializeLarge_JsonGeekAI(Blackhole blackhole) {
        blackhole.consume(jsonGeekAI.fromJson(largeJson, Order.class));
    }

    // 生成测试数据
    private Order generateOrder(int itemCount) {
        Order order = new Order();
        order.setOrderId(UUID.randomUUID().toString());
        order.setCustomerId(UUID.randomUUID().toString());
        order.setOrderDate(new Date());
        order.setStatus("PROCESSING");
        
        Address address = new Address();
        address.setStreet("123 Test St");
        address.setCity("Test City");
        address.setState("Test State");
        address.setCountry("Test Country");
        address.setPostalCode("12345");
        address.setPhoneNumber("+1234567890");
        
        order.setShippingAddress(address);
        order.setBillingAddress(address);
        
        List<OrderItem> items = new ArrayList<>();
        for (int i = 0; i < itemCount; i++) {
            OrderItem item = new OrderItem();
            item.setProductId(UUID.randomUUID().toString());
            item.setProductName("Product " + i);
            item.setQuantity(i + 1);
            item.setUnitPrice(10.0 + i);
            item.setDiscount(i % 2 == 0 ? 0.1 : 0.0);
            item.setSku("SKU" + i);
            
            Map<String, String> attributes = new HashMap<>();
            attributes.put("color", "red");
            attributes.put("size", "medium");
            attributes.put("weight", "1.5kg");
            item.setAttributes(attributes);
            
            items.add(item);
        }
        order.setItems(items);
        
        PaymentInfo paymentInfo = new PaymentInfo();
        paymentInfo.setPaymentMethod("CREDIT_CARD");
        paymentInfo.setTransactionId(UUID.randomUUID().toString());
        paymentInfo.setCardType("VISA");
        paymentInfo.setLastFourDigits("1234");
        paymentInfo.setPaymentDate(new Date());
        paymentInfo.setPaymentStatus("COMPLETED");
        
        order.setPaymentInfo(paymentInfo);
        order.setTotalAmount(1000.0);
        order.setTax(100.0);
        order.setShippingCost(50.0);
        order.setCurrency("USD");
        
        List<String> tags = Arrays.asList("premium", "express", "international");
        order.setTags(tags);
        
        Map<String, String> metadata = new HashMap<>();
        metadata.put("source", "web");
        metadata.put("priority", "high");
        metadata.put("notes", "Handle with care");
        order.setMetadata(metadata);
        
        return order;
    }

    public static void main(String[] args) throws RunnerException {
        Options opt = new OptionsBuilder()
                .include(JsonBenchmark.class.getSimpleName())
                .build();
        new Runner(opt).run();
    }
}
