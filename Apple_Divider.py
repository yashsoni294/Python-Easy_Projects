while True:
    try:
        Apple_numbers=int(input("Enter the numbers of Apple Harry Potter has got.\n"))
        Range_min=int(input("Enter the min number to check.\n"))
        Range_max=int(input("Enter the max number to check.\n"))
        if Range_min>Range_max:
            print("The minimum number can not be greater then maximum number.")
            continue
        break
    except Exception as e:
        print(f"{e}, You have entered somthing wrong!")
        continue
for i in range(Range_min, Range_max + 1):
    if Range_max == Range_min:
        print("This is not a range and both min and max are equal.")
        if Apple_numbers % i == 0:
            print(f"{i} is divisor of {Apple_numbers}")
            break
        else:
            print(f"{i} is not a divisor of {Apple_numbers}")
            break
    else:
        if Apple_numbers % i == 0:
            print(f"{i} is divisor of {Apple_numbers}")
        else:
            print(f"{i} is not a divisor of {Apple_numbers}")
