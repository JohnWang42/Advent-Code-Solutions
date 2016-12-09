# Day 17
import binascii
data = open('input-day17.txt', 'r').read().split('\n')
containers = []
for row in data:
    containers.append(int(row))
bits = len(containers)
target = 150
combos = 0
minbits = "1" * bits
mincombos = 0
for c in range(int("1" * bits, 2)):
    curr = bin(c)[2:].zfill(bits)
    csum = 0
    for i in range(len(curr)):
        if curr[i] == "1":
            csum += containers[i]
    if csum == target:
        combos += 1
        if curr.count('1') < minbits.count('1'):
            minbits = curr
            mincombos = 1
        elif curr.count('1') == minbits.count('1'):
            mincombos += 1
print "Combos: " + str(combos)
print "Combos with minimum containers: " + str(mincombos)
