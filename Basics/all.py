""" The all() function is an inbuilt function in Python which returns true if all the elements of a given iterable( List, Dictionary, Tuple, set, etc) are True else it returns False. 

It also returns True if the iterable object is empty. """

""" Syntax: all( iterable )
 
Parameters: Iterable: It is an iterable object such as a dictionary,tuple,list,set,etc. """


# Example #1: Working of all() with Lists:

# All elements of list are true
l = [4, 5, 1]
print(all(l))
 
# All elements of list are false
l = [0, 0, False]
print(all(l))
 
# Some elements of list are
# true while others are false
l = [1, 0, 6, 7, False]
print(all(l))
 
# Empty List
l = []
print(all(l))


# Example #2: Working of all() with Tuples.

# All elements of tuple are true
t = (2, 4, 6)
print(all(t))
 
# All elements of tuple are false
t = (0, False, False)
print(all(t))
 
# Some elements of tuple
# are true while others are false
t = (5, 0, 3, 1, False)
print(all(t))
 
# Empty tuple
t = ()
print(all(t))


# Example #3: Working of all() with Sets.

# All elements of set are true
s = {1, 1, 3}
print(all(s))

# All elements of set are false
s = {0, 0, False}
print(all(s))

# Some elements of set
# are true while others are false
s = {1, 2, 0, 8, False}
print(all(s))

# Empty set
s = {}
print(all(s))


# Example #4: Working of all() with Dictionaries.

# Note: In the case of a dictionary if all the keys of the dictionary are true or the dictionary is empty the all() returns true else it returns false.

# All elements of dictionary are true
d = {1: "Hello", 2: "Hi"}
print(all(d))

# All elements of dictionary are false
d = {0: "Hello", False: "Hi"}
print(all(d))

# Some elements of dictionary
# are true while others are false
d = {0: "Salut", 1: "Hello", 2: "Hi"}
print(all(d))

# Empty dictionary
d = {}
print(all(d))


# Example #5: Working of all() with Strings.

# Non-Empty String
s = "Hi There!"
print(all(s))

# Non-Empty String
s = "000"
print(all(s))

# Empty string
s = ""
print(all(s))
