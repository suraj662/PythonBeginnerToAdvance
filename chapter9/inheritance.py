# ------------------------------------------------------------------------------
# 2. INHERITANCE (Sharing Code: Parent and Child Classes)
# ------------------------------------------------------------------------------
# A Child class automatically gets all the variables and methods of its Parent.
# This prevents you from copying and pasting the same code over and over.

# The Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating food.")

# The Child Class (Notice 'Animal' is inside the parentheses)
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")

# The dog gets both its own bark() method AND the parent's eat() method!
my_dog = Dog("Rex")
my_dog.eat()   # Inherited from Animal
my_dog.bark()  # Defined in Dog