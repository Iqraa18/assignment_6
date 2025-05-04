# aggregation.py

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display(self):
        print(f"Employee: {self.name}, Position: {self.position}")

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # aggregation: Department has a reference to Employee

    def display_info(self):
        print(f"Department: {self.department_name}")
        self.employee.display()  # accessing the Employee's display method

# Example usage
emp1 = Employee("Iqra", "Manager")
dept1 = Department("HR", emp1)

dept1.display_info()
