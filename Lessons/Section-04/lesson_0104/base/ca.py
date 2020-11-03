from base.account import Account


class CurrentAccount(Account):
    def __init__(self, agency, account, balance, limit=100):
        super().__init__(agency, account, balance)
        self._limit = limit

    @property
    def limit(self):
        return self._limit

    def to_withdraw(self, value):
        if (self.balance + self.limit) < value:
            print("Your balance is insufficient.")
            return

        self.balance -= value
        self.details()
