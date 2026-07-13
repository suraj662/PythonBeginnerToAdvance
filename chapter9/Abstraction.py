# ------------------------------------------------------------------------------
# 4. ABSTRACTION (Forcing a Structure)
# ------------------------------------------------------------------------------
# Abstraction is like a contract. You create a "Base" class that says:
# "Any child class MUST have these specific methods, but I won't write the
# code for them here. The child has to figure it out."
# We use the built-in 'abc' (Abstract Base Class) module for this.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        # We don't write any code here. We just force child classes to have it.
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    # If we forget to write this 'area' method, Python will throw an error!
    def area(self):
        return self.side * self.side

my_square = Square(5)
print(f"Area of square: {my_square.area()}")