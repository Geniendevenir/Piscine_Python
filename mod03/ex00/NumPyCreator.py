import numpy as np

class NumPyCreator:
	def from_list(self, lst):
		return np.array(lst)

	def from_turple(self, tpl):
		return np.zeros(tpl)

	def from_iterable(self, itr):
		return np.array(itr)

	def from_shape(self, shape, value=0):
		return np.full(shape, value)

	def random(self, shape):
		return np.random.random(shape)

	def identity(self, n):
		return np.identity(n)


test = NumPyCreator()
a = [[1, 2, 3], [6, 3, 4]]
b = (2, 3)
c = {
	1 : 'one',
	2 : 'two',
	3 : 'three'
}
d_shape = (2, 3)
d_value = 1
e = (3, 4)
f = 5
print(f"a = {a}")
print(test.from_list(a))
print(f"b = {b}")
print(test.from_turple(b))
print(f"c = {c}")
print(test.from_iterable(c))
print(test.from_shape(d_shape, d_value))
print(test.random(e))
print(test.identity(f))

