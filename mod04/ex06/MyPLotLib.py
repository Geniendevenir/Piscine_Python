import pandas as pd
import matplotlib
matplotlib.use('TkAgg')  # or use 'Agg' if you don't need interactive windows
import matplotlib.pyplot as plt

class MyPlotLib:
	def histogram(data, features):
		plt.figure(figsize=(8, 4))
		# Drop missing values to avoid plotting issues
		unique_years = sorted(data[features[0]].unique())
		plt.hist(data[features[0]], bins=len(unique_years), edgecolor='black')
		plt.title(f'Histogram of {features[0]}')
		plt.xlabel(features[0])         # Label the x-axis with the current features[0]
		plt.ylabel(features[1])     # Y-axis shows frequency/count
		# Optionally, set x-ticks for the 'Year' histogram only
		plt.xticks(unique_years, rotation=45)  # rotate labels if there are many years
		plt.show()
	
	def density(data, features):
		for feature in features:
			plt.figure(figsize=(8, 4))
			data[feature].plot(kind='density')
			plt.title(f'Density Plot of {feature}')
			plt.xlabel(feature)
			plt.show()

	def pair_plot(data, features):
		""""""
	def box_plot(data, features):
		""""""