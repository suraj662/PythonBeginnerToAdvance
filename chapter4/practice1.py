# take input and print posotive if num is greater than zero and so on

num = int(input("Enter number "))

if(num < 0):
    print("Negative")
elif (num == 0):
    print("Zero")
else:
    print("Positive")