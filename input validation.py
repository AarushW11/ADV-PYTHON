def validate_positive(func):
    def wrapper(*args):
        for i in args:
            if type(i) != int or i <= 0:
                print("Error! All arguments must be positive integers.")
                return
        return func(*args)
    return wrapper


# Function to add numbers
@validate_positive
def add_numbers(a, b):
    print("Sum =", a + b)


# User input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Function call
add_numbers(num1, num2)