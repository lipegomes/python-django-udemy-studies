from abc import ABC, abstractclassmethod


class Account(ABC):
    def __init__(self, agency, account, balance):
        self._agency = agency
        self._account = account
        self._balance = balance

    @property
    def agency(self):
        return self._agency

    @property
    def account(self):
        return self._account

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("The balance amount must be numeric.")

        self._balance = value

    def deposit(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("The deposit amount must be numeric.")

        self.balance += value
        self.details()

    def details(self):
        print(f"Agency: {self.agency}", end=" ")
        print(f"Account: {self.account}", end=" ")
        print(f"Balance: {self.balance}")

    @abstractclassmethod
    def to_withdraw(self, value):
        pass
