import numpy as np
import matplotlib.pyplot as plt
import os

class ImageProcessor:
	def __exit__(self, exc_type, exc_value, traceback):
		if (exc_value != None):
			return("Error: file couldn't Open")
		return (self)
	def load(self, path):
		if (os.path.exists(path) == 0):
			raise(f"Error: {path} don't exists")
		try:
			img = plt.imread(path) #ndarray
		except:
			raise PermissionError("Could not Read File")
		height, width, channel = img.shape
		if channel == 4:
			img_rgb = img[:, :, :3]
		else:
			img_rgb = img
		print(f"{img_rgb}, Dimension: {height}/{width}")
		return img_rgb
			
	def display(self, array):
		plt.imshow(array)
		plt.axis('off')
		plt.show()