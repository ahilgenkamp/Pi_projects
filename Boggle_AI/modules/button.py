import RPi.GPIO as GPIO
import time
import os
import sys

class simple_button(object):
	"""Class for use with an simple click button
	"""
	def __init__(self, function, *args, pin=7, pin_setup='BOARD', **kwargs):
		self.pin = pin
		if pin_setup == 'BCM':
			GPIO.setmode(GPIO.BCM)
		else:
			GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)
		GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) #set for use with internal pull up resistor.  If using a resistor on a bread board this can be removed.
		GPIO.remove_event_detect(self.pin)
		GPIO.add_event_detect(self.pin, GPIO.RISING, callback=lambda x: self.callback(function, *args, **kwargs))
		
	def callback(self, function, *args, **kwargs):
		if GPIO.input(self.pin) == 1:
			function(*args, **kwargs)
		else:
			pass
		

if __name__ == '__main__':
	try:
    def test():
      print('Hey!')

		simple_button(test, pin=17, pin_setup='BCM')
		while True:
			time.sleep(0.5)		
	except KeyboardInterrupt:
		print('\n\n *** Stopping Program ***')
		try:
			GPIO.cleanup()
			sys.exit(0)
		except SystemExit:
			GPIO.cleanup()
			os._exit(0)
