from datetime import datetime

# Decorator for logging
def log_function(func):
    def wrapper():
        print("Function Name:", func.__name__)
        print("Called At:", datetime.now().strftime("%H:%M:%S"))
        return func()
    return wrapper


# Function to be logged
@log_function
def greet():
    print("Hello! Welcome to Python.")


# Function call
greet()