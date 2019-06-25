#python program to take picture when button is pressed
from modules.button import simple_button
from modules.pi_camera import pi_camera
import os
import time
import datetime
import sys

if __name__ == '__main__':
	try:
		#create function to pass when button is pressed
		def take_pic(save_path):
			file_name = str(datetime.datetime.now())+'.jpg'
			pi_camera().capture(save_path=save_path+'/'+file_name, t=0.5)
			print('Picture Taken')
		cwd = os.getcwd()
		'''
		def print_test():
			print(cwd)

		simple_button(print_test, pin=17, pin_setup='BCM')	
		'''
		simple_button(take_pic, cwd+"/boggle_images/", pin=17, pin_setup='BCM')
		while True:
			time.sleep(0.5)

	except KeyboardInterrupt:
		print('\n\n *** Stopping Program ***')
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)
