# logger.py

class Logger:
    def __init__(self):
        print("Logger object created.")

    def __del__(self):
        print("Logger object destroyed.")

# Example usage
logger1 = Logger()

# Manually deleting the object to trigger destructor
del logger1
