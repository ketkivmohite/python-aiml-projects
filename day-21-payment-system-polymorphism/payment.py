class PaymentMethod:
    def process_payment(self,amount):
        print(f"Processing your generic amount of ${amount}")

class CreditCard(PaymentMethod):
     def process_payment(self,amount):
        print(f"Processing credit card payment of ${amount}")
  

class PayPal(PaymentMethod):
     def process_payment(self,amount):
        print(f"Processing PayPal payment of ${amount}")

class Cash(PaymentMethod):
     def process_payment(self,amount):
        print(f"Processing cash amount of ${amount}")

payments = [CreditCard() , PayPal() , Cash()]

for payment in payments:
    payment.process_payment(100)

