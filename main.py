class Heroes:
    
    def __init__(self, name, element, type,damage):
        self.name = name
        self.element = element
        self.type = type
        self.damage = damage

    def attack(self):
        print(f"{self.name} were attacking with {self.element}.")

    def voice(self):
        print(f"{self.name} is speaking ")

class Vampires(Heroes):
    def blooddrunk(self):
        print(f"{self.name} drink blood with {self.damage} damage.")

class Light(Heroes):
    def attacklight(self):
        print(f"{self.name} is attacks with light power.")

class Physical(Heroes):
    def Megapunch(self):
        print(f"{self.name} is attacking with  giant physic power.")

class Magic(Heroes):
    def MagicAttack(self):
        print(f"{self.name} is attack with mahic power.")

class Sworder(Heroes):
    def SwordAttack(self):
        print(f"{self.name} is attack with sword.")

