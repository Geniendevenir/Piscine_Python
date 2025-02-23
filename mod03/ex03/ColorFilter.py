import matplotlib.pyplot as plt
import numpy as np


class ColorFilter:
	def to_blue(self, array):
		""".copy / .zeros / .shape / .dstack  / = """
		blue_filter = array.copy()
		blue_filter[:, :, 0] = 0
		blue_filter[:, :, 1] = 0
		plt.imshow(blue_filter)
		plt.axis('off')
		plt.show()

	def to_green(self, array):
		""".copy / * / = """
		green_filter = array.copy()
		green_filter[:, :, 0] = 0
		green_filter[:, :, 2] = 0
		plt.imshow(green_filter)
		plt.axis('off')
		plt.show()

	def to_red(self, array):
		""".copy / .to_green / .to_blue / - / + / ="""
		red_filter = array.copy()
		red_filter[:, :, 1] = 0
		red_filter[:, :, 2] = 0
		plt.imshow(red_filter)
		plt.axis('off')
		plt.show()


"""
For rows in range(Height):
HEIGHT = Nbr of Rows (y):	-
							-
							-
							-

	For col in range(Width):
WIDTH = Nbr of Column (x):	- - - - -

		r, g, b = col 
If array[y][x] is an array just get the element

[		   0       1       2       3       4
	0 [ [[RGB]] [[RGB]] [[RGB]] [[RGB]] [[RGB]] ]
	1 [ [[RGB]] [[RGB]] [[RGB]] [[RGB]] [[RGB]] ]
	2 [ [[RGB]] [[RGB]] [[RGB]] [[RGB]] [[RGB]] ]
	3 [ [[RGB]] [[RGB]] [[RGB]] [[RGB]] [[RGB]] ]
]
"""

""" 
FIRST STUPID VERSION JUST USE SLICING
def to_blue(self, array):
		height, width, channel = array.shape
		blue_array = array.copy()
		print(blue_array)
		for row in range(blue_array.shape[0]):
			for col in range(blue_array.shape[1]):
				blue_array[row, col][2] = 1
		result = np.dstack((array, blue_array))
		plt.imshow(result)
		plt.axis('off')
		plt.show()
		
"""