import re

data = open('input-day6.txt', 'r').read().split('\n')
grid = [None]*1000
for i, row in enumerate(grid):
    grid[i] = [False]*1000
for i, line in enumerate(data):
    if(line != ''):
        posList = re.findall('([0-9]{1,3}),([0-9]{1,3})', line)
        for posy in range(int(posList[0][1]), int(posList[1][1]) + 1):
            for posx in range(int(posList[0][0]), int(posList[1][0]) + 1):
                if('turn off' in line):
                    grid[posx][posy] = False
                if('turn on' in line):
                    grid[posx][posy] = True
                if('toggle' in line):
                    grid[posx][posy] = not (grid[posx][posy])

lightsOn = 0
for row in grid:
    lightsOn += sum(row)
print 'Lights On: ' + str(lightsOn)

grid = [None]*1000
for row in range(0, 1000):
    grid[row] = [0]*1000

for i, line in enumerate(data):
    if(line != ''):
        posList = re.findall('([0-9]{1,3}),([0-9]{1,3})', line)
        for posy in range(int(posList[0][1]), int(posList[1][1]) + 1):
            for posx in range(int(posList[0][0]), int(posList[1][0]) + 1):
                if('turn off' in line):
                    if(grid[posx][posy] != 0):
                        grid[posx][posy] -= 1
                if('turn on' in line):
                    grid[posx][posy] += 1
                if('toggle' in line):
                    grid[posx][posy] += 2
lightsOn = 0
for row in grid:
    lightsOn += sum(row)
print 'Total Brightness: ' + str(lightsOn)
