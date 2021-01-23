"""
Author: Yash Soni
Date: 23_Jan_2021
Purpose: Python Learning Purpose
"""
import random
def Random_generaotr(new_list):
    while True:
        Random=random.randint(1,len(new_list))
        if Random%2!=0:
            Surname=Random
            break
        else:
            continue
    return Surname
if __name__ == '__main__':
    num_friends=int(input("Please enter the Numbers of your Friends :\n"))
    name_list=[]
    for i in range(num_friends):
        name_list.append(input(f"{i+1}. Please enter the name of your friend: \n"))
    list=[]
    new_list=[]
    for name in name_list:
        list=name.split(" ")
        for i in list:
            new_list.append(i)
    print(new_list)
    a=0
    surname_list=[]
    print("Your friends funny names are as follows: ")
    for i in range(num_friends):
        if i==0:
            surname = Random_generaotr(new_list)
            pass
        else:
            surname = Random_generaotr(new_list)
            for x in surname_list:
                if x==new_list[surname]:
                    surname = Random_generaotr(new_list)
                    continue
        print(f"{new_list[0+a]} {new_list[surname]}")
        surname_list.append(new_list[surname])
        a+=2
