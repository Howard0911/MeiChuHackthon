import RPi.GPIO as GPIO
import pigpio
import time

PwmLeftPin = 12 # 32
PwmRightPin = 13 # 33
LeftForward = 16 # 36
LeftBackward = 20 # 38
RightForward = 19 #35
RightBackward = 26 #37
EnablePin = 23 #Rpi 16
PWM_FREQ = 800

#pi = pigpio.pi()
GPIO.setmode(GPIO.BCM)
GPIO.setup(EnablePin, GPIO.OUT)
GPIO.setup(LeftForward, GPIO.OUT)
GPIO.setup(LeftBackward, GPIO.OUT)
GPIO.setup(RightForward, GPIO.OUT)
GPIO.setup(RightBackward, GPIO.OUT)

def LeftTurn():
	GPIO.output(LeftForward,True)
	GPIO.output(RightBackward,True)
	GPIO.output(LeftBackward,False)
	GPIO.output(RightForward,False)

def RightTurn():
	GPIO.output(LeftForward,False)
	GPIO.output(RightBackward,False)
	GPIO.output(LeftBackward,True)
	GPIO.output(RightForward,True)

def Forward(speed):
	GPIO.OUTPUT(LeftForward , True)
	GPIO.OUTPUT(RightForward, True)
	GPIO.output(RightBackward,False)
	GPIO.output(LeftBackward,False)


def Backward(speed):
	GPIO.OUTPUT(LeftBackward , True)
	GPIO.OUTPUT(RightBackward , True)
	GPIO.output(RightForwardward,False)
	GPIO.output(LeftForwardward,False)
	
def Stop():
	GPIO.output(LeftForward,True)
	GPIO.output(RightBackward,True)
	GPIO.output(LeftBackward,True)
	GPIO.output(RightForward,True)
	
	
