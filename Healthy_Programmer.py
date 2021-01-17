import time,datetime
import pygame
n=0
p=0
w=0
a=1
b=1
c=1
def waterplay():
    global a
    a=a+1
    global n
    n=n+1
    pygame.mixer.init()
    pygame.mixer.music.load("The_Water_Song(256kbps).mp3")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()
    while True:
        print(" Please type 'Done' to stop the song")
        q = input(" ")
        q = q.upper()
        if q == 'DONE':
            pygame.mixer.music.stop()
            with open("water.txt", 'a') as f:
                f.write(f"\n {n}. {datetime.datetime.now()} :Drank water")
                break
        else:
            print("You have entered something wrong!")
            continue
def eyeex():
    global b
    b=b+1
    global p
    p=p+1
    pygame.mixer.init()
    pygame.mixer.music.load("Nainowale_Ne_Full_Video_Song___Padmaavat___Deepika_Padukone___Shahid_Kapoor___Ranveer_Singh(256kbps).mp3")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()
    while True:
        print(" Please type 'Done' to stop the song")
        q = input(" ")
        q = q.upper()
        if q == 'DONE':
            pygame.mixer.music.stop()
            with open("eyes.txt", 'a') as f:
                f.write(f"\n {p}. {datetime.datetime.now()} :Eye exercise done")
            break
        else:
            print("You have entered something wrong!")
            continue
def Exercise():
    global c
    c=c+1
    global w
    w=w+1
    pygame.mixer.init()
    pygame.mixer.music.load("_Chak_Lein_De__Chandni_Chowk_To_China__Akshay_Kumar,_Deepika_Padukone__Kailash_Kher(256kbps).mp3")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()
    while True:
        print("Please type 'Done' to stop the song")
        q = input(" ")
        q = q.upper()
        if q == 'DONE':
            pygame.mixer.music.stop()
            with open("physicalexercise.txt", 'a') as f:
                f.write(f"\n {w}. {datetime.datetime.now()} :Physical Exercise Done ")
            break
        else:
            print("You have entered something wrong!")
            continue
print("                            ## Healthy Programmer ##")
timer_stop = datetime.datetime.utcnow()
while True:
        if datetime.datetime.utcnow() - timer_stop > datetime.timedelta(minutes=25*a):
            print("Its Drinking Time.\n# Now You have to drink water.")
            waterplay()
        if datetime.datetime.utcnow() - timer_stop > datetime.timedelta(minutes=30*b):
            print("Its Eye Exercise Time.\n# Now do some eye exercises.")
            eyeex()
        if datetime.datetime.utcnow() - timer_stop > datetime.timedelta(minutes=45*c):
            print("Its Physical Exercise Time.\n# Now you have to do some physical Exercise. ")
            Exercise()
        continue
