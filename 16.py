T = input()

for t in xrange(T):
    F, G = map(int, raw_input().split())

    dd = {}
    groups = []
    for i in xrange(G):
        E, N = map(int, raw_input().split())
        ll = map(int, raw_input().split())
        groups.append([E, ll])

        for elem in ll:
            if elem not in dd:
                dd[elem] = set()

            dd[elem].add(i)


    results = [None for _ in xrange(F)]

    eliminated = 0
    while eliminated < len(groups):
        for floor in xrange(F):
            if floor not in dd:
                continue

            now = dd[floor]
            temp = []

            moxneeded = None
            moxInd = None
            for ind in now:
                if groups[ind][0] == 0:
                    continue

                hede = float(groups[ind][0]) / len(groups[ind][1])
                if moxneeded is None or moxneeded < hede:
                    moxneeded = hede
                    moxInd = ind

            if moxInd is not None:
                if results[floor] is None:
                    results[floor] = 0

                results[floor] += 1
                groups[moxInd][0] -= 1

                if groups[moxInd][0] == 0:
                    eliminated += 1

    print "Case #%d: %d" % (t+1, max(filter(lambda x: x is not None, results)))


