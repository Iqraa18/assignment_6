# composition.py

class Engine:
    def start(self):
        print("Engine started!")

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # composition: Car has an Engine

    def start(self):
        print(f"{self.brand} car is ready to go!")
        self.engine.start()  # calling method of Engine class

# Example usage
engine1 = Engine()
car1 = Car("Toyota", engine1)

car1.start()
