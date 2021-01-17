var1=int(input("Enter the 1st No.:"))
var2=input("Enter operation :")
var3=int(input("Enter the 2st No.:"))
if var2=="+":
    if var1 == 56 and var3 == 9:
        print(77)
    else:
        print(var1 + var3)
elif var2=="-":
    print(var1-var3)
elif var2=="*":
    if var1==45 and var3==3:
        print(555)
    else:
        print(var1*var3)

elif var2=="/":
    if var1 == 56 and var3 == 6:
        print(4)
    else:
        print(var1 /var3)
else:
    print("Something went wrong. Try again!")
