
from colorama import init, Back, Style

# Инициализация Colorama
init(autoreset=True)

# Использование colorama для изменения цвета фона вывода
print(Back.CYAN + 'This is a test message with a cyan background')

# Вывести все зависимости в файл
with open('requirements.txt', 'w') as f:
    dependencies = !pip freeze
    f.write('\n'.join(dependencies))
