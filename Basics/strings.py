""" Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello". """

# you can display a string literal with the print() function:

print("hello")
print('hello')


# you can use three double quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


""" Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string. """

a = "hello, world!"
print(a[1])


# since strings are arrays, we can loop through the characters in a string, with a for loop.

for x in "banana":
  print(x)


# to get the length of a string, use the len() function.

a = "hello, world!"
print(len(a))


# to check if a certain phrase or character is present in a string, we can use the keyword in.

txt = "the best things in life are free!"
print("free" in txt)

# use it in an if statement:

txt = "the best things in life are free!"
if "free" in txt:
  print("yes, 'free' is present.")


# to check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

txt = "the best things in life are free!"
print("expensive" not in txt)

# use it in an if statement:

txt = "the best things in life are free!"
if "expensive" not in txt:
  print("no, 'expensive' is NOT present.")


""" You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string. """

# get the characters from position 2 to position 5 (not included):

b = "hello, world!"
print(b[2:5])


# get the characters from the start to position 5 (not included):

b = "hello, world!"
print(b[:5])


# get the characters from position 2, and all the way to the end:

b = "hello, world!"
print(b[2:])


# use negative indexes to start the slice from the end of the string:

""" Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2): """

b = "hello, world!"
print(b[-5:-2])


# the upper() method returns the string in upper case:

a = "hello, world!"
print(a.upper())


# the lower() method returns the string in lower case:

a = "Hello, World!"
print(a.lower())


# the strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


# the replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))


# the split() method returns a list where the text between the specified separator becomes the list items.

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


# merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c)


# to add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)


# use the format() method to insert numbers into strings:

age = 21
txt = "My name is Ataberk, and I am {}"
print(txt.format(age))


# the format() method takes unlimited number of arguments, and are placed into the respective placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


# you can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


""" To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes: """

# the escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."


# other escape characters used in Python:

""" 

'	Single Quote	
\	Backslash	
n	New Line	
r	Carriage Return	
t	Tab	
b	Backspace	
f	Form Feed	
ooo	Octal value	
xhh	Hex value 

"""