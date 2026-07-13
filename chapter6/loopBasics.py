# while and for loop
#print name 100th times

num=0
while num < 100:
    print("suraj")
    num = num+1

#print 1 to 10 number
p =1
while p<=10:
    print(p)
    p += 1

j=10
while j >=0:
    print(j)
    j -= 1

#print even no. 1 to 50 ---
i=1
while (i <=50):
    if(i%2 == 0):
        print(i)
    i +=1

#print sum of n natural number ---
no = 5
sum =0
while (no >=0):
    sum = sum +no
    no -=1
print(sum)


#print right-triangle star pattern ---

rows = 5

# Loop through each row from 1 to rows
for i in range(1, rows + 1):
    # Print '*' repeated 'i' times
    print('* ' * i)


# Write a program to print the multiplication table of any number using a while
# loop.
# (Hint: Start i = 1 and run the loop until i <= 10.)
n= int(input("Enter a number : "))
i =1
while i <=10:
    print(f"{n} * {i} = {n*i}")
    i = i+1