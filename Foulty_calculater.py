"""
Author : Yash Soni
Date : 31_Jan_2021
Purpose : Python Learning Purpose
"""
while True:
    try:
        number_1 = int(input("Enter the first number :\n"))
        operator = input(
            "Enter the operation which you want to do on the two numbers :\n")
        number_2 = int(input("Enter the second number :\n"))
        break
    except Exception as e:
        print(e, "You have entered something wrong !! , Try it again.")
        continue
    
if operator == "+":
    if number_1 == 56 and number_2 == 9:
        print("The sum of the two numbers is : ", 77)
    elif number_2 == 56 and number_1 == 9:
        print("The sum of the two numbers is : ", 77)
    else:
        print("The sum of the two numbers is : ", number_1+number_2)
elif operator == "-":
    print("The substraction of the two numbers is : ", number_1-number_2)
elif operator == "/":
    if number_1 == 56 and number_2 == 6:
        print("The sum of the two numbers is : ", 4)
    elif number_2 == 56 and number_1 == 6:
        print("The sum of the two numbers is : ", 4)
    else:
        print("The division of the  of the two numbers is : ", number_1/number_2)
elif operator == "*":
    if number_1 == 45 and number_2 == 3:
        print("The sum of the two numbers is : ", 555)
    elif number_2 == 45 and number_1 == 3:
        print("The sum of the two numbers is : ", 555)
    else:
        print("The multiplication of the  of the two numbers is : ", number_1*number_2)
else:
    print("You have entered wrong operation !!")

