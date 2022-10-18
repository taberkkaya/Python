# Assume we have the following file, located in the same folder as Python:

""" To open the file, use the built-in open() function.

The open() function returns a file object, which has a read() method for reading the content of the file: """

f = open("py_tutorial\demofile.txt", "r")
print(f.read())


# If the file is located in a different location, you will have to specify the file path, like this:

# Open a file on a different location:

f = open("C:\\workspaces\py_tutorial\myfiles\welcome.txt", "r")
print(f.read())


# By default the read() method returns the whole text, but you can also specify how many characters you want to return:

# Return the 5 first characters of the file:

f = open("py_tutorial\demofile.txt", "r")
print(f.read(5))


# You can return one line by using the readline() method:

# Read one line of the file:

f = open("py_tutorial\demofile.txt", "r")
print(f.readline())


# By calling readline() two times, you can read the two first lines:

f = open("py_tutorial\demofile.txt", "r")
print(f.readline())
print(f.readline())


# By looping through the lines of the file, you can read the whole file, line by line:

# Loop through the file line by line:

f = open("py_tutorial\demofile.txt", "r")
for x in f:
  print(x)


# It is a good practice to always close the file when you are done with it.

# Close the file when you are finish with it:

f = open("py_tutorial\demofile.txt", "r")
print(f.readline())
f.close()

# Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.