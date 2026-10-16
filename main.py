class Heroes:
    
    def __init__(self, name, element, type,damage):
        self.name = name
        self.element = element
        self.type = type
        self.damage = damage
    
    def attack(self):
        print(f"{self.name} were attacking with {self.element}.")
    
    def voice(self):
        print(f" {self.name} is speaking ")
class Vampires(Heroes):
    def blooddrunk(self):
        print(f" {self.name} drink blood with {self.damage} damage.")
my_vamp = ["ДИО", "stand", " vampire", 31]
my_vamp.blooddrunk()
