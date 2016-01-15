def mean(vals):
	"""Calculate the arithmetic mean of a list of numbers in vals"""
	assert type(vals) is list, 'wrong input format'
	total = sum(vals)
	length = len(vals)
	return total/length
	
def test_mean():
	assert mean([2,4]) == 3.0 #you know the answer you should get and you're testing the formula that it gives you the correct answer
test_mean()

##assertions and exceptions make sure you're using the correct file type
#runs program with non-numbers
#print(mean("hello")) ###throws error above

