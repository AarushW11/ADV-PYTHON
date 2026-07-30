def call_counter(func):
    count = 0

    def wrapper():
        nonlocal count
        count += 1
        print("Function has been called", count, "time(s).")
        return func()

    return wrapper


# Function
@call_counter
def greet():
    print("Hello! Welcome.")


# Function calls
greet()
greet()
greet()