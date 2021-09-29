# Simple program to output the date and time to the console.

# https://docs.python.org/3.9/library/datetime

import datetime

#help(datetime)

now = datetime.datetime.now()

print ("Current date and time : ")
print (now.strftime("%d-%m-%Y %H:%M:%S")) # % are placeholders to print the variables to.