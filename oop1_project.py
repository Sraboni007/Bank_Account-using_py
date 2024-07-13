from bank_account import *

Dave = BankAccount(1000, "Dave")
Raju = BankAccount(2000, "Raju")

Dave.getBalance()
Raju.getBalance()

Raju.deposit(500)

Dave.withdraw(10000)
Dave.withdraw(10)

Dave.transfer(100, Raju)

Sam = InterestRewardsAcct(1000, "Sam")
Sam.getBalance()
Sam.deposit(100)
Sam.transfer(100, Dave)

Blaze = savingsAcct(1000, "Blaze")
Blaze.getBalance()
Blaze.deposit(100)
Blaze.transfer(10000, Raju)
