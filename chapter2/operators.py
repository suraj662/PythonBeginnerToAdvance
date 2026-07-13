#operator perform operation ---
# ==============================================================================
#                      PYTHON OPERATORS REFERENCE TABLE
# ==============================================================================
#
#  Type                 | Python Syntax            | Description
# ----------------------|--------------------------|----------------------------
#  Arithmetic           | +, -, *, /, %, **, //    | Math tools (+ Power/Floor)
#  Relational           | <, <=, >, >=, ==, !=     | Comparison (Returns True/False)
#  Logical (Lowercase)  | and, or, not             | Combines boolean conditions
#  Bitwise              | &, |, ^, ~, <<, >>       | Binary bit-level logic
#  Assignment           | =, +=, -=, *=, %=, //=   | Stores or updates variables
#  Ternary              | x if condition else y    | Inline conditional check
#  Identity             | is, is not               | Checks exact memory location
#  Membership           | in, not in               | Checks item inside sequence
#
# ==============================================================================


#arithmetic operator ---
x=10
y=20
print(x+y)

#Relational operator ---
print(x <= y)
print(x >= y)
print(x == y)

#Logical operator ---
print(x <y and x <= y)
print(x <y and x >= y)
print(x <y or x <= y)
print(not(x != y))

#Assignment operator ---
a=5
a = a+6
print(a)
#or
a+= 6
print(a)

