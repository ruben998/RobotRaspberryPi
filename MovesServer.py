
import RPi.GPIO as GPIO


class Moves():
	def __init__(self):
		GPIO.setwarnings(False)
	    GPIO.setmode(GPIO.BOARD)
	    GPIO.setup(7, GPIO.OUT)
	    GPIO.setup(11, GPIO.OUT)
	    GPIO.setup(13, GPIO.OUT)
	    GPIO.setup(15, GPIO.OUT)
	    
	def forward(self):
	    stop()
	    GPIO.output(11, True)
	    GPIO.output(13, True)

	def back(self):
	    stop()
	    GPIO.output(15, True)
	    GPIO.output(7, True)

	def right():
	    stop(self)
	    GPIO.output(7, True)
	    GPIO.output(13, True)

	def left(self):
	    stop()
	    GPIO.output(11, True)
	    GPIO.output(15, True)

	def stop(self):
	    GPIO.output(7, False)
	    GPIO.output(11, False)
	    GPIO.output(13, False)
	    GPIO.output(15, False)