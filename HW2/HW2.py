class SuperHero:
    person = "people"

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def name_hero(self):
        return self.name

    def double_health(self):
        self.health_points = self.health_points * 2

    def __str__(self):
        return f'Имя героя: {self.nickname}, суперспособность: {self.superpower}, ' \
               f'Количество здоровье: {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)


class AirHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False

    def double_health(self):
        self.fly = True
        return self.health_points ** 2

    def true_in_phrase(self):
        return "True in the True_phrase"

    def __str__(self):
        return super().__str__() + f', Урон: {self.damage}, Возможность летать: {self.fly}'

#
# air_hero = AirHero("John", "Airman", "Air Control", 100, "I am the air", 50)
# print(air_hero.true_in_phrase())
# print(air_hero.double_health())
# print(air_hero)


class EarthHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False

    def double_health(self):
        self.health_points = self.health_points ** 2
        self.fly = True

    def true_in_phrase(self):
        return "True in the True_phrase"

    def __str__(self):
        return super().__str__() + f', Урон: {self.damage}, Возможность летать: {self.fly}'


class SpaceHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False

    def double_health(self):
        self.health_points = self.health_points ** 2
        self.fly = True

    def true_in_phrase(self):
        return "True in the True_phrase"

    def __str__(self):
        return super().__str__() + f', Урон: {self.damage}, Возможность летать: {self.fly}'


class Villain(SpaceHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)
    person = "monster"

    def gen_x(self):
        pass

    def crit(self, damage):
        return damage ** 2


air_hero = AirHero("John", "Airman", "Air Control", 100, "I am the air", 50)
earth_hero = EarthHero("Tom", "Earthling", "Earthquake", 80, "I am the earth", 40)
space_hero = SpaceHero("Alice", "Spacewoman", "Zero Gravity", 120, "I am in space", 60)
villain = Villain("Evil Joe", "The Monster", "Pure Evil", 150, "I am the villain", 70)

# print(air_hero)
# print(earth_hero)
# print(space_hero)
# print(villain)
#
# print(f"Length of catchphrase: {len(air_hero)}")
# print(f"Length of catchphrase: {len(villain)}")
#
# air_hero.double_health()
# earth_hero.double_health()
# space_hero.double_health()
# villain.double_health()
#
# print(air_hero)
# print(earth_hero)
# print(space_hero)
# print(villain)
#
# print(air_hero.true_in_phrase())
# print(earth_hero.true_in_phrase())
# print(space_hero.true_in_phrase())
print(villain.damage)
villain.damage = villain.crit(villain.damage)
print(villain.damage)
