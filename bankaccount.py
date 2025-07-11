class BankAccount:
    def __init__(self,number,holder,balance = 0):
        print("A new bank account was created.")
        self.number = number
        self.holder = holder
        self.balance = balance

    def deposit(self):
        self.balance += 20

    def withdraw(self):
        pass

      
