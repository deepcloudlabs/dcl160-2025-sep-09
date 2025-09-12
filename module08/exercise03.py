from banking.core import Account, CheckingAccount, SavingsAccount, AccountStatus

acc1 = Account(iban="TR1", balance=10_000_000.0, status=AccountStatus.ACTIVE)
acc2 = Account(iban="TR1", balance=20_000_000.0, status=AccountStatus.ACTIVE)
print(str(acc1))
print(acc1.__str__())
print(acc1.__eq__(acc2))
print(acc1 == acc2)
acc3 = acc1 + acc2
print(acc1 < acc2)  # True
print(acc1 > acc2)  # False
acc4 = CheckingAccount("TR4", 100_000, AccountStatus.ACTIVE, 5_000.0)
acc5 = SavingsAccount("TR5", 5_000_000, AccountStatus.ACTIVE)

print(acc4)
print(acc5)
print(acc5.deposit(1_000_000))
print(acc5.withdraw(1_000_000))
try:
    print(acc4.withdraw(105_000))
    print(acc1.withdraw(3_000_000))  # 7_000_000
    # print(acc1.withdraw(9_000_000)) # raised an exception
    # acc1.__balance -= 9_000_000
    # acc1.balance -= 9_000_000
    print(f"acc1.balance: {acc1.balance}")
    acc1.status = AccountStatus.BLOCKED
    print(f"acc1.status: {acc1.status.value},{acc1.status.name}")
    acc1.deposit(3_000_000)  # deposit(acc1,3_000_000)
except ValueError as e:
    print(e)