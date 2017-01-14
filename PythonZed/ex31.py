prompt = ("> ")

print "WELCOME TO KROZ"

print "You are standing on a beach, watching your ship sink into the waves. Exhausted and soaking wet, you are faced with a decision."
print "1. Search the shore for survivors."
print "2. Search the shore for useable loot."
print "3. Stumble inland."



beach = raw_input(prompt)

if beach == "1":
    print "There are no survivors."

elif beach == "2":
    print "There is no loot."

else:
    print "You stumble inland."

door = raw_input(prompt)

if door == "1":
    print "There's a giant bear here eating a cheesecake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. GOod job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

else:
    print "You stumble around and fall on a knife and die. Good job!"
