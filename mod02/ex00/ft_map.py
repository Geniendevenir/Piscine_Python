def ft_map(function_to_apply, iterable):
	if not callable(function_to_apply):
		raise TypeError("Function to apply needs to be callable")
	try:
		iter(iterable)
	except:
		raise TypeError("Iterable needs to be iterable")
	for obj in iterable:
			yield function_to_apply(obj)

x = [1, 2, 3, 4, 5]
print(list(ft_map(lambda dum: dum + 1, x)))