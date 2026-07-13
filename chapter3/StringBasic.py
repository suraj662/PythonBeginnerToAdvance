# string - sequence of character
#string - can be represented by 3 form ---
str1 = 'mix'
str2 = "six"
str3 = '''fix'''

print(str1)
print(str2)
print(str3)

#string concatenation
print(str1 + " " + str2)

#length of string
print(len(str1))  #3

#indexing of string
print(str2[2])  #x

#strings are immutable - means string can't be changed directly after value gets assigned
#str1[0] = "a"  #TypeError: 'str' object does not support item assignment
               #bcoz string are immutable