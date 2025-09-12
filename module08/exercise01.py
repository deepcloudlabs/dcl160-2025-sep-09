class Account:
    """
    attributes: iban, balance, status
    behaviour: withdraw, deposit
    """
    def __init__(self, iban: str, balance: float= 0.0, status: str = "ACTIVE"):
        self.iban = iban
        self.balance = balance
        self.status = status
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
        if self.status != "ACTIVE":
            raise ValueError("status must be ACTIVE")
        # business rule
        if self.balance < amount:
            raise ValueError("amount must be greater than balance")
        self.balance -= amount
        return self.balance

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
        if self.status != "ACTIVE":
            raise ValueError("status must be ACTIVE")
        self.balance += amount
        return self.balance