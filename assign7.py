# employee.py

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name           # public
        self._salary = salary      # protected
        self.__ssn = ssn           # private

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")  # Accessing private variable inside the class

# Example usage
emp = Employee("Iqra", 100000, "123-45-6789")

# Accessing public variable
print("Public:", emp.name)

# Accessing protected variable (allowed but discouraged)
print("Protected (convention):", emp._salary)

# Accessing private variable (will raise an error)
try:
    print("Private:", emp.__ssn)
except AttributeError as e:
    print("Private:", e)

# Access through a method
emp.show_info()
