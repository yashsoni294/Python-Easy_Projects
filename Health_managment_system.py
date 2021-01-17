
def forcopynames():
    print("Press 1 for Harry."
    "Press 2 for Hammad."
    "Press 3 for Rohan.")
    c= int(input())
    return c
def getdate():
    import datetime
    return datetime.datetime.now()
def printstatmt():
    print([getdate()])
    print(d.readlines())
def printlines():
    print("Write the text you want to add on file :-")
    e = input()
    print([getdate()])
    d.write(e)

print("                          ##  Welcome to Health management System  ##")

while True :
    print(" ## If you want to Retrieve data Press 1 OR Press 2 to Locking data ELSE Press 0 for exit the System ##")
    a = int(input())
    if a == 1:
        print("    ##  Press 1 for Retrieve diet or Press 2 for Retrieve work out plan.##")
        b = int(input())
        if b == 1:
            x = forcopynames()
            if x == 1:
                with open("harrydiet.txt", "r") as d:
                    printstatmt()
            elif x == 2:
                with open("hammaddiet.txt", "r") as d:
                    printstatmt()
            elif x == 3:
                with open("rohandiet.txt", "r") as d:
                    printstatmt()
        elif b == 2:
            x = forcopynames()
            if x == 1:
                with open("hammadworkout.txt", "r") as d:
                    printstatmt()
            elif x == 2:
                with open("hammadworkout.txt", "r") as d:
                    printstatmt()
            elif x == 3:
                with open("rohanworkout.txt", "r") as d:
                    printstatmt()
    elif a == 2:
        print("Press 1 for Locking  diet."
              "Press 2 for Locking  work out plan.")
        b = int(input())
        if b == 1:
            x = forcopynames()
            if x == 1:
                with open("harrydiet.txt", "a") as d:
                    printlines()
            elif x == 2:
                with open("hammaddiet.txt", "a") as d:
                    printlines()
            elif x == 3:
                with open("rohandiet.txt", "a") as d:
                    printlines()
        elif b == 2:
            x = forcopynames()
            if x == 1:
                with open("harryworkout.txt", "a") as d:
                    printlines()

            elif x == 2:
                with open("hammadworkout.txt", "a") as d:
                    printlines()
            elif x == 3:
                with open("rohanworkout.txt", "a") as d:
                    printlines()
    elif a==0:
        print("We are exiting our System.")
        break
    else:
        print("You have entered something wrong.")
        continue
print("Thank You.")
                           ## ROHAN DIET PLAN ##
[7:00 AM]- Early Morning:-
                         A glass Traditional egg nog(4 eggs,low fat milk,2 tsp sugar / Soaked almonds + 1 Glass skimmed milk
[9:00 AM]- Breakfast:-
                     Chicken sandwich-4 slices brown bread/ wheat flakes / quinoa with skimmed milk and some nuts
[11:00AM]- Mid Morning:-
                       Buttermilk made from low-fat yogurt / 1 Big bowl of water melon or pineapple + 2 Cheese slices
[1:30 PM]- Lunch:-
                   Fish curry - 1 big cup / 2 Wheat/jowar/bjara chapattis or brown rice+ veggies + bowl of dal + cottage cheese
[6:00 PM]- Enening snack:-
                          Sprouts or boiled legumes with onion , tomato , cucomber , and lime juice + whey with water +cottage cheese
[8:00 PM]- Dinner:-
                   5 Egg white omelet with Asparagus + 4 Toasted brown bread / 2 Wheat/jowar/bajra/chapattis or brown rice + veggies + bowl of dal + cottage cheese

asdfsdkjhg               ## ROHAN WORK OUT PLAN ##
[DAY-1] - LEGS:-
     EXERCISE          SETS         REPS.       REST(MINS.)
1.Barbell squats         4            8               2
2.Leg press              4           25               2
3.Leg curl               5            8               1
4.Lunges                 3          15-20             1
5.Leg extensions         3          15-20             1
6.Seated calf raise      5           12               1
7.Standing claf raise    4          25-30             1
8.Cardio: -Perform for 20 to 25 min.

[DAY-2] - CHEST/ABS:-
     EXERCISE                SETS         REPS.       REST(MINS.)
1.Barbell bench press         4            6               1
2.Inclined dumbell press      4            8               1
3.Flat dumbell flies          4           12               1
4.Dumbell pullovers           4           15               1
5.Push ups                    3         Failure            1
6.Leg raise off bench         3           25              1/2
7.Cable crunches              3           15              1/2
8.Inclined sit ups            3           20              1/2
9.Cardio: -Perform for 20 to 25 min.

[DAY-3] - BACK:-
     EXERCISE                SETS         REPS.       REST(MINS.)
1.Chine up                     4         Failure            1
2.One arm dumbell rows         4           10               1
3.Reverse grip pull downs      4           12               1
4.Barbell power cleans         4            8               1
5.Hyperextensions              4         15-20              1
6.Dumbell side bends           4           20               1
7.Cardio: -Perform for 20 to 25 min.

[DAY-4] - SHOULDERS/ABS:-
     EXERCISE                SETS         REPS.       REST(MINS.)
1.Military press               5            8             2
2.Side laterals                4           10             1
3.Barbell upright rows         4           12             1
4.Bent over laterals           5           12             1
5.Incined sit ups              4          30-50           1
6.Cardio: -Perform for 20 to 25 min.

[DAY-5] - ARMS:-
     EXERCISE                SETS         REPS.       REST(MINS.)
1.Close grip bench press       5            6               2
2.Standing barbell press       5            6               2
3.Skull crunchers              4           10               1
4.Inclined Dumbbell curls      4           10               1
5.Triceps cable press downs    3           15               1
6.Dumbbell concentraction curls 3          15               1
7.Seated calf raise            3           30               1
8.Standing calf raise          3           25               1
9.Cardio: -Perform for 20 to 25 min.

[DAY - 6 AND 7]- REST.               ## HAMMAD WORK OUT PLAN ##
[DAY-1] - LEGS:-
     EXERCISE          SETS         REPS.       REST(MINS.)
1.Barbell squats         4            8               2
2.Leg press              4           25               2
3.Leg curl               5            8               1
4.Lunges                 3          15-20             1
5.Leg extensions         3          15-20             1
6.Seated calf raise      5           12               1
7.Standing claf raise    4          25-30             1
8.Cardio: -Perform for 20 to 25 min.

[DAY-2] - CHEST/ABS:-
     EXERCISE                SETS         REPS.       REST(MINS.)
1.Barbell bench press         4            6               1
2.Inclined dumbell press      4            8               1
3.Flat dumbell flies          4           12               1
4.Dumbell pullovers           4           15               1
5.Push ups                    3         Failure            1
6.Leg raise off bench         3           25              1/2
7.Cable crunches              3           15              1/2
8.Inclined sit ups            3           20              1/2
9.Cardio: -Perform for 20 to 25 min.

[DAY-3] - BACK:-
     EXERCISE                SETS         REPS.       REST(MINS.)
1.Chine up                     4         Failure            1
2.One arm dumbell rows         4           10               1
3.Reverse grip pull downs      4           12               1
4.Barbell power cleans         4            8               1
5.Hyperextensions              4         15-20              1
6.Dumbell side bends           4           20               1
7.Cardio: -Perform for 20 to 25 min.

[DAY-4] - SHOULDERS/ABS:-
     EXERCISE                SETS         REPS.       REST(MINS.)
1.Military press               5            8             2
2.Side laterals                4           10             1
3.Barbell upright rows         4           12             1
4.Bent over laterals           5           12             1
5.Incined sit ups              4          30-50           1
6.Cardio: -Perform for 20 to 25 min.

[DAY-5] - ARMS:-
     EXERCISE                SETS         REPS.       REST(MINS.)
1.Close grip bench press       5            6               2
2.Standing barbell press       5            6               2
3.Skull crunchers              4           10               1
4.Inclined Dumbbell curls      4           10               1
5.Triceps cable press downs    3           15               1
6.Dumbbell concentraction curls 3          15               1
7.Seated calf raise            3           30               1
8.Standing calf raise          3           25               1
9.Cardio: -Perform for 20 to 25 min.

[DAY - 6 AND 7]- REST.
               ## HAMMAD WORK OUT PLAN ##
[DAY-1] - LEGS:-
     EXERCISE          SETS         REPS.       REST(MINS.)
1.Barbell squats         4            8               2
2.Leg press              4           25               2
3.Leg curl               5            8               1
4.Lunges                 3          15-20             1
5.Leg extensions         3          15-20             1
6.Seated calf raise      5           12               1
7.Standing claf raise    4          25-30             1
8.Cardio: -Perform for 20 to 25 min.

[DAY-2] - CHEST/ABS:-
     EXERCISE                SETS         REPS.       REST(MINS.)
1.Barbell bench press         4            6               1
2.Inclined dumbell press      4            8               1
3.Flat dumbell flies          4           12               1
4.Dumbell pullovers           4           15               1
5.Push ups                    3         Failure            1
6.Leg raise off bench         3           25              1/2
7.Cable crunches              3           15              1/2
8.Inclined sit ups            3           20              1/2
9.Cardio: -Perform for 20 to 25 min.

[DAY-3] - BACK:-
     EXERCISE                SETS         REPS.       REST(MINS.)
1.Chine up                     4         Failure            1
2.One arm dumbell rows         4           10               1
3.Reverse grip pull downs      4           12               1
4.Barbell power cleans         4            8               1
5.Hyperextensions              4         15-20              1
6.Dumbell side bends           4           20               1
7.Cardio: -Perform for 20 to 25 min.

[DAY-4] - SHOULDERS/ABS:-
     EXERCISE                SETS         REPS.       REST(MINS.)
1.Military press               5            8             2
2.Side laterals                4           10             1
3.Barbell upright rows         4           12             1
4.Bent over laterals           5           12             1
5.Incined sit ups              4          30-50           1
6.Cardio: -Perform for 20 to 25 min.

[DAY-5] - ARMS:-
     EXERCISE                SETS         REPS.       REST(MINS.)
1.Close grip bench press       5            6               2
2.Standing barbell press       5            6               2
3.Skull crunchers              4           10               1
4.Inclined Dumbbell curls      4           10               1
5.Triceps cable press downs    3           15               1
6.Dumbbell concentraction curls 3          15               1
7.Seated calf raise            3           30               1
8.Standing calf raise          3           25               1
9.Cardio: -Perform for 20 to 25 min.

[DAY - 6 AND 7]- REST.               ## HARRY WORK OUT PLAN ##
[DAY-1] - LEGS:-
     EXERCISE          SETS         REPS.       REST(MINS.)
1.Barbell squats         4            8               2
2.Leg press              4           25               2
3.Leg curl               5            8               1
4.Lunges                 3          15-20             1
5.Leg extensions         3          15-20             1
6.Seated calf raise      5           12               1
7.Standing claf raise    4          25-30             1
8.Cardio: -Perform for 20 to 25 min.

[DAY-2] - CHEST/ABS:-
     EXERCISE                SETS         REPS.       REST(MINS.)
1.Barbell bench press         4            6               1
2.Inclined dumbell press      4            8               1
3.Flat dumbell flies          4           12               1
4.Dumbell pullovers           4           15               1
5.Push ups                    3         Failure            1
6.Leg raise off bench         3           25              1/2
7.Cable crunches              3           15              1/2
8.Inclined sit ups            3           20              1/2
9.Cardio: -Perform for 20 to 25 min.

[DAY-3] - BACK:-
     EXERCISE                SETS         REPS.       REST(MINS.)
1.Chine up                     4         Failure            1
2.One arm dumbell rows         4           10               1
3.Reverse grip pull downs      4           12               1
4.Barbell power cleans         4            8               1
5.Hyperextensions              4         15-20              1
6.Dumbell side bends           4           20               1
7.Cardio: -Perform for 20 to 25 min.

[DAY-4] - SHOULDERS/ABS:-
     EXERCISE                SETS         REPS.       REST(MINS.)
1.Military press               5            8             2
2.Side laterals                4           10             1
3.Barbell upright rows         4           12             1
4.Bent over laterals           5           12             1
5.Incined sit ups              4          30-50           1
6.Cardio: -Perform for 20 to 25 min.

[DAY-5] - ARMS:-
     EXERCISE                SETS         REPS.       REST(MINS.)
1.Close grip bench press       5            6               2
2.Standing barbell press       5            6               2
3.Skull crunchers              4           10               1
4.Inclined Dumbbell curls      4           10               1
5.Triceps cable press downs    3           15               1
6.Dumbbell concentraction curls 3          15               1
7.Seated calf raise            3           30               1
8.Standing calf raise          3           25               1
9.Cardio: -Perform for 20 to 25 min.

[DAY - 6 AND 7]- REST.
               ## HARRY WORK OUT PLAN ##
[DAY-1] - LEGS:-
     EXERCISE          SETS         REPS.       REST(MINS.)
1.Barbell squats         4            8               2
2.Leg press              4           25               2
3.Leg curl               5            8               1
4.Lunges                 3          15-20             1
5.Leg extensions         3          15-20             1
6.Seated calf raise      5           12               1
7.Standing claf raise    4          25-30             1
8.Cardio: -Perform for 20 to 25 min.

[DAY-2] - CHEST/ABS:-
     EXERCISE                SETS         REPS.       REST(MINS.)
1.Barbell bench press         4            6               1
2.Inclined dumbell press      4            8               1
3.Flat dumbell flies          4           12               1
4.Dumbell pullovers           4           15               1
5.Push ups                    3         Failure            1
6.Leg raise off bench         3           25              1/2
7.Cable crunches              3           15              1/2
8.Inclined sit ups            3           20              1/2
9.Cardio: -Perform for 20 to 25 min.

[DAY-3] - BACK:-
     EXERCISE                SETS         REPS.       REST(MINS.)
1.Chine up                     4         Failure            1
2.One arm dumbell rows         4           10               1
3.Reverse grip pull downs      4           12               1
4.Barbell power cleans         4            8               1
5.Hyperextensions              4         15-20              1
6.Dumbell side bends           4           20               1
7.Cardio: -Perform for 20 to 25 min.

[DAY-4] - SHOULDERS/ABS:-
     EXERCISE                SETS         REPS.       REST(MINS.)
1.Military press               5            8             2
2.Side laterals                4           10             1
3.Barbell upright rows         4           12             1
4.Bent over laterals           5           12             1
5.Incined sit ups              4          30-50           1
6.Cardio: -Perform for 20 to 25 min.

[DAY-5] - ARMS:-
     EXERCISE                SETS         REPS.       REST(MINS.)
1.Close grip bench press       5            6               2
2.Standing barbell press       5            6               2
3.Skull crunchers              4           10               1
4.Inclined Dumbbell curls      4           10               1
5.Triceps cable press downs    3           15               1
6.Dumbbell concentraction curls 3          15               1
7.Seated calf raise            3           30               1
8.Standing calf raise          3           25               1
9.Cardio: -Perform for 20 to 25 min.

[DAY - 6 AND 7]- REST.kjh
                           ## HAMMAD DIET PLAN ##
[7:00 AM]- Early Morning:-
                         A glass Traditional egg nog(4 eggs,low fat milk,2 tsp sugar / Soaked almonds + 1 Glass skimmed milk
[9:00 AM]- Breakfast:-
                     Chicken sandwich-4 slices brown bread/ wheat flakes / quinoa with skimmed milk and some nuts
[11:00AM]- Mid Morning:-
                       Buttermilk made from low-fat yogurt / 1 Big bowl of water melon or pineapple + 2 Cheese slices
[1:30 PM]- Lunch:-
                   Fish curry - 1 big cup / 2 Wheat/jowar/bjara chapattis or brown rice+ veggies + bowl of dal + cottage cheese
[6:00 PM]- Enening snack:-
                          Sprouts or boiled legumes with onion , tomato , cucomber , and lime juice + whey with water +cottage cheese
[8:00 PM]- Dinner:-
                   5 Egg white omelet with Asparagus + 4 Toasted brown bread / 2 Wheat/jowar/bajra/chapattis or brown rice + veggies + bowl of dal + cottage cheese

                           ## HARRY DIET PLAN ##
[7:00 AM]- Early Morning:-
                          A fruit of your choice + whey protein / Soaked almonds + 1 Glass skimmed milk
[9:00 AM]- Breakfast:-
                     A bowl of oats / wheat flakes / quinoa with skimmed milk and some nuts
[11:00AM]- Mid Morning:-
                         Buttermilk made from low-fat yogurt / 1 Big bowl of water melon or pineapple + 2 Cheese slices
[1:30 PM]- Lunch:-
                   2 Wheat/jowar/bjara chapattis or brown rice+ veggies + bowl of dal + cottage cheese
[6:00 PM]- Enening snack:-
                          Sprouts or boiled legumes with onion , tomato , cucomber , and lime juice + whey with water +cottage cheese
[8:00 PM]- Dinner:-
                   2 Wheat/jowar/bajra/chapattis or brown rice + veggies + bowl of dal + cottage cheese
