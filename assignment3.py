
# Strategy Pattern for Payment Processing

# Base Strategy Class
class PaymentStrategy:
    def pay(self, amount):
        pass


# Credit Card Payment
class CreditCard(PaymentStrategy):
    def pay(self, amount):
        print("Paid Rs.", amount, "using Credit Card")


# UPI Payment
class UPI(PaymentStrategy):
    def pay(self, amount):
        print("Paid Rs.", amount, "using UPI")


# PayPal Payment
class PayPal(PaymentStrategy):
    def pay(self, amount):
        print("Paid Rs.", amount, "using PayPal")


# Payment Context Class
class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


# Main Program
print("Select Payment Method:")
print("1. Credit Card")
print("2. UPI")
print("3. PayPal")

choice = int(input("Enter your choice: "))
amount = float(input("Enter payment amount: "))

if choice == 1:
    payment = CreditCard()
elif choice == 2:
    payment = UPI()
elif choice == 3:
    payment = PayPal()
else:
    print("Invalid payment method")
    exit()

processor = PaymentProcessor(payment)
processor.process_payment(amount)
