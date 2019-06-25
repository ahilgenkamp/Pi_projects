#python program to take picture when button is pressed
#from ...button import simple_button
#from ..pi_camera import pi_camera
import os
import time
import datetime
import importlib

importlib.import_module(simple_button)
importlib.import_module(pi_camera)

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
