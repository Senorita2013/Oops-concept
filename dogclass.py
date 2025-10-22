class Dog:
    animal = "Dog"

    def __init__(self,breed,colour):
        self.breed = breed
        self.colour = colour

    def display_details(self):
        print(f"Animal:{Dog.animal}")
        print(f"Breed:{self.breed}")
        print(f"Colour:{self.colour}")
        print("-"*30)

dog1 = Dog("Labrador","Golden")
dog2 = Dog("German Sheperd","Black and Tan")

dog1.display_details()
dog2.display_details()