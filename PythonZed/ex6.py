

# Assigns the variable x to a string. The %d references a digit given at the end: 10
x = "There are %d types of people." % 10
# Gives the variable 'binary' the string 'binary'.
binary = "binary"
# ditto
do_not = "don't"
# passes a string to y, which is passed the variables binary and do_not which are then evaluated to their target strings.
y = "Those who know %s and those who %s." % (binary, do_not)

# Prints out the joke.
print x
# Prints the punchline
print y

# Prints the string and puts the raw input from the variable x out to it.
print "I said: %r." % x
# Prints the string and inputs the string from y into it. Makes use of single quotes inside double.
print "I also said: '%s'." % y

# Stores a boolean variable
hilarious = False
# another variable, this one which itself references a variable. That variable is not specified here
joke_evaluation = "Isn't that joke so funny?! %r"

# Prints the string variable and calls the boolean. Shows that a variable can hold a placeholder reference to another variable which doesn't have to be called at variable assignment - instead it can be referenced later.
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# Shows how the plus operator affects strings (by concatenating them).
print w + e
