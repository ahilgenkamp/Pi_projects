# flash LED lights

import RPi.GPIO as GPIO
import time
import os
import sys

class LED(object):
	"""Code to turn on / off LED or to flash
	"""
	def __init__(self, pin, pin_setup='BOARD'):
		self.pin = pin
		if pin_setup == 'BCM':
			GPIO.setmode(GPIO.BCM)
		else:
			GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)
		GPIO.setup(self.pin, GPIO.OUT)
		
	def on(self):
		GPIO.output(self.pin, GPIO.HIGH)

	def off(self):
		GPIO.output(self.pin, GPIO.LOW)

	def flash(self, flash, sleep):
		for n in range(0,flash):
			self.on()
			time.sleep(sleep)
			self.off()

# Create loop to flash LEDs

if __name__ == '__main__':
	try:
		LED = LED(pin=18, pin_setup='BCM')
		LED.flash(flash=10, sleep=1.5)
		'''
		LED.on()
		time.sleep(1)
		LED.off()
		time.sleep(1)
		LED.on()
		time.sleep(5)
		LED.off()
		'''
	except KeyboardInterrupt:
		print('\n\n *** Stopping Program ***')
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)

