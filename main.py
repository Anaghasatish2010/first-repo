from bankaccount import BankAccount

acc1 = BankAccount(holder = "Anagha", number = 2406, balance = 20000000)
print(acc1)
print(type(acc1))
print(acc1.balance)
print(acc1.holder)
print(acc1.number)

acc2 = BankAccount(holder = "Priya", number = 3140, balance = 300000000)
print(acc2.balance)
print(acc2.holder)
print(acc2.number)
 
acc1.deposit(20)

