# dog.py

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking! Woof woof!")

# Example usage
dog1 = Dog("Max", "Labrador")
dog1.bark()
