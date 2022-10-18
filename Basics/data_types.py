""" 

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType 

"""

# you can get the data type of any object by using the type() function:

x = 5
print(type(x))


# in Python, the data type is set when you assign a value to a variable:

x = "hello world"	                            # str	
x = 20	                                        # int	
x = 20.5	                                    # float	
x = 1j	                                        # complex	
x = ["apple", "banana", "cherry"]	            # list	
x = ("apple", "banana", "cherry")	            # tuple	
x = range(6)	                                # range	
x = {"name" : "ataberk", "age" : 36}	        # dict	
x = {"apple", "banana", "cherry"}	            # set	
x = frozenset({"apple", "banana", "cherry"})	# frozenset	
x = True	                                    # bool	
x = b"hello"	                                # bytes	
x = bytearray(5)	                            # bytearray	
x = memoryview(bytes(5))	                    # memoryview	
x = None	                                    # NoneType


# if you want to specify the data type, you can use the following constructor functions:

x = str("Hello World")	                        # str	
x = int(20)	                                    # int	
x = float(20.5)	                                # float	
x = complex(1j)	                                # complex	
x = list(("apple", "banana", "cherry"))	        # list	
x = tuple(("apple", "banana", "cherry"))	    # tuple	
x = range(6)	                                # range	
x = dict(name="John", age=36)	                # dict	
x = set(("apple", "banana", "cherry"))	        # set	
x = frozenset(("apple", "banana", "cherry"))	# frozenset	
x = bool(5)	                                    # bool	
x = bytes(5)	                                # bytes	
x = bytearray(5)	                            # bytearray	
x = memoryview(bytes(5))	                    # memoryview