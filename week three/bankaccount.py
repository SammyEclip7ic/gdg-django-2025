class BankAccount:
    def __init__(self):
        self.__balance = 0
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return f"Total Balance: {self.__balance}"

my_account = BankAccount()
my_account.deposit(100)
my_account.withdraw(200)
