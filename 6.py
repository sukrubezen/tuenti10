import socket
import time

s = socket.socket()
s.connect(("steam-origin.contest.tuenti.net", 2003))

def rec(s):
    check =  s.recv(1024)
    print (check)
    return check.split(b"---")[0].split(b"\n")

def convert(i, j):
    result = b""
    if i > 0:
        result += b"%dd" % i
    else:
        result += b"%du" % -i

    if j > 0:
        result += b"%dr" % j
    else:
        result += b"%dl" % -j

    return result


x, y = 0, 0
px, py = x, y+1

visited = set()
field = rec(s)
def walk(x, y):
    global field
    print (x, y, visited)
    visited.add((x, y))
    for i, j in [[1, 2], [1, -2], [2, -1], [2, 1], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]:
        if field[2+i][2+j] == 35:
            continue

        #print ("====>>", field, i, j, convert(i, j), field[2+i][2+j])
        # try walking
        if (x+i, y+j) not in visited:
            s.send(convert(i, j))
            time.sleep(0.2)
            field = rec(s)
            walk(x+i, y+j)
            s.send(convert(-i, -j))
            time.sleep(0.2)
            field = rec(s)

walk(x, y)