# imports the argv module from the library sys
from sys import argv

# passes the name of the script and the name of a single filename to two variables.
script, input_file = argv

# defines a function that takes a file object and prints it using the read function.
def print_all(f):
    print f.read()

# Sets the position from where the file will be read/written. Defaults to absolute positioning. This function moves the pointer to the start of the file.
def rewind(f):
    f.seek(0)

# prints out the number stored in a variable, followed by a single line from the input file.
def print_a_line(line_count, f):
    print line_count, f.readline()

# opens the file object and passes it to a variable
current_file = open(input_file)

print "First let's print the whole file:\n"

# calls the print all function, which prints the contents using "read"
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# calls the 'rewind' function, moving the pointer to the start of the file.
rewind(current_file)

print "Let's print three lines:"

# each of these prints a single line, using a variable that is manually iterated to keep track of line numbers.
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
