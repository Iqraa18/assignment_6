# custom_exception.py

# Define custom exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be at least 18"):
        self.message = message
        super().__init__(self.message)

# Function that checks age
def check_age(age):
    if age < 18:
        raise InvalidAgeError()  # Raise custom exception
    else:
        print("Access granted. Age is valid.")

# Example usage
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("InvalidAgeError:", e)
