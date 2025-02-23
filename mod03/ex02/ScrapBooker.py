import numpy as np
import matplotlib.pyplot as plt

class ScrapBooker:
	def crop(self, array, dim, position=(0,0)):
		height, width = array.shape
		if dim[0] + position[0] > height:
			return print("Crop Impossible: Wrong height")
		elif dim[1] + position[1] > width:
			return print("Crop Impossible: Wrong width")
		return array[position[0]:position[0] + dim[0],
			   		position[1]:position[1] + dim[1]]

	def thin(self, array, n, axis):
		height, width = array.shape
		if axis == 0: #Rows
			if n > height:
				return print("Thin Impossible: n > number of rows")
			else:
				to_remove = np.arange(n - 1, height, n)
				print(f"arr to remove =\n{to_remove}")
				thined_arr = np.delete(array, to_remove, axis)
				return thined_arr
		elif axis == 1: #Columns
			if n > width:
				return print("Thin Impossible: n > number of columns")
			else:
				to_remove = np.arange(n - 1, width, n)
				print(f"arr to remove =\n{to_remove}")
				thined_arr = np.delete(array, to_remove, axis)
				return thined_arr
		return
	
	def juxtapose(self, array, n, axis):
			new_array = array
			for i in range(n - 1):
				new_array = np.concatenate((new_array, array), axis)
			return (new_array)
	
	def mosaic(self, array, dim):
		return np.tile(array, dim)