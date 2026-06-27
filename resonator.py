class Resonator:
    current_version = "3.4" 

    def __init__(self, name, element, hp, weapon):
        self.name = name
        self.element = element
        self.max_hp = hp   
        self.hp = hp
        self.weapon = weapon
        self.equipped_echoes = []  

    @classmethod
    def update_game_version(cls, new_version):
        cls.current_version = new_version
        print(f"Game updated to Version {cls.current_version}")

    def is_alive(self):
        return self.hp > 0  

    def display_stats(self):
        print(f"Resonator: {self.name} | Element: {self.element} | HP: {self.hp}/{self.max_hp} | Weapon: {self.weapon}")
        if self.equipped_echoes:
            print(f"Equipped Echoes: {', '.join(self.equipped_echoes)}")
    
    def take_damage(self, amount):
        try:
            if amount < 0:
                raise ValueError
            
            self.hp -= amount
            if self.hp < 0:  
                self.hp = 0
                
            print(f"{self.name} took {amount} damage. Current HP: {self.hp}")
            if not self.is_alive():
                print(f"{self.name} has fallen!")
        except TypeError:
            print("Damage has to be an integer or float.")
        except ValueError:
            print("Damage has to be a positive number.")

    def absorb_echo(self, echo_name):
        self.equipped_echoes.append(echo_name)
        print(f"Successfully absorbed {echo_name} Echo")

    def save_stats(self):
        with open("stats.txt", "w") as f:
            f.write(f"{self.name}, {self.element}, {self.hp}, {self.weapon}")

    def check_stats(self):
        try: 
            with open("stats.txt", "r") as f:
                print(f"Saved Data: {f.read()}")
        except FileNotFoundError:
            print("stats.txt does not exist. Save stats first.")


class Character(Resonator):  

    def __init__(self, name, element, hp, weapon, sequence):
        super().__init__(name, element, hp, weapon)
        self.sequence = sequence

    def use_ultimate(self):
        print(f"{self.name} unleashes Resonance Liberation")

    def resonance_chain(self):
        print(f"Resonance Chain: S{self.sequence}")

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["element"], data["hp"], data["weapon"], data["sequence"])

    @staticmethod
    def calculate_damage(atk, crit_multiplier):
        print(atk * crit_multiplier)


rover = Character.from_dict({
    "name": "Rover", 
    "element": "Spectro", 
    "hp": 12000, 
    "weapon": "Sword", 
    "sequence": 6
})

rover.absorb_echo("Crownless")
rover.absorb_echo("Havoc Dreadmane")

rover.display_stats() 
rover.resonance_chain() 

rover.save_stats()
rover.check_stats()

rover.use_ultimate()
rover.take_damage(5000)
print(rover.is_alive())
rover.calculate_damage(2200, 2.5)
