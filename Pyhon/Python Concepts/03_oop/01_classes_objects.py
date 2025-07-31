# Classes and Objects
class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):  # type:ignore
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

    def bark(self):
        return f"{self.name} says Woof!"

    def describe(self):
        return f"{self.name} is {self.age} years old."


# Create objects (instances)
my_dog = Dog("Buddy", 3)
your_dog = Dog("Lucy", 5)

print(my_dog.describe())
print(my_dog.bark())
print(f"Buddy's species: {my_dog.species}")

print(your_dog.describe())
print(f"Lucy's species: {your_dog.species}")