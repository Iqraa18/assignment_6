# class_decorators.py

def add_greeting(cls):
    cls.greet = lambda self: "Hello from Decorator!"  # Adding greet method to the class
    return cls

@add_greeting  # Applying the decorator
class Person:
    def __init__(self, name):
        self.name = name

# Example usage
person1 = Person("Iqra")
print(person1.greet())  # Calling the dynamically added greet method
