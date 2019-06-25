#python program to take picture when button is pressed
#from ...button import simple_button
#from ..pi_camera import pi_camera
import os
import time
import datetime
import RPi.GPIO as GPIO
import sys
from picamera import PiCamera

class pi_camera(object):
	
	def __init__(self, res=None, framerate=None, brightness=50):
		self.camera = PiCamera()
		self.camera.brightness = brightness
		if res is not None:
			self.camera.resolution = res
		if framerate is not None:
			self.camera.framerate = framerate	

	def preview(self, t=10):
		self.camera.start_preview()
		time.sleep(t)
		self.camera.stop_preview()
		
	def capture(self, save_path, num=1, t=2):
		'''
		save path file extension should be .jpg
		'''
		self.camera.start_preview()
		for i in range(num):
			time.sleep(t)
			if i == 0:
				self.camera.capture(save_path)
			else:
				self.camera.capture(save_path[0:-4]+str(i)+save_path[-4:])
		self.camera.stop_preview()
		
	def record_video(self, save_path, t=10):
		'''
		save path file extension should be .h264
		'''
		self.camera.start_preview()
		self.camera.start_recording(save_path)
		time.sleep(t)
		self.camera.stop_recording()
		self.camera.stop_preview()

		
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
		#create function to pass when button is pressed
		def take_pic(save_path):
			file_name = datetime.datetime.now()+'.jpg'
			pi_camera.capture(save_path=save_path+'/'+file_name, t=0.5)

		cwd = os.getcwd()
		simple_button(take_pic, cwd+"/boggle_images", pin=17, pin_setup='BCM')	
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
