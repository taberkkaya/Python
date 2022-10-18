# To delete a file, you must import the OS module, and run its os.remove() function:

# Remove the file "demofile.txt":

import os
os.remove("demofile.txt")


# To avoid getting an error, you might want to check if the file exists before you try to delete it:


# Check if file exists, then delete it:

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")


# To delete an entire folder, use the os.rmdir() method:

# Remove the folder "myfolder":

import os
os.rmdir("myfolder")

# Note: You can only remove empty folders.