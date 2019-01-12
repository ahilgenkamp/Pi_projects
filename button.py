import RPi.GPIO as GPIO
import time
import os
import sys
from rgb_led_pwm import rgb_led

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
		color_list = [(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),(255,0,255),(255,69,0),(112,128,144)]
		def run_rgb_led(r_pin, g_pin, b_pin, rgb_setup='BOARD'):
			RGB = rgb_led(red_pin=r_pin, green_pin=g_pin, blue_pin=b_pin, pin_setup=rgb_setup)
			for c in color_list:
				RGB.setColor(color=(c[0],c[1],c[2]))
				time.sleep(1)
			RGB.off()

		simple_button(run_rgb_led, 19, 20, 21, pin=17, pin_setup='BCM', rgb_setup='BCM')
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
