"""
Author: Yash Soni
Date: 20-jan-2021
Purpose: Python learning purpose
"""
import random
while True:
    try:
        Star_number=int(input("Enter the First number of your choice.\n "))
        End_number=int(input("Enter the Last number of your choice.\n "))
        if Star_number>=End_number:
            print("Your first number can not ne gr"
                  "eater than your Last number. Please Enter again")
            continue
        else:
            break
    except Exception as e:
        print("You have entered something wrong. Please Enter again ")
        continue
Randum_number=random.randint(Star_number+1,End_number-1)
whose_turn=1
while True:
    if whose_turn%2==0:
        print(f"It's your turn.Please choose"
              f" a number between {Star_number} and {End_number}\n")
        whose_turn=whose_turn+1
        while True:
            try:
                your_choice=int(input())
                if your_choice < Star_number or End_number > End_number:
                    print(f"Choice should be be"
                          f"tween {Star_number} and {End_number} ")
                    continue
                else:
                    break
            except Exception as e:
                print("You have entered something wrong!!")
                continue
        if your_choice < Randum_number:
            print("Choice is less than the winning Number. ")
        elif your_choice > Randum_number:
            print("Choice is Greater than the winning Number. ")
        elif your_choice==Randum_number:
            print("Your Guess is correct and y"
                 "ou won the Game. Congratulations!!")
            print(f"You took {whose_turn//2} Gu"
                  f"esses to Arrive the Winning Number.")
            break
        else:
            continue
    else:
        print(f"It's your friends turn. Your friend have to choose"
              f" a number between {Star_number} and {End_number}\n")
        while True:
            try:
                friends_choice = int(input())
                if friends_choice<Star_number or friends_choice>End_number:
                    print(f"Choice should be be"
                          f"tween {Star_number} and {End_number} ")
                    continue
                else:
                    break
            except Exception as e:
                print("You have entered something wrong!!")
                continue
        whose_turn=whose_turn+1
        if friends_choice<Randum_number:
            print("Choice is less than the winning Number. ")
        elif friends_choice>Randum_number:
            print("Choice is Greater than the winning Number. ")
        elif friends_choice == Randum_number:
            print("Your Friends Guess is correct and"
                  " he has  won the Game. Congratulations to him!!")
            print(f"Your friend took {(whose_turn+1)//2} Gu"
                  f"esses to Arrive the Winning Number.")
            break

        else:
            continue
