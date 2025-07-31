# Functions
def greet(name="Guest"):  # type:ignore
    """This function greets the given name."""
    return f"Hello, {name}!"


print(greet("Alice"))
print(greet())  # Uses default argument


def add_numbers(a, b):  # type:ignore
    return a + b  # type:ignore


result = add_numbers(5, 7)
print(f"Sum: {result}")


def many_args(*args, **kwargs):  # type:ignore
    print("Positional args:", args)  # type:ignore
    print("Keyword args:", kwargs)  # type:ignore


many_args(1, 2, 3, name="Bob", age=30)