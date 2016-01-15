##separating test_stats parts of the code

from stats import mean
#will start looking for the mean file in shared folder
#can also use explicit path
from nose.tools import assert_equal, assert_almost_equals

def test_mean():
	assert_equal(mean([2,4]),3.0) #you know the answer you should get and you're testing the formula that it gives you the correct answer
#test_mean()

def test_empty_list():
	assert_equal(mean([]),0)
#test_empty_list()

def test_floating_mean():
	assert_almost_equals(mean([0.5,0.5,1]),0.666666666) #make sure you add enough points after the decimal point
##test_floating_mean()

###nosetest will let you check that all your error checking tests work
#runs functions with test in the name

#way to check for errors without assert_equals and nose.tools
#def test_floating_mean():
	# assert mean([2,3]) == 2.5
##test_floating_mean()

#broken version of above test
#def test_floating_mean():
#	assert mean([0.5, 0.5, 1]) == 0.66666
##test_floating_mean()