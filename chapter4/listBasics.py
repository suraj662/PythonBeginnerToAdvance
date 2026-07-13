#list - it is a built-in data type that can store multiple values
# in a single variable
#list is mutuable means it can be changed after initialization of value
#list can store different data types

myList = [23, "suraj" , "Developer" , 829116]
food = ["chole bhature" ,"gulab Jamun", "dosa" , "Briyani"]
print(len(food))

#acessing indexing --
print(food[0])
print(food[1])
print(food[2])
print(food[3])

#modifying in list --
#list are changable(mutuable)
food[2] = "barfi"
print(food[2])

#silcing in list --
print(food[1:3])
print(food[ : 4])
print(food[:-1])
print(food[-2:4])
print(food[-3:-1])
print(food[-3:])