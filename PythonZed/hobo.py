# Hobo

# some variables to help capture the different things people might write.
north = ['north', 'nrth', 'nth']
south = ['south', 'South', 'sth']
east = ['east', 'est']
west = ['west', 'wst']
look = ['look', 'lk', 'lok']
described = False




# prints a simple help text
def help():
    print """    ----------
    Welcome hobo! Life hasn't been kind to you, has it? Thanks to it's twists
    and turns you find yourself alienated from the rest of society and with
    meagre resources at your disposal. Luckily, you have your trusty bindle and
    your wits! Money is for capitalist pigdog fools! You can always USE
    something in your bindle, LOOK around you or LOOK at something more closely,
    and USE one item on another. You can CHECK your bindle or TAKE something for
    your bindle. You can move available directions.

    Good luck hobo!
    ----------
    """

def start():
    help()
    pathway()

def pathway():
    description = """    You're standing on the footpath outside a large old-
    fashioned wooden villa. SOUTH is a busy road. EAST the pathway stretches
    interminably past similar houses. To the WEST the pathway also stretches on,
    leading you past many, many homes. So many homes, and yet you don't have
    one! You must have done something wrong with your life. To the NORTH is a
    white picket fence, an open gate and the enormous house. It beckons you.
    """
    choice = raw_input("> ").lower()

    if choice in north:
        print """    As you pass through the gate, the picket fence reminds you
        of a row of even, white teeth."""
    elif choice in south:
        print "you went south"
    elif choice in east:
        print "You went east"
    elif choice in look:
        if 'fence' or 'picket' in choice:
            print """    On closer inspection, you notice symbols scratched on
            one of the palings. You recognise hobo marks, code left by other
            hobos offering advice about the house they stand before. You
            recognise the symbol for 'food', 'no dogs' and something that could
            be either 'mass hobo grave in yard' or 'warm fire'. Funny how those
            two symbols look so similar."""
    else:
        print "You went nowhere"

start()
