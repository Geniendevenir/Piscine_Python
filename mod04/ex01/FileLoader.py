import pandas as pd


class FileLoader():
	def load(self, path):
		df = pd.read_csv(path) #Load CSV file as a Panda Dataframe
		height, width = df.shape
		print(f"Loading dataset of dimensions {height} x {width}")
		return df

	def display(self, df, n):
		if n >= 0:
			print(df.head(n))
		else:
			print(df.tail(n))