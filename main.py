from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "наносит удар мечом"

class Bow(Weapon):
    def attack(self):
        return "пускает стрелу из лука"

class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def changeWeapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            return self.weapon.attack()
        else:
            return "не вооружен"


class Monster:
    def __init__(self, name):
        self.name = name

def battle(player, monster):

    print(f"{player.name} {player.attack()}")
    print(f"{monster.name} побежден")

sword = Sword()
bow = Bow()

# Пример

fighter = Fighter("Богатырь Вася")
monster = Monster("Дракон")

print(f"{fighter.name} выходит на поле битвы")
print(f"на встречу выходит {monster.name}! \n Начинается битва")

fighter.changeWeapon(sword)
battle(fighter, monster)

fighter.changeWeapon(bow)

battle(fighter, monster)
