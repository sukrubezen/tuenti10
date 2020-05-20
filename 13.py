import sys
sys.setrecursionlimit(1000000)

def solve(h, a, b, limit):
    sofar = 0
    parent = None
    dec = True
    area = a*b*h

    while True:
        #print sofar, limit, h
        if sofar != 0:
            area = (2*a+2*b-4) * h

        if area > limit:
            return None

        if h == 2 and parent == 1:
            return sofar + area


        parent = h

        if dec:
            h -= 2
        else:
            h += 1

        dec = not dec
        limit -= area
        sofar += area

        a += 2
        b += 2


T = input()
for t in xrange(T):
    N = input()

    lower = 3
    upper = 10**9
    a = 1

    moxH = None
    while lower < upper:
        mid = (lower+upper) // 2
        mr = solve(mid, a, a, N)

        if mr is None:
            upper = mid-1
        else:
            if mid == lower:
                break
            lower = mid

    now = solve(lower, a, a, N)
    if now is not None:
        moxH = lower

    now = solve(lower+1, a, a, N)
    if now is not None:
        moxH = lower+1

    #print moxH

    if moxH is None:
        print "Case #%d: %s" % (t+1, "IMPOSSIBLE")
    else:
        result = 0
        lower = 1
        upper = 10**10
        while lower < upper:
            #print lower, upper
            mid = (lower+upper) // 2
            mr = solve(moxH, mid, mid, N)

            if mr is None:
                upper = mid-1
            else:
                if mid == lower:
                    break
                lower = mid

        #print lower, moxH
        now = solve(moxH, lower, lower, N)
        if now is not None:
            result = max(result, now)

        now = solve(moxH, lower, lower+1, N)
        if now is not None:
            result = max(result, now)

        now = solve(moxH, lower+1, lower+1, N)
        if now is not None:
            result = max(result, now)

        now = solve(moxH, lower+1, lower+2, N)
        if now is not None:
            result = max(result, now)


        print "Case #%d: %d %d" % (t+1, moxH, result)

#print solve(3, 1, 1, 20)