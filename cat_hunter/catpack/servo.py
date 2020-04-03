from gpiozero import AngularServo
from gpiozero import Button
from time import sleep
import random

x = AngularServo(3, min_angle=-90, max_angle=90)

# lower is quicker for speed
speed = 0.4
# number of direction changes
length = 10

def twitch():
    for i in range(length):
        x.angle= random.randrange(-90,90)
        sleep(speed)
        x.detach()

twitch()
#         
#         
#     x.angle= random.randrange(-90,90)
#     sleep(dur)
#     x.angle = random.randrange(-90,90)
#     sleep(dur)
#     x.angle = random.randrange(-90,90)
#     sleep(dur)
#     x.angle=random.randrange(-90,90)
#     sleep(dur)
#     x.angle = random.randrange(-90,90)
#     sleep(dur)
#     x.angle = random.randrange(-90,90)
#     sleep(dur)
#     x.angle= random.randrange(-90,90)
#     sleep(dur)
#     x.angle = random.randrange(-90,90)
#     sleep(dur)
#     x.angle = random.randrange(-90,90)
#     sleep(dur)
#     x.angle=random.randrange(-90,90)
#     sleep(dur)
#     x.angle = random.randrange(-90,90)
#     sleep(dur)
#     x.angle = random.randrange(-90,90)


    
    


        

