# Day 4
import re
data = open('input-day4.txt', 'r').read().split('\n')

# checksum regex
checkReg = r"(?<=\[).*(?<!\])"
# encrypted name and sector id regex
nameIdReg = r"([a-z\-]+)([0-9]+)"
summation = 0

for row in data:
    checksum = re.findall(checkReg, row)[0]
    nameId = re.search(nameIdReg, row)
    name = nameId.group(1).replace('-', '')
    sectorId = int(nameId.group(2))
    tally = {}

    # tally characters
    for ch in name:
        if ch in tally:
            tally[ch] += 1
        else:
            tally[ch] = 1
    result = sorted(tally.iteritems(), key=lambda (k, v): (v, k))[::-1]
    start = 0
    compcode = ''
    while len(compcode) < 5:
        high = result[start][1]
        end = start
        if end < len(result):
            while end < len(result) and result[end][1] == high:
                end += 1
        if start != end - 1:
            for i in range(end - 1, start - 1, -1):
                if len(compcode) < 5:
                    compcode += result[i][0]
                else:
                    break
        else:
            compcode += result[start][0]
        start = end
    if checksum == compcode:
        summation += sectorId
print summation
