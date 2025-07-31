# main.py
import my_module
from my_module import greet_user  # type:ignore
import math  # Built-in module

area = my_module.circle_area(7)  # type:ignore
print(f"Area using my_module: {area}")

greeting = greet_user("Charlie")
print(greeting)

print(f"Square root of 16: {math.sqrt(16)}")