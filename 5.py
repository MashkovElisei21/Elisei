
with open('reg.txt', 'r') as file:
    dependencies = file.readlines()


with open('requirements.txt', 'w') as file:
    for dependency in dependencies:
        file.write(dependency.strip() + '\n')

class Hello:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"


class NewHello(Hello):
    def __init__(self, name):
        super().__init__(name)

    def tptint(self):
        return f"Hi, {self.name}! Have a good day!"


from class1 import NewHello



obj = NewHello("Alice")



print(obj.tptint())

