#conditional statement ---

mark = int(input("Enter mark : "))

if mark >= 90:
    print("A grade")
elif mark >= 80:
    print("B grade")
elif mark >= 70:
    print("B2 grade")
elif mark <= 70:
    print("C grade")

age = int(input("Enter age : "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")