class Animal:
    """Base class for all animals"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        """General eating method for all animals"""
        print(f"{self.name} is eating.")

    def sleep(self):
        """General sleep method for all animals"""
        print(f"{self.name} is sleeping.")

    def get_info(self):
        """Return basic information about the animal"""
        return f"Name: {self.name}, Age: {self.age} years"


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color
        self.is_warm_blooded = True  # Mammals are warm-blooded

    def nurse_young(self):
        """Method specific to mammals for nursing their young"""
        print(f"{self.name} is nursing its young.")

    def get_info(self):
        """Override to include fur color and warm-blooded characteristic"""
        return super().get_info() + f", Fur Color: {self.fur_color}, Warm-Blooded: {self.is_warm_blooded}"


class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span  # Wing span in meters
        self.can_fly = True  # Most birds can fly

    def fly(self):
        """Bird-specific method to fly"""
        if self.can_fly:
            print(f"{self.name} is flying with a wingspan of {self.wing_span} meters.")
        else:
            print(f"{self.name} cannot fly.")

    def lay_eggs(self):
        """Bird-specific method for laying eggs"""
        print(f"{self.name} is laying eggs.")

    def get_info(self):
        """Override to include wing span and flying ability"""
        return super().get_info() + f", Wing Span: {self.wing_span} meters, Can Fly: {self.can_fly}"


class Fish(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type  # Type of scales (e.g., smooth, rough)
        self.can_swim = True  # Fish can swim

    def swim(self):
        """Fish-specific method to swim"""
        print(f"{self.name} is swimming.")

    def breathe_underwater(self):
        """Fish-specific method for underwater breathing"""
        print(f"{self.name} is breathing underwater through gills.")

    def get_info(self):
        """Override to include scale type and swimming ability"""
        return super().get_info() + f", Scale Type: {self.scale_type}, Can Swim: {self.can_swim}"


# Example usage
mammal = Mammal(name="Elephant", age=10, fur_color="Gray")
bird = Bird(name="Eagle", age=5, wing_span=2.0)
fish = Fish(name="Shark", age=3, scale_type="Rough")

# Display details and specific behaviors
print(mammal.get_info())
mammal.eat()
mammal.nurse_young()

print(bird.get_info())
bird.fly()
bird.lay_eggs()

print(fish.get_info())
fish.swim()
fish.breathe_underwater()
