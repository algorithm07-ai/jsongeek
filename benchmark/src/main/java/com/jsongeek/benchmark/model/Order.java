package com.jsongeek.benchmark.model;

import lombok.Data;
import java.util.List;
import java.util.Date;

@Data
public class Order {
    private String orderId;
    private String customerId;
    private Date orderDate;
    private String status;
    private Address shippingAddress;
    private Address billingAddress;
    private List<OrderItem> items;
    private PaymentInfo paymentInfo;
    private double totalAmount;
    private double tax;
    private double shippingCost;
    private String currency;
    private List<String> tags;
    private Map<String, String> metadata;
}

@Data
class Address {
    private String street;
    private String city;
    private String state;
    private String country;
    private String postalCode;
    private String phoneNumber;
}

@Data
class OrderItem {
    private String productId;
    private String productName;
    private int quantity;
    private double unitPrice;
    private double discount;
    private String sku;
    private Map<String, String> attributes;
}

@Data
class PaymentInfo {
    private String paymentMethod;
    private String transactionId;
    private String cardType;
    private String lastFourDigits;
    private Date paymentDate;
    private String paymentStatus;
}
