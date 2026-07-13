#slicing in string gives you access a part of string
#syntax - string[start : end]  end index is excluded

str1 = "helloWorld"
print(str1[0 : 5]) #hello
print(str1[ :5]) #hello
print(str1[3: ]) #loWorld
print(str1[0 : 5 : 2])
print(str1[0 : 5 : 3])

#negative indexing in string --
# "h  e  l  l  0"
# -5 -4 -3  -2 -1

# question on slicing
#take input and print middle 3 charaters , last 2 character

#green 5/2
str ="green"
mid = len(str)//2  #// is a modulus operator
print(mid)
print(str[mid-1:mid+2])

