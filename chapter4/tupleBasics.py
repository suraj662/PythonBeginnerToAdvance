#Tuple ---
#same like list but it is immutuable(can't be changed after creation)
#Syntax -- myTuple = (12,13 ,45,78)

# ==============================================================================
# UNDERSTANDING TUPLES IN PYTHON
# ==============================================================================
# A Tuple is a built-in data type in Python used to store collections of data.
# Key Characteristics:
# 1. Ordered: The items have a defined order that will not change.
# 2. Immutable: Once a tuple is created, you CANNOT change, add, or remove items.
# 3. Allows Duplicates: It can hold identical values.
# 4. Syntax: Written with round brackets () instead of square brackets [].
# ==============================================================================

# --- 1. CREATING A TUPLE ---
# You define a tuple by placing elements inside parentheses.
my_tuple = ("apple", "banana", "cherry", "apple", "date")
print("Original Tuple:", my_tuple)

# CRITICAL EDGE CASE: Creating a tuple with only ONE item requires a trailing comma.
single_item_tuple = ("apple",)  # Without the comma, Python sees this just as a string.


# --- 2. TUPLE INDEXING ---
# Indexing allows you to access a specific item based on its position (starting at 0).
# Negative indexing starts from the end (-1 is the last item).

#  Indices:      [0]        [1]       [2]        [3]       [4]
#  Neg Indices:  [-5]       [-4]      [-3]       [-2]      [-1]
#  Values:     "apple"   "banana"  "cherry"   "apple"    "date"

print("First item (index 0):", my_tuple[0])       # Output: apple
print("Third item (index 2):", my_tuple[2])       # Output: cherry
print("Last item (index -1):", my_tuple[-1])      # Output: date


# --- 3. TUPLE SLICING ---
# Slicing allows you to extract a specific portion (sub-tuple).
# Syntax: tuple[start_index : end_index] -> Note: 'end_index' is EXCLUDED.

# Slice from index 1 up to (but not including) index 4
print("Slice [1:4]:", my_tuple[1:4])  # Output: ('banana', 'cherry', 'apple')

# Shortcut: Omitting start means "start from the beginning"
print("Slice [:3]:", my_tuple[:3])    # Output: ('apple', 'banana', 'cherry')

# Shortcut: Omitting end means "go all the way to the end"
print("Slice [2:]:", my_tuple[2:])    # Output: ('cherry', 'apple', 'date')

# Negative slicing
print("Slice [-3:-1]:", my_tuple[-3:-1])  # Output: ('cherry', 'apple')


# --- 4. TUPLE METHODS ---
# Because tuples are immutable, they only have TWO built-in methods.
# They do not have methods like append(), insert(), pop(), or remove().

# Method A: .count(value)
# Counts the total number of times a specific value appears in the tuple.
apple_count = my_tuple.count("apple")
print("Count of 'apple':", apple_count)  # Output: 2

# Method B: .index(value)
# Finds the FIRST index position where the specified value occurs.
# Throws a ValueError if the item is not found.
banana_index = my_tuple.index("banana")
print("First index of 'banana':", banana_index)  # Output: 1


# --- 5. IMMUTABILITY DEMONSTRATION ---
# Un-commenting the line below will throw a TypeError because you cannot modify a tuple:
# my_tuple[0] = "blueberry"

