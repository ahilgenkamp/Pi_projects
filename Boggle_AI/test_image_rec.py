#test image rec

from PIL import Image
import numpy as np
import os
from matplotlib import pyplot as plt


def threshold(imageArray):
	balanceAr = []
	newAr = imageArray

	for r in imageArray:
		for p in r:
			avgNum = np.mean(p) 
			#another option to get average for a list: functools.reduce(lambda x, y: x+y, p/3)
			balanceAr.append(avgNum)

	balance = np.mean(balanceAr)

	for r in newAr:
		for p in r:
			if np.mean(p) > balance:
				p[0] = 255
				p[1] = 255
				p[2] = 255
			else:
				p[0] = 0
				p[1] = 0
				p[2] = 0
	return newAr

cwd = os.getcwd()

i = Image.open(cwd+"\\boggle_images\\2019-06-25 225947.825859.jpg")
iar = np.array(i)

#Show original image
#plt.imshow(iar)
#plt.show()

#show thresholding for the image
iar2 = threshold(iar)
plt.imshow(iar2)
plt.show() 
