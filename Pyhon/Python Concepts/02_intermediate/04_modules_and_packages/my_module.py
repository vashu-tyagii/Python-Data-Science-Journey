# my_module.py
def circle_area(radius):  # type:ignore
    import math

    return math.pi * radius**2 #type:ignore


def greet_user(name): #type:ignore
    return f"Greetings from my_module, {name}!"


if __name__ == "__main__":
    print("This is my_module being run directly.")
    print(f"Area of circle with radius 5: {circle_area(5)}")