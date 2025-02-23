import os
import csv
import itertools

class CsvReader():
	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		if filename == "" or not isinstance(filename, str):
			raise TypeError ("Error: filename should be a non-empty string")
		if not isinstance(sep, str) or len(sep) != 1 or sep.isprintable() == False:
			raise TypeError ("Error: sep must be ONE printable character")
		if (not isinstance(header, bool)):
			raise TypeError ("Error: header must either be True or False")
		if (not isinstance(skip_top, int) or not isinstance(skip_bottom, int)):
			raise TypeError ("Error: skip_top and skip_bottom must be int")
		if (skip_top < 0 or skip_bottom < 0):
			raise ValueError("Error: skip_top and skip_bottom must be positive int")
		self.filename = filename
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom
		self.file = None
		self.data = []
		self.header_data = None

	def __enter__(self):
		if not os.path.exists(self.filename):
			raise FileExistsError(f"Error: File Not Found")
		try:	
			self.file = open(self.filename, "r")
		except Exception as e:
			print(f"Error opening file: {e}")
			return

		reader = csv.reader(self.file, delimiter=self.sep)
		rows = list(reader) #Already Correct [[]]
		expected_length = len(rows[0]) if rows else 0
		for row in rows:
			if(len(row) != expected_length):
				raise ValueError(f"Error: Row {row} has {len(row)} fields, expected {expected_length}")
		
		if self.header:
			self.header_data = rows[0]
			rows = rows[1:]
		
		self.data = rows[self.skip_top : len(rows) - self.skip_bottom if self.skip_bottom else None]
	
		return (self)

	def __exit__(self, exc_type, exc_value, traceback):
		if self.file:
			self.file.close()

	def getdata(self):
		return self.data

	def getheader(self):
		return self.header_data if self.header else None

with CsvReader("test.csv", skip_top=1, skip_bottom=1) as file:
	data = file.getdata()
	print(data)
	header = file.getheader()

