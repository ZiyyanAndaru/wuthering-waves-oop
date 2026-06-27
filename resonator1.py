class Resonator():
    current_version = 3.4

    def track_version(self):
        print(f"The current version is {self.current_version}")

    def __init__(self, name, element, hp, weapon):
        self.name = name
        self.element = element
        self.hp = hp 
        self.weapon = weapon

    def is_alive(self):
        if self.hp <= 0:
            return False
        return True
    
    def display_stats(self):
        print(f"Resonator:{self.name}, Element:{self.element}, HP:{self.hp}, Weapon Type:{self.weapon}")
    
    def take_damage(self, amount):
        try:
            if amount < 0:
                raise ValueError
            self.hp = self.hp - amount
            print(f"HP After Damage: {self.hp}")
        except TypeError:
            print("Damage has to be an integer")
        except ValueError:
            print("Damage has to be a positive integer")

    def save_stats(self):
        with open("stats.txt", "w") as f:
            f.write(f"{self.name}, {self.element}, {self.hp}, {self.weapon}")

    def check_stats(self):
        try: 
            with open("stats.txt", "r") as f:
                content = f.read()
                print(content)
        except FileNotFoundError:
            print("stats.txt does not exist. You need to save the stats first.")

class MainCharacter(Resonator):

    def __init__(self, name, element, hp, weapon, forte_level):
        super().__init__(name, element, hp, weapon)
        self.forte_level = forte_level

    def use_ultimate(self):
        print(f"The Resonator {self.name} has used their ultimate")

    def forte_circuit(self):
        print(f"Forte Circuit Level: {self.forte_level}")

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["element"], data["hp"], data["weapon"], data["forte_level"])

    @staticmethod
    def calculate_damage(damage, multiplier):
        return damage * multiplier
        



Denia = MainCharacter.from_dict({"name": "Denia", "element": "Fusion", "hp": 16000, "weapon": "Rectifier", "forte_level": 9})


Denia.save_stats()
Denia.check_stats()


