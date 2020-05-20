# -*- coding: utf-8 -*-


txt = open("pg17013.txt").read()

l = "a, b, c, d, e, f, g, h, i, j, k, l, m, n, ñ, o, p, q, r, s, t, u, v, w, x, y, z, á, é, í, ó, ú, ü".split(', ')

txt = txt.lower()
ll = []
for ch in txt:
    if ch not in l:
        ll.append(" ")
    else:
        ll.append(ch)

txt = "".join(ll)

words = txt.split(" ")
words = list(filter(lambda x: len(x) >= 3, words))

from collections import Counter

dd = Counter(words)
dk = list(dd.items())

dk.sort(key=lambda x: x[0])
dk.sort(key=lambda x: -x[1])

#for i in range(230):
#    print (i, dk[i])


wr = {}
for i in range(len(dk)):
    wr[dk[i][0]] = [i+1, dk[i][1]]

T = int(input())
for i in range(T):
    x = input()

    try:
        x = int(x)
        print ("Case #%d: %s %d" % (i+1, dk[x-1][0], dk[x-1][1]))
    except:
        print ("Case #%d: %d #%d" % (i+1, wr[x][1], wr[x][0]))



# ser 517  - 784
# amor 156 - 157