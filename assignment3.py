class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class DebitCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Debit Card")


class UpiPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")

class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


amount = float(input("Enter payment amount: "))

print("\nSelect Payment Method")
print("1. Credit Card")
print("2. Debit Card")
print("3. UPI")

choice = int(input("Enter your choice: "))

if choice == 1:
    strategy = CreditCardPayment()
elif choice == 2:
    strategy = DebitCardPayment()
elif choice == 3:
    strategy = UpiPayment()
else:
    print("Invalid choice!")
    exit()

processor = PaymentProcessor(strategy)
processor.process_payment(amount)