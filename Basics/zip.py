""" Python zip() method takes iterable or containers and returns a single iterator object, having mapped values from all the containers. 

It is used to map the similar index of multiple containers so that they can be used just using a single entity.  """


""" Syntax :  zip(*iterators) 

Parameters : Python iterables or containers ( list, string etc ) 
Return Value : Returns a single iterator object, having mapped values from all the 
containers. """


# Example 1: Python zip two lists

name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
 
# using zip() to map values
mapped = zip(name, roll_no)
 
print(set(mapped))


# Example 2: Python zip enumerate

names = ['Mukesh', 'Roni', 'Chari']
ages = [24, 50, 18]
 
for i, (name, age) in enumerate(zip(names, ages)):
    print(i, name, age)


# Example 3: Python zip() Dictionary

stocks = ['reliance', 'infosys', 'tcs']
prices = [2175, 1127, 2750]
 
new_dict = {stocks: prices for stocks,
            prices in zip(stocks, prices)}
print(new_dict)


# Unzipping means converting the zipped values back to the individual self as they were. This is done with the help of “*” operator.

# Python code to demonstrate the working of
# unzip
 
# initializing lists
name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = [4, 1, 3, 2]
marks = [40, 50, 60, 70]
 
# using zip() to map values
mapped = zip(name, roll_no, marks)
 
# converting values to print as list
mapped = list(mapped)
 
# printing resultant values
print("The zipped result is : ", end="")
print(mapped)
 
print("\n")
 
# unzipping values
namz, roll_noz, marksz = zip(*mapped)
 
print("The unzipped result: \n", end="")
 
# printing initial lists
print("The name list is : ", end="")
print(namz)
 
print("The roll_no list is : ", end="")
print(roll_noz)
 
print("The marks list is : ", end="")
print(marksz)


""" There are many possible applications that can be said to be executed using zip, 

be it student database or scorecard or any other utility that requires mapping of groups. 

A small example of scorecard is demonstrated below.  """

# Python code to demonstrate the application of
# zip()
 
# initializing list of players.
players = ["Sachin", "Sehwag", "Gambhir", "Dravid", "Raina"]
 
# initializing their scores
scores = [100, 15, 17, 28, 43]
 
# printing players and scores.
for pl, sc in zip(players, scores):
    print("Player :  %s     Score : %d" % (pl, sc))