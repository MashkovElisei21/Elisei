# bank.py

class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

# Создание нового класса, унаследованного от Bank

class AdvancedBank(Bank):
    def __init__(self, name, balance, account_type):
        super().__init__(name, balance)
        self._account_type = account_type

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value

# Создание нового класса, унаследованного от AdvancedBank

class PremiumBank(AdvancedBank):
    def __init__(self, name, balance, account_type, interest_rate):
        super().__init__(name, balance, account_type)
        self._interest_rate = interest_rate

    @property
    def interest_rate(self):
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        if value < 0:
            raise ValueError("Interest rate cannot be negative")
        self._interest_rate = value
