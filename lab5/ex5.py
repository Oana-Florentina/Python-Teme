class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Habitat: {self.habitat}")

class Mammal(Animal):
    def __init__(self, name, habitat, fur_color):
        super().__init__(name, habitat)
        self.fur_color = fur_color

    def display_info(self):
        super().display_info()
        print(f"Class: Mammal")
        print(f"Fur Color: {self.fur_color}")

    def give_birth(self):
        print(f"{self.name} is a mammal and gives birth to live young.")

class Bird(Animal):
    def __init__(self, name, habitat, feather_color):
        super().__init__(name, habitat)
        self.feather_color = feather_color

    def display_info(self):
        super().display_info()
        print(f"Class: Bird")
        print(f"Feather Color: {self.feather_color}")

    def lay_eggs(self):
        print(f"{self.name} is a bird and lays eggs.")

class Fish(Animal):
    def __init__(self, name, habitat, scale_color):
        super().__init__(name, habitat)
        self.scale_color = scale_color

    def display_info(self):
        super().display_info()
        print(f"Class: Fish")
        print(f"Scale Color: {self.scale_color}")

    def lay_eggs(self):
        print(f"{self.name} is a fish and lays eggs.")


mammal = Mammal(name="Lion", habitat="Grassland", fur_color="Golden")
mammal.display_info()
mammal.give_birth()

bird = Bird(name="Eagle", habitat="Sky", feather_color="Brown")
bird.display_info()
bird.lay_eggs()

fish = Fish(name="Salmon", habitat="River", scale_color="Silver")
fish.display_info()
fish.lay_eggs()
