# Inheritance
class Animal:
    def __init__(self, name):  # type:ignore
        self.name = name

    def speak(self):  # type:ignore
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        return f"{self.name} barks."


class Cat(Animal):  # Cat inherits from Animal
    def speak(self):
        return f"{self.name} meows."


my_animal = Dog("Rex")
print(my_animal.speak())

another_animal = Cat("Whiskers")
print(another_animal.speak())