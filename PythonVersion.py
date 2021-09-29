# This prints out the version of Python being used and adds some info about the version

# The sys module provides information about constants, 
# functions and methods of the Python interpreter. 
# dir(system) gives a summary of the available constants, 
# functions and methods. Another possibility is the help() function. 
# Using help(sys) provides valuable detail information.

# https://docs.python.org/3.9/library/sys

import sys 



print("Python Version:\n")
print(sys.version)

print("\n\n")  # added just to help with terminal formatting
print("Version Info:")
print(sys.version_info)

print("\n\n") # added just to help with terminal formatting

help(sys)