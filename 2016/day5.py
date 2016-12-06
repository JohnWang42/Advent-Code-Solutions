# Day 5
import md5
data = "ffykfhsq"
pw = ''
ind = 1

while len(pw) < 8:
    hsh = md5.new(data + str(ind)).hexdigest()
    if hsh[0:5] == "00000":
        pw += str(hsh[5])
    ind += 1
print pw
