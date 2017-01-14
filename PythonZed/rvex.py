from sys import argv

script, filename = argv

print "I'm now opening:", filename
target = open(filename, 'r')

print "I read %s, now I'm going to display it for you:" % filename

print target.read()
target.close()
