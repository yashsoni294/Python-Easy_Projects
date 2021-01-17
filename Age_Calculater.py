while True:
    age=int(input("Please Enter your age or Enter your birth year."))
    if age>2021:
        print("It seem like you are not born yet!! Please enter valid input")
        continue
    if age<150:
        age=age
        Century=100-age
        Century=Century+2021
        print(f"You will turn 100 year's at {Century} ")
        break
    elif age>1900:
        age=2021-age
        Century = 100 - age
        Century = Century + 2021
        print(f"You will turn 100 year's at {Century} ")
        break
    else:
        print("You seem to be the oldest person alive! You should claime for Geniese Wolrd Record!! ")
        continue
print("Would you like to know your age at particualar year of your choice ?")
choice=int(input("Pres 1 for Yes and 0 for No"))
while True:
    if choice==1:
        year=int(input("Please Enter the year you want to know your age."))
        age_will_be=(year-2021)+age
        print(f"You will be {age_will_be} at the year {year}")
        break
    elif choice==0:
        break
    else:
        print("You have enterd something wrong.")
        continue
