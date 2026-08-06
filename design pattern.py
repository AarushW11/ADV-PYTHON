class CreditCard:
    def pay(self, amount):
        print("Paid ₹", amount, "using Credit Card")


class DebitCard:
    def pay(self, amount):
        print("Paid ₹", amount, "using Debit Card")


class UPI:
    def pay(self, amount):
        print("Paid ₹", amount, "using UPI")


# Context Class
class Payment:
    def __init__(self, strategy):
        self.strategy = strategy

    def make_payment(self, amount):
        self.strategy.pay(amount)


# Main Program
print("Select Payment Method")
print("1. Credit Card")
print("2. Debit Card")
print("3. UPI")

choice = int(input("Enter your choice: "))
amount = float(input("Enter amount: ₹"))

if choice == 1:
    payment = Payment(CreditCard())
elif choice == 2:
    payment = Payment(DebitCard())
elif choice == 3:
    payment = Payment(UPI())
else:
    print("Invalid Choice")
    exit()

payment.make_payment(amount)