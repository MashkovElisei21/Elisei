class SuperHero:
    people = 'people'gi

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        return self.name

    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return f"Прозвище: {self.nickname}, Суперспособность: {self.superpower}, Здоровье: {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)



hero = SuperHero('Bruce Wayne', 'Batman', 'суперсила', 100, 'I\'m Batman!')

# Применение методов
print(hero.get_name())
hero.double_health()
print(hero.health_points)
print(hero)
print(len(hero))
