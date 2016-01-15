def mean(vals):
	"""Calculate the arithmetic mean of a list of numbers in vals"""
	assert type(vals) is list, 'wrong input format'
	total = sum(vals)
	length = len(vals)
	return total/length
	
#print(mean([2,4]))

##assertions and exceptions make sure you're using the correct file type
#runs program with non-numbers
print(mean("hello"))
