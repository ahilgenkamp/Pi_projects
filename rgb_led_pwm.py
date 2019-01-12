import RPi.GPIO as GPIO
import time
import os
import sys

class rgb_led(object):
	"""Class for use with an RGB LED
	Uses PWM to display any color
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
		#SETUP FOR PWM (2000KHz frequency)
		self.p_r = GPIO.PWM(self.red, 2000)
		self.p_g = GPIO.PWM(self.green, 2000)
		self.p_b = GPIO.PWM(self.blue, 2000)
		self.p_r.start(0)
		self.p_g.start(0)
		self.p_b.start(0)
		
	def map(rgb_val):
		return rgb_val * 100 / 255
	
	def setColor(self, color):  #input color as a tuple
		r_val = map(color[0])
		g_val = map(color[1])
		b_val = map(color[2])
		
		self.p_r.ChangeDutyCycle(100-r_val)
		self.p_g.ChangeDutyCycle(100-g_val)
		self.p_b.ChangeDutyCycle(100-b_val)
		
	def off(self):
		self.p_r.start(0)
		self.p_g.start(0)
		self.p_b.start(0)

if __name__ == '__main__':
	try:
		RGB = rgb_led(red_pin=19, green_pin=20, blue_pin=21, pin_setup='BCM')
		RGB.setColor(color=(255,0,0))
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
