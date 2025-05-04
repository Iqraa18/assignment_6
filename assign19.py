class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, num):
        return num * self.factor  # Multiply input by the factor

# Example usage
multiplier = Multiplier(5)  # Create a multiplier object with factor 5

# Test using callable()
print(callable(multiplier))  # Check if the object is callable (True)

# Test by calling the object like a function
result = multiplier(6)  # This calls the __call__() method
print("Result:", result)
