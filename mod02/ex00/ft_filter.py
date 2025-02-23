def ft_filter(function_to_apply, iterable):
	if not callable(function_to_apply):
		raise TypeError("Function to apply needs to be callable")
	try:
		iter(iterable)
	except:
		raise TypeError("Iterable needs to be iterable")
	for obj in list(iterable):
		if function_to_apply(obj):
			yield obj
		else:
			continue

x = [1, 2, 3, 4, 5]
print(list(ft_filter(lambda dum: not (dum % 2), x)))