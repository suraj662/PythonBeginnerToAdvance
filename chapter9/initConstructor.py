#Init Constructor ---

# ==============================================================================
#                  THE __init__ CONSTRUCTOR IN PYTHON: A GUIDE
# ==============================================================================
# In Python, Object-Oriented Programming (OOP) uses "Classes".
# Think of a Class as a BLUEPRINT (like a blueprint for a house).
# An Object (or Instance) is the ACTUAL HOUSE built from that blueprint.
#
# The __init__ method is the "Constructor".
# It is a special function that runs AUTOMATICALLY the exact moment you
# create a new object. It "initializes" (sets up) the object's starting state.
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. THE BASICS: CREATING A CLASS WITH __init__
# ------------------------------------------------------------------------------
class VideoGameCharacter:

    # The __init__ method always has double underscores on both sides (called "dunder").
    # The first parameter must ALWAYS be 'self'.
    # 'self' is Python's way of saying "the specific object we are building right now".

    def __init__(self, name, character_class, starting_health):

        # Here, we are attaching the data passed in to the specific object (self)
        self.name = name
        self.role = character_class
        self.health = starting_health
        self.level = 1  # We can also set default values that don't need to be passed in!

        # You can even make it do things immediately when created
        print(f"--> {self.name} has entered the game!")


# ------------------------------------------------------------------------------
# 2. BRINGING IT TO LIFE (Creating Objects)
# ------------------------------------------------------------------------------
# Notice we DO NOT call __init__ directly!
# Just calling the Class name triggers __init__ automatically behind the scenes.
# Also notice we don't pass anything for 'self' — Python handles 'self' automatically.

player_1 = VideoGameCharacter("Aragorn", "Ranger", 100)
player_2 = VideoGameCharacter("Gandalf", "Wizard", 80)


# ------------------------------------------------------------------------------
# 3. PROVING THAT 'self' WORKS
# ------------------------------------------------------------------------------
# Because of 'self' inside the __init__ method, player_1 and player_2
# safely hold their own unique data without mixing it up.

print("\n--- Player Stats ---")
print(f"Player 1: {player_1.name} | Role: {player_1.role} | HP: {player_1.health}")
print(f"Player 2: {player_2.name} | Role: {player_2.role} | HP: {player_2.health}")


# ==============================================================================
# QUICK SUMMARY:
# 1. __init__ runs automatically when you create a new object.
# 2. 'self' is required as the first parameter. It points to the object being created.
# 3. Use self.variable_name to store data safely inside that specific object.
# 4. It saves you from having to create an empty object and set variables manually later.
# ==============================================================================