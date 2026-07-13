# ------------------------------------------------------------------------------
# 3. POLYMORPHISM (Many Forms)
# ------------------------------------------------------------------------------
# This means "same method name, different behavior". If a Child class doesn't
# like how the Parent class does something, it can "override" that method.

class Cat(Animal):
    # The Cat class has the same method name 'bark' wouldn't make sense,
    # but let's override a general 'make_sound' method.

    def make_sound(self):
        print(f"{self.name} says Meow!")

class Duck(Animal):
    def make_sound(self):
        print(f"{self.name} says Quack!")

# Even though they are different animals, we can loop through them and
# call the EXACT SAME method name, and they each know what to do.
animals = [Cat("Whiskers"), Duck("Donald")]
for animal in animals:
    animal.make_sound()