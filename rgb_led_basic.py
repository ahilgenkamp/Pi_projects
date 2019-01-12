import RPi.GPIO as GPIO
import time
import os
import sys

class rgb_led(object):
	"""Class for use with an RGB LED
	"""
	def __init__(self, red_pin, green_pin, blue_pin, pin_setup='BOARD'):
		self.red = red_pin
		self.green = green_pin
		self.blue = blue_pin
		if pin_setup == 'BCM':
			GPIO.setmode(GPIO.BCM)
		else:
			GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)
		#SETUP FOR EACH ANODE
		GPIO.setup(self.red, GPIO.OUT)
		GPIO.setup(self.green, GPIO.OUT)
		GPIO.setup(self.blue, GPIO.OUT)
		#SET ALL PINS TO FALSE TO START
		GPIO.output(self.red, False)
		GPIO.output(self.green, False)
		GPIO.output(self.blue, False)

	def on(self, color):
		if color == 'red':
			GPIO.output(self.red, True)
			GPIO.output(self.green, False)
			GPIO.output(self.blue, False)
		elif color == 'green':
			GPIO.output(self.red, False)
			GPIO.output(self.green, True)
			GPIO.output(self.blue, False)
		elif color == 'blue':
			GPIO.output(self.red, False)
			GPIO.output(self.green, False)
			GPIO.output(self.blue, True)
		elif color == 'yellow':
			GPIO.output(self.red, True)
			GPIO.output(self.green, True)
			GPIO.output(self.blue, False)
		elif color == 'magenta':
			GPIO.output(self.red, True)
			GPIO.output(self.green, False)
			GPIO.output(self.blue, True)
		elif color == 'cyan':
			GPIO.output(self.red, False)
			GPIO.output(self.green, True)
			GPIO.output(self.blue, True)
		else:
			print('Choose a valid color: (red, green, blue, yellow, magenta, cyan)')
			GPIO.output(self.red, False)
			GPIO.output(self.green, False)
			GPIO.output(self.blue, False)

	def off(self):
		GPIO.output(self.red, False)
		GPIO.output(self.green, False)
		GPIO.output(self.blue, False)



if __name__ == '__main__':
	try:
		RGB = rgb_led(red_pin=5, green_pin=6, blue_pin=13, pin_setup='BCM')
		RGB.on(color='red')
		time.sleep(1)
		RGB.on(color='green')
		time.sleep(1)
		RGB.on(color='blue')
		time.sleep(1)
		RGB.off()
	except KeyboardInterrupt:
		print('\n\n *** Stopping Program ***')
		try:
			GPIO.cleanup()
			sys.exit(0)
		except SystemExit:
			GPIO.cleanup()
			os._exit(0)
