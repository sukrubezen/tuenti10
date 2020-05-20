T = input()

for i in xrange(T):
    N = input()

    s = set()
    lost = set()
    for _ in xrange(N):
        a, b, c = map(int, raw_input().split())

        if c == 1:
            lost.add(b)
            s.discard(b)
            if a not in lost:
                s.add(a)
        else:
            lost.add(a)
            s.discard(a)
            if b not in lost:
                s.add(b)

    print "Case #%d: %d" % (i+1, list(s)[0])