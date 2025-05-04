# shape.py

from abc import ABC, abstractmethod

class Shape(ABC):  # abstract base class
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Example usage
rect = Rectangle(9, 10)
print("Area of rectangle:", rect.area())
