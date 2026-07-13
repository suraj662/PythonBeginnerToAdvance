#Function Basic ----
#block of reusable code that performs a specific task , Instead of writing same lines repeatedly
#we define the function once and use mutiple times
# def keyword used to make function
a=2
b=3
print(a+b)


#instead of this ,we can do this --
def add(a,b):
    return a+b

print(add(3,4))

#no parameter function--
def greet():
    print("Hello Suraj")

greet()
greet()
greet()


#write a function that gives message "Welcome to python programming Suraj" n times --
def wel(n):
    i=1
    while (i<=n):
        print("Welcome to python programming Suraj")
        i=i+1

wel(5)

#why are functions used in programming ?
#to make more readable program
# reduce and help in reducuncy(remove duplicasy)

