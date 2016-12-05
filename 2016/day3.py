# Day 3
import re

data = open('input-day3.txt', 'r').read().split('\n')
regex = r"[0-9]{1,}"
tricount = 0

for row in data:
    sides = []
    matches = re.findall(regex, row)
    for m in matches:
        sides.append(int(m))
    valid = (sides[0] + sides[1] > sides[2]) and (sides[0] + sides[2] > sides[1]) and (sides[1] + sides[2] > sides[0])
    if valid:
        tricount += 1
print tricount

