# imports the module argv from the library sys
from sys import argv

# passes commandline arguments to two variables. script takes the name of this file and filename the filename entered at the commandline.
script, filename = argv

# passes the file object to the variable txt
txt = open(filename)

# prints the name of the file
print "Here's your file %r:" % filename
# uses the read command to read the file object, then uses print to send it to standard output.
print txt.read()

txt.close()
