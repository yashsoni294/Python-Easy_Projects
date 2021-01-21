"""
Author:Yash Soni
Date: 21_Jan_2021
Purpose: Python Learning
"""
import re
from collections import Counter
print("                      ## Welcome to Search Engine. ##")
Search_list=["what is my ip","what time is it","how to register to vote",
             "how to tie a tie",
             "can you run it","what song is this","how to lose weight",
             "how many ounces in a cup",
             "how to get pregnant","how to make pancakes",
             "where are you now","how to lose weight fast",
             "how old is donald trump","how to screenshot on mac",
             "how to download youtube videos",
             "can i run it","python is the best language ever python"]
User_query=input("Enter what you are searching for :\n")
User_query=User_query.lower()
User_query_List=User_query.split(" ")
lst=[]
n=0
for i in Search_list:
    i=i.lower()
    for a in User_query_List:
        match_list=re.findall(a,i)
        if len(match_list)!=0:
            lst.append(n)
    n+=1
lst=[key for key ,value in Counter(lst).most_common()]
print(f"From Your search, {len(lst)} results found. ")
numb=1
for i in lst:
    print(f"{numb}.\"{Search_list[i]}\"\n")
    numb+=1
