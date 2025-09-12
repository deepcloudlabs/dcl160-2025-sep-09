from enum import Enum
from typing import Generator


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


# 15:05
"""
Customer --> Account
fullname : str
identity : str
accounts : ?
getAccount(iban: str) -> Account
addAccount(account : Account) -> bool
closeAccount(account) -> bool
getTotalBalance() -> float
"""


class Customer:
    def __init__(self, full_name: str, identity: str):
        self.__full_name = full_name
        self.__identity = identity
        self.__accounts = {}

    @property
    def full_name(self) -> str:
        return self.__full_name

    @property
    def identity(self) -> str:
        return self.__identity

    @property
    def accounts(self) -> Generator[Account]:
        for _ in self.__accounts.values():
            yield _

    def addAccount(self, account: Account) -> Account:
        if account.iban in self.__accounts:
            raise ValueError(f"Account {account.iban} already exists")
        self.__accounts[account.iban] = account
        return account

    def closeAccount(self, account: Account) -> Account:
        if account.iban not in self.__accounts:
            raise ValueError(f"Account {account.iban} does not exist")
        account.status = AccountStatus.CLOSED
        del self.__accounts[account.iban]
        return account

    def getTotalBalance(self) -> float:
        return sum(map(lambda account: account.balance, self.__accounts.values()))

    def getAccount(self, iban: str) -> Account:
        if iban not in self.__accounts:
            raise ValueError(f"Account {iban} does not exist")
        return self.__accounts[iban]

    def __str__(self) -> str:
        return f"Customer[fullname: {self.full_name}, identity: {self.identity}]"

    def printAccounts(self):
        for _ in self.accounts:
            print(_)


# 15:30
class Bank:
    def __init__(self, bddk_id: str, commercial_name: str) -> None:
        self.__bddk_id = bddk_id
        self.__commercial_name = commercial_name
        self.__accounts = {}

    def getCustomer(identity: str) -> Customer:
        pass

    def addCustomer(customer: Customer) -> bool:
        pass

    def releaseCustomer(customer) -> bool:
        pass

    def getAccount(iban: str) -> Account:
        pass

    def getTotalBalance(sel) -> float:  # functional programming
        pass


jack = Customer("jack bauer", "1")
jack.addAccount(Account("TR1", 100_000, AccountStatus.ACTIVE))
jack.addAccount(CheckingAccount("TR2", 200_000, AccountStatus.ACTIVE, 10_000))
jack.addAccount(SavingsAccount("TR3", 300_000, AccountStatus.ACTIVE))
print(jack)
jack.printAccounts()
print(jack.getTotalBalance())  # 600000
jack.closeAccount(jack.getAccount("TR2"))
jack.printAccounts()
print(jack.getTotalBalance())  # 400000
