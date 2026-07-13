# ------------------------------------------------------------------------------
# 1. ENCAPSULATION (Hiding Data)
# ------------------------------------------------------------------------------
# We use double underscores `__` to make variables "private". This stops outside
# code from changing sensitive data directly. They must use your methods instead.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public variable (anyone can see/change this)
        self.__balance = balance    # PRIVATE variable (hidden from the outside)

    # To let people see the balance safely, we provide a "Getter" method
    def get_balance(self):
        return self.__balance

    # To let people change the balance safely, we provide a "Setter" method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")

account = BankAccount("Alice", 1000)
print(account.owner)                # Works fine! Outputs: Alice
# print(account.__balance)          # ERROR! Python protects this private data.
account.deposit(500)                # Safe way to change the balance.