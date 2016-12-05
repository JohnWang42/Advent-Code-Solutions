# Day 1
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
    turndir = instr[0]
    dist = int(instr[1:])
    direction = turn(turndir, cardinal)
    if direction == 0:
        return [x, y + dist, direction]
    if direction == 1:
        return [x + dist, y, direction]
    if direction == 2:
        return [x, y - dist, direction]
    if direction == 3:
        return [x - dist, y, direction]

# 0 = North, 1 = East, 2 = South, 3 = West
currdir = 0
currx = 0
curry = 0
for row in data:
    info = go(row.strip(), currx, curry, currdir)
    currx = info[0]
    curry = info[1]
    currdir = info[2]
print abs(currx) + abs(curry)
