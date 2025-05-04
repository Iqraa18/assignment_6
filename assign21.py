# countdown.py

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # Return the iterator object

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # Stop iteration when below 0
        value = self.current
        self.current -= 1
        return value

# Example usage
count = Countdown(8)

for number in count:
    print(number)
