while True:
    try:
        Elements=input("Enter the elements of the list which you want to invert.")
        List = Elements.split(",")
        a = 0
        for i in List:
            List[a] = int(i)
            a += 1
        break
    except Exception as e:
        print("You have not entered the elements with comma(,). Please rewrite the"
              " elements with comma(,)")
        continue
print(f"The list which you have enterd is as:\n{List}")
print("1. The inverted list using Inbuilt Method of given list is :")
List.reverse()
print(List)
List.reverse()
print("2. The inverted list using [::-1]/Slicing Method of given list is :")
List=List[::-1]
print(List)
List=List[::-1]
n=0
sub=1
if len(List)%2==0:
    ln=len(List)
else:
    ln=len(List)-1
while n<ln/2:
    List[n]=List[n]+List[len(List)-sub]
    List[len(List) - sub]=List[n]-List[len(List)-sub]
    List[n]=List[n]-List[len(List)-sub]
    n=n+1
    sub=sub+1
print("3. The inverted list after Swapping first element with last one and "
      "\nsecond element with second last one and so no .... of given list is :")
print(List)
