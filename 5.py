N = input()

for t in xrange(N):
    now = input()
    k, rem = now//20, now%20

    if 0 <= rem <= 9*k:
        print "Case #%d: %d" % (t+1, k)
    else:
        print "Case #%d: IMPOSSIBLE" % (t+1)