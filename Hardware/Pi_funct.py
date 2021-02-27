from time import sleep
import RPi.GPIO as GPIO
from picamera import PiCamera

#########################################
############### ROBOT ARM ###############
#########################################

####################################
############### INIT ###############
####################################
GPIO.setmode(GPIO.BCM)

###### ARM ######
servoPIN = 27
GPIO.setup(servoPIN, GPIO.OUT)

arm = GPIO.PWM(servoPIN, 50) # GPIO 27 for PWM with 50Hz
arm.start(2.5) # Initialization

###### BASE ######
servo2PIN = 17
GPIO.setup(servo2PIN, GPIO.OUT)

base = GPIO.PWM(servo2PIN, 50) # GPIO 17 for PWM with 50Hz
base.start(2.5) # Initialization

###### VALVE ######
valvePIN = 22
GPIO.setup(valvePIN, GPIO.OUT)

####################################
############## ANGLES ##############
####################################
#(angle/18)+2
#maximal angles : U2 - D5 & L11 - C7 - R3
up = 2.2 
down = 5

left = 11
center = 7
right = 3

####################################
############# Movement #############
####################################
def bLeft():
    i = center
    while i < left:
        base.ChangeDutyCycle(i)
        print(i)
        sleep(.1)
        i += 0.1
    sleep(2)   
def bCenter():
    base.ChangeDutyCycle(center)
    sleep(2)
def bRight():
    i = center
    while i > right:
        base.ChangeDutyCycle(i)
        print(i)
        sleep(.1)
        i -= 0.1
    sleep(2)

def aDown():
    arm.ChangeDutyCycle(down)
    sleep(4)
def aUp():
    i = down
    while i > up:
        arm.ChangeDutyCycle(i)
        print(i)
        sleep(.1)
        i -= 0.1
    sleep(2)


def valveON():
    GPIO.output(valvePIN, 1)
    sleep(3)

def valveOFF():
    GPIO.output(valvePIN, 0)
    sleep(3)


##########################################
############### Pi CAMERA  ###############
##########################################

camera = PiCamera()

def takePic(numb):
    camera.start_preview()
    sleep(1)
    for i in range(numb):
        camera.capture('/home/pi/Desktop/img/image%s.jpg' %i)
    sleep(1)
    camera.stop_preview()