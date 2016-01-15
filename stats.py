def mean(vals):
	"""Calculate the arithmetic mean of a list of numbers in vals"""
	assert type(vals) is list, 'wrong input format'
	vals = [float(x) for x in vals]
	total = sum(vals)
	length = len(vals)
	if length == 0:
		return 0.0
	else:
		return total/length
	


##assertions and exceptions make sure you're using the correct file type
#runs program with non-numbers
#print(mean("hello")) ###throws error above

