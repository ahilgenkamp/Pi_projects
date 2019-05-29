#Simple class to collect raspberry pi camera functions

from picamera import PiCamera
import time
import os


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


if __name__ == '__main__':
	try:
		cwd = os.getcwd()
		pi_camera().preview(t=5)
		#pi_camera().capture(cwd+"/boggle_images/boggle test.jpg", num=1, t=6)
	except KeyboardInterrupt:
		print('\n\n *** Stopping Program ***')
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)
