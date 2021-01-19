print("                      ## Welcome to The Next Palindrome ## ")
def Reversing_Number(integr):
    rev = 0
    while integr > 0:
        lm = integr % 10
        rev = rev * 10 + lm
        integr = integr // 10
    return rev
test_number=int(input("Enter the number of test you want to test.\n"))
List_of_Number=[]
for i in range(test_number):
    number=int(input(f"Enter the {i+1} number:\n"))
    List_of_Number.append(number)
n=1
for a in List_of_Number:
    b=0
    while True:
        rev=a+b
        b=b+1
        if rev == Reversing_Number(rev):
            print(f"The next Palindrome of the  number {a} is: {rev}")
            break
        else:
            continue
