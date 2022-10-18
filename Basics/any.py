# Python any() function returns True if any of the elements of a given iterable( List, Dictionary, Tuple, set, etc) are True else it returns False. 

""" Syntax: any(iterable)

Parameters: Iterable: It is an iterable object such as a dictionary, tuple, list, set, etc.                 

Returns: Python any() function returns true if any of the items is True. """


# Example #1: Python any()  function Lists 

# All elements of list are true
l = [ 4, 5, 1]
print(any( l ))

# All elements of list are false
l = [ 0, 0, False]
print(any( l ))

# Some elements of list are
# true while others are false
l = [ 1, 0, 6, 7, False]
print(any( l ))

# Empty List
l = []
print(any( l ))


# Example #2: Working of any() function with Tuples

# All elements of tuple are true
t = (2, 4, 6)
print(any(t))

# All elements of tuple are false
t = (0, False, False)
print(any(t))

# Some elements of tuple are true while
# others are false
t = (5, 0, 3, 1, False)
print(any(t))

# Empty tuple
t = ()
print(any(t))


# Example #3: Working of any() function with Sets

# All elements of set are true
s = { 1, 1, 3}
print(any( s ))

# All elements of set are false
s = { 0, 0, False}
print(any( s ))

# Some elements of set are true while others are false
s = { 1, 2, 0, 8, False}
print(any( s ))

#Empty set
s = {}
print(any( s ))


# Example #4: Working of any() function with Dictionaries

# Note: In the case of a dictionary if all the keys of the dictionary are false or the dictionary is empty the any() returns False. If at least one key is True any() returns True.

# All elements of dictionary are true
d = {1: "Hello", 2: "Hi"}
print(any(d))

# All elements of dictionary are false
d = {0: "Hello", False: "Hi"}
print(any(d))

# Some elements of dictionary
# are true while others are false
d = {0: "Salut", 1: "Hello", 2: "Hi"}
print(any(d))

# Empty dictionary
d = {}
print(any(d))


# Example #5: Working of any() function with Strings

# Non-Empty String
s = "Hi There!"
print(any(s))

# Non-Empty String
s = "000"
print(any(s))

# Empty string
s = ""
print(any(s))


# Example #6: Python any function with condition

# Python3 code to demonstrate working of
# Check if any element in list satisfies a condition
# Using any()

# initializing list
test_list = [4, 5, 8, 9, 10, 17]

# printing list
print("The original list : " + str(test_list))

# Check if any element in list satisfies a condition
# Using any()
res = any(ele > 10 for ele in test_list)

# Printing result
print("Does any element satisfy specified condition ? : " + str(res))


# Example #7: Python any() function with for loop

def any(list_x):
	for item in list_x:
		if item:
			return True
	return False

x = [4, 5, 8, 9, 10, 17]
print(any(x))