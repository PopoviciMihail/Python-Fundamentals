from abc import ABC, abstractmethod


# --- Multi-level Inheritance ---
# limit to 1 or 2 levels
class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")


class Chicken(Bird):
    pass


# --- Multiple Inheritance ---
# use it properly
# things become complicated when the inherited classes have things in common


# bad example:
class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


class Manager(Employee, Person):
    pass


manager = Manager()
manager.greet()
print(Manager.mro())
print(Manager.__mro__)


# good example
class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass


# --- Abstract class ---
# abstract base classes: provide some common code to its derivatives
# abstract class cannot be instantiated
# need to implement the abstract methods
class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream.")
