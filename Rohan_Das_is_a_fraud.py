"""
Author: Yash Soni
Date: 21_Jan_2021
Purpose: Python Learning purpose
"""
import random
def rohanMultiplication(number):
    randem_add_number=random.randint(5,8)
    randem_index=random.randint(2,8)
    table_list=[]
    increament=0
    for i in range(10):
        table_list.append(number+increament)
        increament += number
    table_list[randem_index]=table_list[randem_index] +randem_add_number
    return table_list
def isCorrect(table):
    n=1
    for i in table:
        whole_no=i/table[0]
        if whole_no==n:
            n+=1
            continue
        else:
            print(f"The table given by Rohan is not correct.\n"
                  f"{i} is wrong there should be {n*table[0]}.\n"
                  f"Hence rohan das is a fraud Guy!! ")
            break
if __name__ == '__main__':
    table=rohanMultiplication(int(input("Enter the to get its table:\n")))
    print(table)
    isCorrect(table)
