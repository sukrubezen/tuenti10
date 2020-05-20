T = input()

for i in xrange(T):
    a, b = raw_input().split()

    if a == "R":
        if b == "S":
            print "Case #%d: %s" % (i+1, "R")
        elif b == "P":
            print "Case #%d: %s" % (i+1, "P")
        else:
            print "Case #%d: %s" % (i+1, "-")

    elif a == "S":
        if b == "R":
            print "Case #%d: %s" % (i+1, "R")
        elif b == "P":
            print "Case #%d: %s" % (i+1, "S")
        else:
            print "Case #%d: %s" % (i+1, "-")

    elif a == "P":
        if b == "S":
            print "Case #%d: %s" % (i+1, "S")
        elif b == "P":
            print "Case #%d: %s" % (i+1, "-")
        else:
            print "Case #%d: %s" % (i+1, "P")
