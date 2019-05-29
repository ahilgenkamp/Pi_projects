#test image rec

from PIL import Image
import numpy as np
import os

cwd = os.getcwd()

i = Image.open(cwd+"\\boggle_images\\boggle test.jpg")
iar = np.asarray(i)

print(iar[0])
