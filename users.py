
from bank import PremiumBank

# Создание экземпляра класса PremiumBank
account = PremiumBank("John Doe", 10000, "Savings", 0.05)

# Использование property для изменения аргументов
account.name = "Jane Doe"
account.balance = 15000
account.account_type = "Checking"
account.interest_rate = 0.03

print(f"Name: {account.name}")
print(f"Balance: {account.balance}")
print(f"Account Type: {account.account_type}")
print(f"Interest Rate: {account.interest_rate}")
