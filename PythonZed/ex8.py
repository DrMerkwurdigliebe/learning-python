# passes a string to the variable formatter. The string contains a series of placeholders.
formatter = "%r %r %r %r"

# Prints the string containing the placeholders and those are then passed some numbers.
print formatter % (1, 2, 3, 4)
# Again, prints the string with the placeholders which are passed strings. Because the string contains the 'raw' placeholder, it shouldn't matter what type of content is passed to it.
print formatter % ("one", "two", "three", "four")
# Passes booleans to the placeholders.
print formatter % (True, False, False, True)
# This one's interesting: it passes the string to print, then the string into the placeholders. Should resolve into a string made of a series of strings with the placeholders in them (but not further resolved.)
print formatter % (formatter, formatter, formatter, formatter)
# Series of strings, separated by commas which should resolve into spaces on a single line.
print formatter % (
    "I had this thing.",
    "that you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
