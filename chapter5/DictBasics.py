#Dictionary Basics
#It is a built-in DataTypes  stored in unordered and key-value pair format
#Key are unique , cannot be duplicate once after created
#Dictionary is mutuable(can be changed after creation)
#Not allow duplicate key

student = {
    "name" : "Suraj",
    "age" : 24,
    "place": "Bokaro",
    "name": "pawan"
}
print(type(student))  #<class 'dict'>

# Keys - "name" ,"age","place"
#values - "suraj" ,24 ,"Bokaro"

#Acessing values --
#values can acess by using key

#if we created same Key again then it will replace the old value to new value
print(student["name"])   #pawan
print(student)     #{'name': 'pawan', 'age': 24, 'place': 'Bokaro'}

#add new key :value in dictionary ---
student["favSubject"] = "Maths"
print(student)


#remove item in dictionary ---
student.pop("age")
print(student)

# --- 2. INDEXING IN DICTIONARIES ---
# Unlike lists or tuples, dictionaries DO NOT use sequence numbers (0, 1, 2...) for indexing.
# Instead, you index into a dictionary directly using its KEYS.

# Standard Indexing:
student_name = student["name"]
print(f"Name accessed via indexing: {student_name}")

# IMPORTANT WARNING: If you try to index a key that doesn't exist, it crashes with a KeyError:
# print(student["city"])  # This will throw an error and stop execution!


# --- 3. SLICING IN DICTIONARIES? ---
# CRITICAL RULE: Dictionaries CANNOT be sliced.
# Slicing (like my_list[1:4]) relies entirely on an ordered numerical sequence.
# Because dictionaries map keys directly to values via a hash table rather than sequence offsets,
# syntax like student['name':'marks'] is invalid and will throw a TypeError.


# --- 4. DICTIONARY METHODS (FROM THE IMAGE) ---

# Method A: .keys()
# Returns a view object containing all the keys present in the dictionary.
all_keys = student.keys()
print(f"student.keys(): {all_keys}")  # Output: dict_keys(['name', 'age', 'marks', 'course'])


# Method B: .values()
# Returns a view object containing all the values present in the dictionary.
all_values = student.values()
print(f"student.values(): {all_values}")  # Output: dict_values(['Suraj', 24, 85, 'B.Tech'])


# Method C: .items()
# Returns all key-value pairs as a sequence of tuples containing (key, value).
all_items = student.items()
print(f"student.items(): {all_items}")  # Output: dict_items([('name', 'Suraj'), ...])


# Method D: .get(key)
# Returns the value of a key SAFELY. If the key doesn't exist, it returns None
# instead of crashing the program with a KeyError.
safe_name = student.get("name")
safe_city = student.get("city")  # "city" doesn't exist
print(f"student.get('name'): {safe_name}")  # Output: Suraj
print(f"student.get('city'): {safe_city}")  # Output: None (No crash!)


# Method E: .update(new_dict)
# Updates the dictionary with items from another dictionary or an iterable of pairs.
# If a key exists, its value is overwritten; if it's new, it gets added.
student.update({"city": "Lucknow", "marks": 92})
print(f"After .update(): {student}")  # "city" is added, "marks" is changed to 92

