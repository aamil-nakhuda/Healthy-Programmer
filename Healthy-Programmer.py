from pygame import mixer
from datetime import datetime
from time import time

def music_on_loop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        userinput=input()
        if userinput==stopper:
            break

def log(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg}{datetime.now}\n")


init_water= time()
init_eyes= time()
init_exer= time()
water_time=40*60
eyes_time=30*60
exercise_time=45*60

while True:
    if time()- init_water > water_time:
        print("Its time to drink water..! Enter 'drank' to stop")
        music_on_loop("water.mp3","drank")
        init_water=time()
        log("Drank water at ")

    if time()- init_eyes > eyes_time:
        print("Its time to do eye exercises..! Enter 'done eyes' to stop")
        music_on_loop("eyes.mp3","done eyes")
        init_eyes=time()
        log("Done eye exercises at ")

    if time()- init_exer > exercise_time:
        print("Its time to do exercise..! Enter 'done exercises' to stop")
        music_on_loop("exercise.mp3","done exerices")
        init_exer=time()
        log("Done exercise at ")
