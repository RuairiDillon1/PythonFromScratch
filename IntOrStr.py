# Basic program checking if the declared instances are int or str.

help(isinstance)

print(isinstance(25,int) or isinstance(25,str))     # leftmost statement is true,
print(isinstance([25],int) or isinstance([25],str)) # therefore the whole or statement is true.
print(isinstance("25",int) or isinstance("25",str))
