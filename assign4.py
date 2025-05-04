# bank.py

class Bank:
    bank_name = "National Bank"  # class variable

    def __init__(self, customer_name):
        self.customer_name = customer_name

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Customer: {self.customer_name}, Bank: {Bank.bank_name}")

# Example usage
b1 = Bank("Iqra")
b2 = Bank("Zain")

b1.display()
b2.display()

# Change the bank name
Bank.change_bank_name("Modern Bank")

# Display again to see the updated bank name
b1.display()
b2.display()
