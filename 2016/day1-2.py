# Day 1 Part 2
data = open('input-day1.txt', 'r').read().split(',')

def turn(dir, curr):
    if dir == 'R':
        curr += 1
    if dir == 'L':
        curr -= 1
    if curr > 3:
        curr = 0
    if curr < 0:
        curr = 3
    return curr

def go(instr, x, y, cardinal):
    steps = []
    turndir = instr[0]
    dist = int(instr[1:])
    direction = turn(turndir, cardinal)
    if direction == 0:
        for inc in range(1, dist + 1):
            steps.append([x, y + inc])
        return [x, y + dist, direction, steps]
    if direction == 1:
        for inc in range(1, dist + 1):
            steps.append([x + inc, y])
        return [x + dist, y, direction, steps]
    if direction == 2:
        for inc in range(1, dist + 1):
            steps.append([x, y - inc])
        return [x, y - dist, direction, steps]
    if direction == 3:
        for inc in range(1, dist + 1):
            steps.append([x - inc, y])
        return [x - dist, y, direction, steps]

# 0 = North, 1 = East, 2 = South, 3 = West
steps = [[0,0]]
currdir = 0
currx = 0
curry = 0
found = False
for row in data:
    info = go(row.strip(), currx, curry, currdir)
    currx = info[0]
    curry = info[1]
    currdir = info[2]
    for st in info[3]:
        for s in steps:
            if st == s:
                print st
                print s
                print abs(s[0]) + abs(s[1])
                found = True
                break
        if found:
            break
    if found:
        break
    steps += info[3]
