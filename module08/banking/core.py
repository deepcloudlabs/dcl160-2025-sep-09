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
        print("Account's withdraw() method is called")
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

    def __eq__(self, other):  # operator overloading
        return self.__iban == other.iban

    def __add__(self, other):
        if self.__iban != other.iban or self.__status != other.status:
            raise ValueError("iban must be equal to account")
        return Account(self.iban, self.balance + other.balance, self.status)

    def __gt__(self, other):
        return self.__balance > other.balance

    def __lt__(self, other):
        return self.__balance < other.balance


"""
CheckingAccount: Sub-class, Derived Class
Account        : Super-class, Based Class
"""


class CheckingAccount(Account):
    def __init__(self, iban: str, balance: float = 0.0, status: AccountStatus = AccountStatus.ACTIVE,
                 overdraft_amount: float = 1_000):
        super().__init__(iban, balance, status)
        self.__overdraft_amount = overdraft_amount

    @property
    def overdraft_amount(self) -> float:
        return self.__overdraft_amount

    @overdraft_amount.setter
    def overdraft_amount(self, new_amount: float):
        self.__overdraft_amount = new_amount

    def withdraw(self, amount: float) -> float:
        print("CheckingAccount's withdraw() method is called")
        if amount <= 0.0:
            raise ValueError("amount must be positive")
        if self.status != AccountStatus.ACTIVE:
            raise ValueError("status must be ACTIVE")
        if self.balance + self.overdraft_amount < amount:
            raise ValueError("amount must be greater than balance")
        self._Account__balance -= amount
        return self.balance

    def __str__(self) -> str:
        return f"CheckingAccount [iban: {self.iban}, balance:{self.balance}, status: {self.status}, overdraft_amount:{self.overdraft_amount}]"


class SavingsAccount(Account):
    def __init__(self, iban: str, balance: float = 0.0, status: AccountStatus = AccountStatus.ACTIVE):
        super().__init__(iban, balance, status)

    def deposit(self, amount: float) -> float:
        return self.balance

    def withdraw(self, amount: float) -> float:
        print("SavingsAccount's withdraw() method is called")
        return self.balance

    def __str__(self) -> str:
        return f"SavingsAccount [iban: {self.iban}, balance:{self.balance}, status: {self.status}]"
