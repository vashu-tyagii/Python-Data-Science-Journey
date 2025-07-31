# Encapsulation and Abstraction (Conceptual)
class BankAccount:
    def __init__(self, account_number, initial_balance):  # type:ignore
        self.__account_number = account_number  # "Private" attribute (by convention)
        self.__balance = initial_balance

    def deposit(self, amount):  # type:ignore
        if amount > 0:
            self.__balance += amount  # type:ignore
            print(f"Deposited {amount}. New balance: {self.__balance}")  # type:ignore
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):  # type:ignore
        if 0 < amount <= self.__balance:  # type:ignore
            self.__balance -= amount  # type:ignore
            print(f"Withdrew {amount}. New balance: {self.__balance}")  # type:ignore
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):  # type:ignore
        # This is an "abstracted" way to get the balance
        return self.__balance  # type:ignore


my_account = BankAccount("12345", 1000)
my_account.deposit(500)  # type:ignore
my_account.withdraw(200)  # type:ignore
# print(my_account.__balance) # This would lead to an AttributeError (name mangling)
print(f"Current balance: {my_account.get_balance()}")
my_account.withdraw(2000)  # Insufficient funds #type:ignore