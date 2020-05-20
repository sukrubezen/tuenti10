s = "3633363A33353B393038383C363236333635313A353336"

out = "514;248;980;347;145;332"
itr = 0
key = []

for i in xrange(0, len(s), 2):
    now = int(s[i:i+2], 16)
    outi = ord(out[itr])

    key.append(now^outi)
    itr += 1

key.reverse()
print key

s = "3A3A333A333137393D39313C3C3634333431353A37363D"
itr = 0
msg = []

for i in xrange(0, len(s), 2):
    now = int(s[i:i+2], 16)
    ki = key[-itr-1]

    msg.append(chr(now^ki))
    itr += 1

print "".join(msg)