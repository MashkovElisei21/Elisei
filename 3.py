class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        amount = float(input("Введите сумму для добавления на счет: "))
        self._balance += amount

    def kill(self):
        self._balance = 0

    def _jackpot(self):
        self._balance *= 10

    def _merge_balance(self, other):
        self._balance += other._balance

# Класс калькулятора
class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def mul(self):
        return self.x * self.y

    def truediv(self):
        if self.y != 0:
            return self.x / self.y
        else:
            return "Ошибка: деление на ноль"

# Пример использования класса Bank
if __name__ == "__main__":
    client1 = Bank("John", 100)
    client2 = Bank("Alice", 200)

    print(f"Баланс {client1._name}: {client1._balance}")
    print(f"Баланс {client2._name}: {client2._balance}")

    client1._merge_balance(client2)

    print(f"Баланс {client1._name}: {client1._balance}")
    print(f"Баланс {client2._name}: {client2._balance}")

# Пример использования класса Calculator
    calc = Calculator(10, 5)
    print("Сложение:", calc.add())
    print("Вычитание:", calc.sub())
    print("Умножение:", calc.mul())
    print("Деление:", calc.truediv())
