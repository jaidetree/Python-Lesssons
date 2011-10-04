def counter(limit, step):
    '''Counts until limit by amount specified as the step'''

    numbers = []
    i = 0

    # while i < limit:
    for i in range(0, limit, step):
        print "At the top i is %d" % i
        numbers.append(i)
        # i += step
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

counter(28, 4)
counter(6, 2)

