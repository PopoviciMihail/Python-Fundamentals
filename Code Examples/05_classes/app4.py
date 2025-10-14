# --- Inheritance ---
# don't repeat yourself
# Animal: Parent, Base
# Mammal: Child, Sub

class Animal:
    def __init__(self):
        print("Animal Contructor")
        self.age = 1

    def eat(self):
        print("eat")



class Mammal(Animal):
    # method overriding = replacing or extending a method defined in the base class
    def __init__(self):
        super().__init__()
        self.weight = 1
        print("Mammal Contructor")

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
print(m.age)
print(m.weight)
print(isinstance(m, Animal))
print(isinstance(m, object))
print(issubclass(Mammal, Animal))

o = object()


# When two or more methods in the same class have the same 
# name but different parameters -> Overloading.
# When the method signature (name and parameters) are the 
# same in the superclass and the child class -> Overriding 
