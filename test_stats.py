##separating test_stats parts of the code

from stats import mean
#will start looking for the mean file in shared folder
#can also use explicit path

def test_mean():
	assert mean([2,4]) == 3.0 #you know the answer you should get and you're testing the formula that it gives you the correct answer
test_mean()

def test_empty_list():
	assert mean([]) == 0.0
test_empty_list()

def test_floating_mean():
	assert mean([2,3]) == 2.5
test_floating_mean()