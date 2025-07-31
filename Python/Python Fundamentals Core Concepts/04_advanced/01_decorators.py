# Decorators
def my_decorator(func):  # type:ignore
    def wrapper(*args, **kwargs):  # type:ignore
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)  # type:ignore
        print("Something is happening after the function is called.")
        return result  # type:ignore

    return wrapper  # type:ignore


@my_decorator
def say_hello(name):  # type:ignore
    print(f"Hello, {name}!")
    return "Greeting Complete"


@my_decorator
def calculate_sum(a, b):  # type:ignore
    return a + b  # type:ignore


say_hello("World")
sum_result = calculate_sum(10, 20)  # type:ignore
print(f"Calculated sum: {sum_result}")