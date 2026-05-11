class Character:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    
    def __str__(self):
        return f"Chracter se jménem {self.name} má roly {self.role}"
    
    def __del__ (self):
        print(f"Postava {self.name} byla odstraněna ze světa.")

class PlayerCharacter(Character):
    def __init__ (self, name, role, c_d):
        super().__init__(name, role)
        self.control_device = c_d
    
    def __str__ (self):
        return f"Postava se jménem {self.name} má ovládací zařízení {self.control_device}"
    
player1 = Character("Aragorn", "Ranger")
player2 = PlayerCharacter("Aragorn", "Ranger", "Keyboard")
print(player1)
print(player2)