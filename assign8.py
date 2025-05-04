# teacher.py

class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person initialized with name: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # calling the base class constructor
        self.subject = subject
        print(f"Teacher initialized with subject: {self.subject}")

# Example usage
t1 = Teacher("Iqra", "Math")
