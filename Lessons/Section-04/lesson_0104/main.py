# 104. Classes Abstratas - Python Orientado a Objetos

from base.sa import SavingsAccount
from base.ca import CurrentAccount

print("---------------------------------------------------")

sa = SavingsAccount(1111, 2222, 0)
sa.deposit(10)
sa.to_withdraw(2)
sa.to_withdraw(8)
sa.to_withdraw(1)

print("---------------------------------------------------")

ca = CurrentAccount(agency=1010, account=2589, balance=1200, limit=350)
ca.deposit(120)
ca.to_withdraw(875)
ca.deposit(1200)

print("---------------------------------------------------")
