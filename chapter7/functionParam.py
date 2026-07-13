#Function Parameter ---
def avg(*args):
    if not args:
        return 0

    return sum(args) / len(args)

print(avg(2,3,6,7))

#default function ---
def sum(a=2,b=3):
    print(a+b)

#if we donot pass any parameter value,then it takes argument already defined values
#this is default function calling --
sum()

#write a function ,that print your name and age in a sentence ---
def show(name ,age):
    print(f"{name} is {age} years old")

#show()  error bcoz we didnot not pass any in parameter , it has no values are
#already defined in function
show("suraj" ,24)

#store the function in any variable --
def add(a,b):
    print(a+b)

result = add(5,6)
print("the result is " ,result)

#write a function that return square of that number --
def sq(num):
    return num**2

result = sq(5)
print("the result of square is " ,result)

# Write a function that takes a string and returns the count of vowels and
# consonants separately.
def func(str):
    vowel = "aeiouAEIOU"

    countVowel =0
    countConsnant=0
    for char in str:
        if char.isalpha():
            if char in vowel:
                countVowel += 1
            else:
                countConsnant += 1


    return countVowel , countConsnant

res = func("Suraj Dev Yadav")
print(res)