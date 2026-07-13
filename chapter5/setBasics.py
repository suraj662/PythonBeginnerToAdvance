#Sets ----
#sets is an collection of unorderd and unique items .
#sets automatically remove duplicate elements and written using curly braces {}
#sets do not enter duplicate elements

food = {"paneer" , "chicken" , "chole bhature", "sandwich"}
print(type(food))   #<class 'set'>
print(food)

#create empty set ---
emptySet = set()
print(type(emptySet))  #<class 'set'>

#create non-empty set ---
football = {"r7" , "mexi" ,"sunil chettry"}
print(type(football))   #<class 'set'>

#sets are mutuable - only element can be added and removed
#cannot be mutuable like list and dictionary

#adding element in sets---
football.add("pogba")
print(football)

#remove element in set---
football.remove("r7")
print(football)


nums = {1, 2, 3, 4}
# Method C: .pop()
# Description: Removes and returns an ARBITRARY (random) element from the set.
# Because sets are unordered, you cannot control or predict which item gets popped.
popped_val = nums.pop()
print(f"After .pop(): {nums} (Randomly removed item: {popped_val})")


# Method D: .union(set2)
# Description: Combines elements from both sets and returns a NEW set.
# Duplicates are automatically removed in the final collection.
set_a = {1, 2}
set_b = {2, 3}
union_result = set_a.union(set_b)
print(f"Union of {set_a} and {set_b}: {union_result}")  # Output: {1, 2, 3}


# Method E: .intersection(set2)
# Description: Finds and returns a NEW set containing only the elements common to both sets.
set_x = {1, 2, 3}
set_y = {2, 3, 4}
intersection_result = set_x.intersection(set_y)
print(f"Intersection of {set_x} and {set_y}: {intersection_result}")  # Output: {2, 3}


# Method F: .clear()
# Description: Empties the set completely, removing all items.
nums.clear()
print(f"After .clear(): {nums}")  # Output: set() (Represents an empty set)