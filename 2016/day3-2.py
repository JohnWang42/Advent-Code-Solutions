# Day 3 Part 2
import re

data = open('input-day3.txt', 'r').read().split('\n')
regex = r"[0-9]{1,}"
tricount = 0
sides = []

for row in data:
    matches = re.findall(regex, row)
    s = []
    for m in matches:
        s.append(int(m))
    sides.append(s)
    if len(sides) == 3:
        for i in range(0, 3):
            if sides[0][i] + sides[1][i] > sides[2][i] and \
            sides[0][i] + sides[2][i] > sides[1][i] and \
            sides[1][i] + sides[2][i] > sides[0][i]:
                tricount += 1
        sides = []
print tricount

