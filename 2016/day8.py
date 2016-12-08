# Day 8 Part & 2
import re
data = open('input-day8.txt', 'r').read().split('\n')
recreg = r"rect ([0-9]+)x([0-9]+)"
rotreg = r"rotate (row|column)? [xy]{1}=([0-9]+) by ([0-9]+)"
screen = []
height = 6
width = 50
for y in range(height):
    screen.append([False] * width)


for row in data:
    if 'rect' in row:
        dim = re.findall(recreg, row)[0]
        for y in range(0, int(dim[1])):
            for x in range(0, int(dim[0])):
                screen[y][x] = True
    else:
        print row
        instr = re.findall(rotreg, row)[0]
        if instr[0] == 'column':
            col = int(instr[1])
            mv = int(instr[2]) % height
            temp = [False] * height
            for y in range(height):
                if screen[y][col]:
                    temp[(y + mv) % height] = True
            for y in range(height):
                screen[y][col] = temp[y]
        else:
            row = int(instr[1])
            mv = int(instr[2]) % width
            temp = [False] * width
            for x in range(width):
                if screen[row][x]:
                    temp[(x + mv) % width] = True
            screen[row] = temp[:]

count = 0
for y in screen:
    line = ''
    for x in y:
        if x:
            line += '#'
            count += 1
        else:
            line += '.'
    print line
print 'Active Pixels :' + str(count)
