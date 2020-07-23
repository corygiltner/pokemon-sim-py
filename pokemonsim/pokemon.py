class Pokemon:
    def __init__(self,health = 100, attack = 0, defense = 0, sp_attack = 0, sp_defense = 0, speed = 0, level = 0, pok_type = None):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed
        self.level = level
        self.pok_type = pok_type

class Pikachu(Pokemon):
    def __init__():
        self.attack = 20
        self.pok_type = "water"

    def water_gun(self, opponent : Pokemon):
        opponent.health = opponent.health - self.attack
        

class Squirtle(Pokemon):
    def __init__():
        self.attack = 15
        self.pok_type = "electric"

    def thunder_jolt(self, opponent : Pokemon)
        opponent.health = opponent.health - self.attack
    