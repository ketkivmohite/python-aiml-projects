# Payment Method Polymorphism in Python

This project demonstrates the concept of **polymorphism** and **inheritance** in Python using a simple payment system example.

## Overview

- A base class `PaymentMethod` defines a generic payment interface.
- Child classes `CreditCard`, `PayPal`, and `Cash` inherit from `PaymentMethod`.
- Each child class overrides the `process_payment` method to handle payments in its own way.
- Demonstrates how polymorphism allows calling the same method on different objects with different behaviors.

## How to Run

1. Clone the repository.
2. Run the Python script `payment.py` using Python 3:
