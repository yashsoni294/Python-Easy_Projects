user="asd"
computer="as"
import random
def computerchoice():
      choic = ["Snake", "Water", "Gun"]
      global computer
      computer = random.choice(choic)
      print("computer's choice is :-",computer)
      return computer
def userchoice():
      print("Choose from the following :-")
      print("# Snake:-Press S ")
      print("# Water:-Press W ")
      print("# Gun  :-Press G ")
      global user
      user = str(input())
      return user
print("             ##   Welcome You to Snake Game   ##")
print("In this Game you have to choose from three things as "
      "1.Sanke ,2.Water ,or 3.Gun, and computer will also choose any from this three "
      "who will more in 10 times will be declared as Winner!  ")
print("Be ready!")
u=0
c=0
cnt=0
while cnt<=9:
      userchoice()
      computerchoice()
      if user == "s" and computer== "Water":
            u = u + 1
      elif user== "w" and computer=="Water":
            u = u + 1
            c = c + 1
      elif user== "g" and computer == "Water":
            c = c + 1
      elif user == "s" and computer =="Snake":
            u = u+1
            c = c+1
      elif user == "w" and computer =="Snake":
            c = +1
      elif user == "g" and computer=="Snake":
            u = u+1
      elif user == "s" and computer =="Gun":
            c = c+1
      elif user == "w" and computer== "Gun":
            u = u+1
      elif user == "g" and computer =="Gun":
            c = c+1
            u = u+1
      cnt=cnt+1
if u>c:
      print("Your score is :",u )
      print("Computers  score is :",c)
      print(" congrates!! You won the Game")
else:
      print("Your score is :", u)
      print("Computers  score is :", c)
      print(" Oops!! You lost the Game")

