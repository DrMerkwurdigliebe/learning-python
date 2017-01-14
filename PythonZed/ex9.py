# passes a long string containing the days of the weeks to the variable 'days'
days = "Mon Tue Wed Thu Fri Sat Sun"
# passes a string to the variable days. uses new lines between them.
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# prints the days and appends the days variable
print "Here are the days: ", days
# prints the months and appends the monts variable. should have new lines beteen the months.
print "Here are the months: ", months

# haven't seen this before - interested to see what the triple quotes do. Perhaps print it exactly like it looks on the page, with new lines and everything?
print """
There's something going on here.
With the three double-quotes.
We'll be able to write as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
