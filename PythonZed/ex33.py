def thenumbers():
    i = 0
    numbers = []

    while i < 6:
        print "At the top of i is %d" % i
        numbers.append(i)

        i += 1
        print "Numbers now: ", numbers
        print "At the bottom is is %d" % i


    print "The numbers: "

    for num in numbers:
        print num
