class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def double_health(self):
        self.health_points **= 2
        self.fly = True  # По умолчанию устанавливаем значение fly на True

    def true_in_phrase(self, True_phrase):
        return True in True_phrase


class AirHero(SuperHero):  # Класс героя воздушной местности
    people = 'air_people'  # Свойство класса

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage

    def double_health(self):
        self.health_points **= 2
        self.fly = True

    def crit(self):
        return self.damage ** 2


class EarthHero(SuperHero):  # Класс героя земной местности
    people = 'earth_people'  # Свойство класса

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage

    def double_health(self):
        self.health_points **= 2
        self.fly = True

    def crit(self):
        return self.damage ** 2


class Villain(EarthHero):  # Класс злодея
    people = 'monster'  # Свойство класса

    def gen_x(self):
        pass

    def crit(self):
        return self.damage ** 3


# Создание объектов классов
air_hero = AirHero('Superman', 'Clark Kent', 'flight', 100, 'Up, up, and away!', 20)
earth_hero = EarthHero('Batman', 'Bruce Wayne', 'intelligence', 150, 'I\'m Batman!', 25)
villain = Villain('Joker', 'The Clown Prince of Crime', 'chaos', 200, 'Why so serious?', 30)

# Применение методов
air_hero.double_health()
print(air_hero.health_points)  # Вывод: 10000
print(air_hero.fly)  # Вывод: True
print(air_hero.true_in_phrase([True, False]))  # Вывод: True
print(air_hero.crit())  # Вывод: 400

earth_hero.double_health()
print(earth_hero.health_points)  # Вывод: 22500
print(earth_hero.fly)  # Вывод: True
print(earth_hero.true_in_phrase([False, True]))  # Вывод: True
print(earth_hero.crit())  # Вывод: 625

print(villain.people)  # Вывод: monster
print(villain.crit())  # Вывод: 27000
