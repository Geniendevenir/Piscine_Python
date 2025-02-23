class TinyStatistician:
	def mean(self, x):
		if not x:
			return None
		return sum(x) / len(x)

	def median(self, x):
		if not x:
			return None
		x.sort()
		x_len = len(x)
		mid = x_len // 2
		if x_len % 2 == 0:
			return (x[mid - 1] + x[mid] / 2)
		else:
			return (float(x[mid]))

	def quartile(self, x):
		if not x:
			return None
		x.sort()
		x_len = len(x)
		
		def percentile(p):
			mid_float = (p / 100) * (x_len - 1) # Calculate Index (float)
			mid_small = int(mid_float)			# Rounding the Index to the closest smallest
			mid_big = int(mid_float) + 1		# Get the next Value
			if mid_big >= x_len:
				return (float(x[mid_big]))
			else:
				return x[mid_small] + (mid_float - mid_small) * (x[mid_big] - x[mid_small])

		return [percentile(25), percentile(75)]

	def var(self, x):
		if not x:
			return None
		x_mean = self.mean(x)
		x_diff = list(map(lambda y: y - x_mean, x))
		x_quar = list(map(lambda y: y**2, x_diff))
		return self.mean(x_quar)

	def std(self, x):
		if not x:
			return None
		return self.var(x) ** 0.5