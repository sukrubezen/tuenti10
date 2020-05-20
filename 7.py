f = open("submitInput (4).txt", "r")

lines = f.readlines()

from string import maketrans

QWERTY = '''-=qwertyuiop[]sdfghjkl;'zxcvbn,./_+QWERTYUIOP{}SDFGHJKL:"ZXCVBN<>?'''
DVORAK = '''[]',.pyfgcrl/=oeuidhtns-;qjkxbwvz{}"<>PYFGCRL?+OEUIDHTNS_:QJKXBWVZ'''
TRANS = maketrans(DVORAK, QWERTY)

for i in xrange(1, len(lines)):
    print "Case #%d: %s" % (i, lines[i].strip("\n").translate(TRANS))