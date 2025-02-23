def ft_reduce(function_to_apply, iterable):
	if not callable(function_to_apply):
		raise TypeError("Function to apply needs to be callable")
	try:
		iterator = iter(iterable)
	except:
		raise TypeError("Iterable needs to be iterable")
	try:
		result = next(iterator)
	except:
		raise TypeError("Iterable must have an initial value")
	for obj in iterator:
			result = function_to_apply(result, obj)
	return result

lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(ft_reduce(lambda u, v: u + v, lst))