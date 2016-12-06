# Day 5 Part 2
from __future__ import print_function
import md5
data = "ffykfhsq"
pw = '________'
ind = 1

while '_' in pw:
    hsh = md5.new(data + str(ind)).hexdigest()
    print("Password: " + pw + " | Checking hash: " + hsh, end='\r')
    pwInd = -1
    if hsh[5].isdigit():
        pwInd = int(hsh[5])
    if hsh[0:5] == "00000" and pwInd != -1 and pwInd >= 0 and pwInd < 8 and pw[pwInd] == '_':
        pw = pw[:pwInd] + hsh[6] + pw[(pwInd + 1):]
    ind += 1
print(pw)
