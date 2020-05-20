import binascii
import tarfile
import traceback
import multiprocessing as mp
from copy import deepcopy

def gf2_matrix_square(square, mat):
    for n in range(0, 32):
        if (len(square) < (n + 1)):
            square.append(gf2_matrix_times(mat, mat[n]))
        else:
            square[n] = gf2_matrix_times(mat, mat[n])
    return square

def gf2_matrix_times(mat, vec):
    sum = 0
    i = 0
    while vec:
        if (vec & 1):
            sum = sum ^ mat[i]
        vec = (vec >> 1) & 0x7FFFFFFF
        i = i + 1
    return sum

dp = {}
def crc32_combine(crc1, crc2, len2):
    key = (crc1, crc2, len2)
    if key in dp:
        return dp[key]

    even = []
    odd = []
    if (len2 == 0):
        return crc1

    odd.append(0xEDB88320)
    row = 1

    for n in range(1, 32):
        odd.append(row)
        row = row << 1

    even = gf2_matrix_square(even, odd)
    odd = gf2_matrix_square(odd, even)

    while (len2 != 0):
        even = gf2_matrix_square(even, odd)
        if (len2 & 1):
            crc1 = gf2_matrix_times(even, crc1)
        len2 = len2 >> 1

        if (len2 == 0):
            break

        odd = gf2_matrix_square(odd, even)
        if (len2 & 1):
            crc1 = gf2_matrix_times(odd, crc1)
        len2 = len2 >> 1

    crc1 = crc1 ^ crc2
    dp[key] = crc1
    return crc1

"""
import zlib

a = zlib.crc32(b"\x00")
b = zlib.crc32(b"\x11")
c = zlib.crc32(b"\x00\x11")

print (a, b, c)
print (crc32_combine(a, b, 1))
"""

f = tarfile.open("animals.tar.gz")
dd = {}
for elem in f.getmembers():
    key = elem.name.split("/")[-1]
    dd[key] = elem

def create_table():
    a = []
    for i in range(256):
        k = i
        for j in range(8):
            if k & 1:
                k ^= 0x1db710640
            k >>= 1
        a.append(k)
    return a

crc_table = create_table()

def crc_update(f, ti, ll, crc):
    #print (ll)
    crc ^= 0xffffffff

    cind = 0
    lind = 0
    results = []
    with f.extractfile(ti) as me:
        updateExists = False
        while True:
            try:
                if lind < len(ll) and ll[lind][0] == cind:
                    if not updateExists:
                        lind += 1
                        cind += 1
                        results.append(None)
                        continue

                    results.append(crc ^ 0xffffffff)
                    updateExists = False
                    crc = 0 ^ 0xffffffff
                    #crc = (crc >> 8) ^ crc_table[(crc & 0xff) ^ ll[lind][1]]
                    lind += 1
                    cind += 1
                else:
                    keep = me.read(1)
                    if keep == b"":
                        if len(ll) == lind:
                            break
                        else:
                            continue

                    updateExists = True
                    #print (keep)
                    keep = int.from_bytes(keep, "big")
                    crc = (crc >> 8) ^ crc_table[(crc & 0xff) ^ keep]
                    cind += 1

                #print (crc ^ 0xffffffff)
                #print ("%08x" % (crc ^ 0xffffffff))

            except Exception as e:
                print (traceback.format_exc())
                break

            #if cind % 10000000 == 0:
             #   print (cind)
        if updateExists:
            #print ("here2")
            results.append(crc ^ 0xffffffff)
        else:
            results.append(None)

    return results, cind-1
    #return crc ^ 0xffffffff


inps = []
while True:
    try:
        name, count = input().split(" ")
        count = int(count)

        inps.append([name, count, []])

        ll = []
        for i in range(count):
            ind, b = map(int, input().split())

            found = False
            itr = 0
            while itr < len(ll):
                if ll[itr][0] < ind:
                    itr += 1
                    continue

                ll = ll[:itr] + [[ind, b, i]] + ll[itr:]
                for i in range(itr+1, len(ll)):
                    ll[i][0] += 1
                found = True
                break

            if not found:
                ll.append([ind, b, i])

            inps[-1][-1].append(deepcopy(ll))

    except:
        break


def process(ind):
    global f, dd, inps

    name, count, ll = inps[ind]

    results = []

    if len(ll) == 0:
        o = []
    else:
        o = ll[-1]

    parts, leng = crc_update(f, dd[name], o, 0)
    #print (parts, o, name, count, leng)


    # no insertion
    crcnow = 0
    for i in range(len(o)):
        if i == 0:
            if parts[0] is not None:
                crcnow = parts[0]
        else:
            if parts[i] is not None:
                crcnow = crc32_combine(crcnow, parts[i], o[i][0] - o[i-1][0]-1)

    if parts[-1] is not None:
        if len(o) == 0:
            crcnow = crc32_combine(crcnow, parts[-1], leng)
        else:
            crcnow = crc32_combine(crcnow, parts[-1], leng - o[-1][0])

    results.append("%s %d: %08x" % (name, 0, crcnow))

    # insertions
    for insertion_itr in range(count):
        crcnow = 0
        for i in range(len(o)):
            if i == 0:
                if parts[0] is not None:
                    crcnow = parts[0]
            else:
                if parts[i] is not None:
                    crcnow = crc32_combine(crcnow, parts[i], o[i][0] - o[i-1][0]-1)

            #print ("before insertion", crcnow)

            if o[i][2] <= insertion_itr:
                #print ("entering ll", o[i][2])
                init = crcnow ^ 0xffffffff
                crcnow = (init >> 8) ^ crc_table[(init & 0xff) ^ o[i][1]]
                crcnow ^= 0xffffffff
                #crcnow = crc32_combine(crcnow, o[i][1], 1)

            #print ("==>>", name, insertion_itr+1, crcnow)


        if parts[-1] is not None:
            if len(o) == 0:
                crcnow = crc32_combine(crcnow, parts[-1], leng)
            else:
                crcnow = crc32_combine(crcnow, parts[-1], leng - o[-1][0])

        results.append("%s %d: %08x" % (name, insertion_itr+1, crcnow))

    fff = open("log", "a")
    fff.write("%d DONE\n" % ind)
    fff.write(str(results))
    fff.write("\n")
    fff.flush()
    fff.close()

    return results

pool = mp.Pool(mp.cpu_count()-1)
hede = pool.map(process, range(len(inps)))
for elem in hede:
    for ee in elem:
        print (ee)

