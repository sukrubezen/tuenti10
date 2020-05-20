T = input()


def count(S, m, n):
    table = [[0 for x in range(m)] for x in range(n+1)]

    for i in range(m):
        table[0][i] = 1

    for i in range(1, n+1):
        for j in range(m):

            # Count of solutions including S[j]
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0

            # Count of solutions excluding S[j]
            y = table[i][j-1] if j >= 1 else 0

            # total count
            table[i][j] = x + y

    return table[n][m-1]

for t in xrange(T):
    ll = map(int, raw_input().split())

    num, nono = ll[0], set(ll[1:])

    ll = []
    for i in xrange(1, num):
        if i not in nono:
            ll.append(i)

    if len(ll) == 0:
        print "Case #%d: %d" % (t+1, 0)
        continue

    print "Case #%d: %d" % (t+1, count(ll, len(ll), num))