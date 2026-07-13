#list method ---
marks1 = [23 , 12, 24 ,89, 90]
print(marks)

marks1[2] = 56
print(marks1)

#max method --
print(max(marks1))

#min method --
print(min(marks1))

#len method -- for length
print(len(marks1))


# ==========================================
# UNDERSTANDING PYTHON LIST METHODS
# ==========================================

# Initializing a sample list to match the "marks" example from the image
marks = [75, 64, 85, 92, 64]
print(f"Original list: {marks}\n")

# --- 1. .append(el) ---
# Description: Adds an element directly to the very end of the list.
# Modifies the list in-place and increases its length by 1.
marks.append(99)
print(f"After .append(99): {marks}")  # Output will have 99 at the end


# --- 2. .insert(i, el) ---
# Description: Inserts an element 'el' at a specific index position 'i'.
# All subsequent elements are shifted to the right.
marks.insert(1, 80)
print(f"After .insert(1, 80): {marks}")  # 80 is now at index 1


# --- 3. .remove(el) ---
# Description: Searches for and removes the FIRST occurrence of the specified element 'el'.
# If the element appears multiple times (like 64 here), only the first one is deleted.
marks.remove(64)
print(f"After .remove(64): {marks}")  # The first 64 is gone


# --- 4. .pop(i) ---
# Description: Removes and returns the element at the specified index 'i'.
# Note: If no index is provided (e.g., marks.pop()), it removes the last item.
removed_element = marks.pop(2)
print(f"After .pop(2): {marks} (Removed element: {removed_element})")


# --- 5. .sort() ---
# Description: Sorts the list permanently in ascending order (smallest to largest).
marks.sort()
print(f"After .sort(): {marks}")


# --- 6. .reverse() ---
# Description: Reverses the current order of the elements in the list permanently.
marks.reverse()
print(f"After .reverse(): {marks}")