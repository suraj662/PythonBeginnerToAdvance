# Expense Tracker Project
from itertools import count
from unittest import addModuleCleanup

expenseList = [] #list of expenses in form of dictionary
print(" Welcome to Expense Tracker : ")

while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Khrcha")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
  #add expense
    if(choice ==1):
        date = input("kis din kharcha kiya")
        category= input("Kis type ka khrcha kiya? (Food, Travel, Makeup, Books): ")
        description = input("detail about your expense")
        amount = float(input("Enter the amount"))

        expense = {
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }
        expenseList.append(expense)
        print(" \n DONE bro. Expense is added succesfully")

#view all expense
    elif(choice ==2):
        if( len(expenseList) == 0):
            print("No expense is added")
        else:
            print("-----ye hai apka saara expense")
            count =1
            for eachKharcha in expenseList:
                print(f"Kharcha Number {count} -> {eachKharcha["date"]}, {eachKharcha["category"]}, {eachKharcha["description"]}, {eachKharcha["amount"]} ")
                count= count+1

#view total expense
    elif(choice ==3):
        total=0
        for eachKharcha in expenseList:
            total = total + eachKharcha["amount"]

        print("\n TOTAL KHRCHA = ", total)


    elif(choice ==4):
        print("exit the application")
        break


    else:
        print("invalid choice")

