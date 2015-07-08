
import RPi.GPIO as GPIO


def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    
def forward():
    stop()
    GPIO.output(11, True)
    GPIO.output(13, True)

def back():
    stop()
    GPIO.output(15, True)
    GPIO.output(7, True)

def right():
    stop()
    GPIO.output(7, True)
    GPIO.output(13, True)

def left():
    stop()
    GPIO.output(11, True)
    GPIO.output(15, True)

def stop():
    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, False)
