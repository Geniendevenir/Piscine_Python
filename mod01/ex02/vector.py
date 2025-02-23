from copy import deepcopy


class Vector:
	def __init__(self, values):
		self.shape = ()
		self.is_valid(values)
		self.values = values
	
	def is_valid(self, values):
		i = self.check_basics(values) + 1
		if i == 1:
			self.check_row(values)
			self.row = values
		else:
			self.check_column(values)
			self.shape = i, 1
			self.column = values

	def check_basics(self, values):
		if (not isinstance(values, list)):
			raise TypeError("Values should be a list")
		if (len(values) <= 0):
			raise ValueError("Values should have at least 1 sublist")
		for i, element in enumerate(values):
			if not isinstance(element, list):
				raise ValueError("Values should be a list containing only list(s)")
		return (i)

	def check_column(self, column):
		for sublst in column:
			if not isinstance(sublst, list):
				raise TypeError("column Sublist Should be list")
			elif len(sublst) != 1:
				print(sublst)
				raise ValueError("column sublist should have 1 float")
			elif not isinstance(sublst[0], float):
				raise ValueError("column Sublist element should be a float")
	
	def check_row(self, row):
		for i, nbr in enumerate(row[0]):
			if not isinstance(nbr, float):
				raise ValueError("row Elements should be floats")
		if i+1 < 2:
			raise ValueError ("Row sublist should have more than one element")
		self.shape = 1, i+1
	
	def dot(self, vec2):
		if self.shape != vec2.shape:
			raise ValueError("Vec1.shape != Vec2.shape")
		result = 0.0
		if self.shape[0] == 1:
			for a, b in zip(self.values[0], vec2.values[0]):
				result += a * b
		else:
			for a, b in zip(self.values, vec2.values):
				result += a[0] * b[0]
		return result
	
	def T(self):
		if self.shape[0] == 1:
			rev_vec = [[nbr] for nbr in self.values[0]]
		else:
			rev_vec = [[lst[0] for lst in self.values]]
		return Vector(rev_vec)
	

	def __add__(self, vec2):
		if self.shape != vec2.shape:
			raise ValueError("Vec1.shape != Vec2.shape")
		result = deepcopy(self.values)
		if self.shape[0] == 1:
			for i, a, b in enumerate(zip(self.values[0], vec2.values[0])):
				result[0][i] = a + b
		else:
			for i, a, b in enumerate(zip(self.values, vec2.values)):
				result[i][0] = a[0] + b[0]
		return result

	def __radd__(self, vec2):
		return (self.__add__(self, vec2))

	def __sub__(self, vec2):
		if self.shape != vec2.shape:
			raise ValueError("Vec1.shape != Vec2.shape")
		result = deepcopy(self.values)
		if self.shape[0] == 1:
			for i, a, b in enumerate(zip(self.values[0], vec2.values[0])):
				result[0][i] = a - b
		else:
			for i, a, b in enumerate(zip(self.values, vec2.values)):
				result[i][0] = a[0] - b[0]
		return result

	def __rsub__(self, vec2):
		if self.shape != vec2.shape:
			raise ValueError("Vec1.shape != Vec2.shape")
		result = deepcopy(self.values)
		if self.shape[0] == 1:
			for i, a, b in enumerate(zip(self.values[0], vec2.values[0])):
				result[0][i] = a - b
		else:
			for i, a, b in enumerate(zip(self.values, vec2.values)):
				result[i][0] = a[0] - b[0]
		return result	

	
	def __truediv__(self, scalar):
		# truediv : only with scalars (to perform division of a Vector by a scalar).
		if scalar <= 0:
			raise ZeroDivisionError("ZeroDivisionError: division by zero.")
		result = deepcopy(self.values)
		if self.shape[0] == 1:
			for i, nbr in enumerate(self.values[0]):
				result[0][i] /= scalar
		else:
			for i, nbr in enumerate(self.values):
				result[i][0] /= scalar
		return str(result)


	def __rtruediv__(self):
		# rtruediv : raises an NotImplementedError with the message "Division of a scalar by a Vector is not defined here."
		raise NotImplementedError("Division of a scalar by a Vector is not defined here.")


	def __mul__(self, scalar):
		result = deepcopy(self.values)
		if self.shape[0] == 1:
			for i, nbr in enumerate(self.values[0]):
				result[0][i] *= scalar
		else:
			for i, nbr in enumerate(self.values):
				result[i][0] *= scalar
		return str(result)

	def __rmul__(self, scalar):
		# mul & rmul: only scalars (to perform multiplication of a Vector by a scalar).
		return self.__mul__(self, scalar)


	def __str__(self):
		return str(self.values)

	def __repr__(self):
		# must be identical, i.e we expect that print(vector) and vector within python interpretor to behave the same, see corresp
		return str(self.values)

