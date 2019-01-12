import RPi.GPIO as GPIO
import time
import os
import sys

class simple_button(object):
	"""Class for use with an simple click button
	"""
	def __init__(self, function, pin, *args, pin_setup='BOARD', **kwargs):
		self.pin = pin
		if pin_setup == 'BCM':
			GPIO.setmode(GPIO.BCM)
		else:
			GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)
		GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.remove_event_detect(self.pin)
		GPIO.add_event_detect(self.pin, GPIO.RISING, callback=lambda x: self.callback(function, *args, **kwargs))
		
	def callback(self, function, *args, **kwargs):
		if GPIO.input(self.pin) == 1:
			function(*args, **kwargs)
		else:
			pass
		

# wait for touch sensor activation

if __name__ == '__main__':
	try:
		def button_print(text):
			print(text)

		simple_button(button_print, 'Hey!', pin=17, pin_setup='BCM')
		while True:
			time.sleep(0.5)		
	except KeyboardInterrupt:
		print('\n\n *** Stopping Program ***')
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)
