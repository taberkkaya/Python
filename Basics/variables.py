# variables are containers for storing data values.
# a variable is created the moment you first assign a value to it.

x = 5
y = "python"
print(x)
print(y)


# variables do not need to be declared with any particular type, and can even change type after they have been set.

x = 4          # x is of type int
x = "ataberk"  # x is now of type str
print(x)


# if you want to specify the data type of a variable, this can be done with casting.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


# you can get the data type of a variable with the type() function.

x = 3
y = "ataberk"
print(type(x))
print(type(y))


# string variables can be declared either by using single or double quotes:

x = "ataberk"
# is the same as
x = 'ataberk'


# variable names are case-sensitive.

a = 4
A = "ataberk"
# A will not overwrite a


# legal variable names:

myvar = "ataberk"
my_var = "ataberk"
_my_var = "ataberk"
myVar = "ataberk"
MYVAR = "ataberk"
myvar2 = "ataberk"


# illegal variable names:

# 2myvar = "ataberk"
# my-var = "ataberk"
# my var = "ataberk"


# python allows you to assign values to multiple variables in one line:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


# and you can assign the same value to multiple variables in one line:

x = y = z = "Orange"
print(x)
print(y)
print(z)


# if you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


# the Python print() function is often used to output variables.

x = "python is awesome"
print(x)


# in the print() function, you output multiple variables, separated by a comma:

x = "python"
y = "is"
z = "awesome"
print(x, y, z)

# you can also use the + operator to output multiple variables:

x = "python "
y = "is "
z = "awesome"
print(x + y + z) # notice the space character after "python " and "is ", without them the result would be "pythonisawesome".


# for numbers, the + character works as a mathematical operator:

x = 5
y = 10
print(x + y)


# in the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:

# x = 5
# y = "ataberk"
# print(x + y)

# the best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:

x = 5
y = "ataberk"
print(x, y)


# global variables can be used by everyone, both inside of functions and outside.
# create a variable outside of a function, and use it inside the function

x = "awesome"

def myfunc():
  print("python is " + x)

myfunc()


# if you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

x = "awesome"

def myfunc():
  x = "fantastic"
  print("python is " + x)

myfunc()

print("python is " + x)


# normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# to create a global variable inside a function, you can use the global keyword.

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("python is " + x)

# also, use the global keyword if you want to change a global variable inside a function.
# to change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("python is " + x)