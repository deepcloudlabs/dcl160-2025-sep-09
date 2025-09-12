from enum import Enum


class AccountStatus(Enum):
    ACTIVE = 100
    BLOCKED = 200
    CLOSED = 300


class Account(object):
    """
    attributes: iban, balance, status
    behaviour: withdraw, deposit
    """

    def __init__(self, iban: str, balance: float = 0.0, status: AccountStatus = AccountStatus.ACTIVE):
        self.__iban = iban
        self.__balance = balance
        self.__status = status

    @property  # getter
    def balance(self) -> float:
        return self.__balance

    @property  # getter
    def iban(self) -> str:
        return self.__iban

    @property  # getter
    def status(self) -> AccountStatus:
        return self.__status

    @status.setter  # setter
    def status(self, new_status: AccountStatus):
        self.__status = new_status

    # business method
    def withdraw(self, amount: float) -> float:
        """
        withdraw money from the account
        :param amount: amount to withdraw
        :return: returns the actual balance
        """
        # validation
        if amount <= 0.0:
            raise ValueError("amount must be positive")
        # business rule
        if self.__status != AccountStatus.ACTIVE:
            raise ValueError("status must be ACTIVE")
        # business rule
        if self.__balance < amount:
            raise ValueError(f"amount ({amount}) must be less than or equal to balance ({self.__balance})")
        self.__balance -= amount
        return self.__balance

    # business method
    def deposit(self, amount: float) -> float:
        """
        deposit money to the account
        :param amount: amount to deposit
        :return: returns the actual balance
        """
        # validation
        if amount <= 0.0:
            raise ValueError("amount must be positive")
        # business rule
        if self.__status != AccountStatus.ACTIVE:
            raise ValueError("status must be ACTIVE")
        self.__balance += amount
        return self.__balance

    def __str__(self) -> str:
        return f"Account [iban: {self.iban}, balance:{self.balance}, status: {self.status}]"

    def __eq__(self, other): # operator overloading
        return self.__iban == other.iban

    def __add__(self, other):
        if self.__iban != other.iban or self.__status != other.status:
            raise ValueError("iban must be equal to account")
        return Account(self.iban, self.balance + other.balance, self.status)

    def __gt__(self, other):
        return self.__balance > other.balance

    def __lt__(self, other):
        return self.__balance < other.balance

acc1 = Account(iban="TR1", balance=10_000_000.0, status=AccountStatus.ACTIVE)
acc2 = Account(iban="TR1", balance=20_000_000.0, status=AccountStatus.ACTIVE)
print(str(acc1))
print(acc1.__str__())
print(acc1.__eq__(acc2))
print(acc1 == acc2)
acc3 = acc1 + acc2
print(acc1 < acc2) # True
print(acc1 > acc2) # False
try:
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
