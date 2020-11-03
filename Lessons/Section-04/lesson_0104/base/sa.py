from base.account import Account


class SavingsAccount(Account):
    def to_withdraw(self, value):
        if self.balance < value:
            print("Your balance is insufficient.")
            return

        self.balance -= value
        self.details()
