class Pet:
    pets = [
        ("papousek1", 5000),
        ("papousek2", 50000),
        ("papousek3", 1000),
        ("papousek4", 80),
        ("papousek5", 15000),
    ]

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Pet, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        self.selected_pet = None

    def choose_pet(self, name):
        if self.selected_pet is not None:
            raise Exception("You can only choose one pet!")
        for pet_name, price in self.pets:
            if pet_name == name and price < 8000:
                self.selected_pet = (pet_name, price)
                return f"You have selected {pet_name} for {price}."
        raise ValueError("Pet not found or price is too high!")

# Příklad použití
pet_singleton = Pet()
print(pet_singleton.choose_pet("papousek1"))  # Vybere papousek1
  # Pokusí se vybrat papousek2, ale vyvolá výjimku
# Pokud se pokusíte vybrat dalšího mazlíčka, vyvolá se výjimka
# print(pet_singleton.choose_pet("papousek3"))