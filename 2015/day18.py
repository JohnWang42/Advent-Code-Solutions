# Day 18
data = open('input-day18.txt', 'r').read().split('\n')
grid = []
for row in data:
    grid.append([])
    for point in row:
        grid[len(grid) - 1].append(point)
nextgrid = grid[:]

for loop in range(100):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            neigbors = 0
            for y in range(-1, 2):
                if neigbors > 3:
                    break
                ychk = row + y
                for x in range( -1, 2):
                    xchk = col + x
                    if ychk >= 0 and ychk < len(grid) and xchk >= 0 and xchk < len(grid[row]) and grid[ychk][xchk] == '#':
                        if str(y) + str(x) != "00":
                            neigbors += 1
            if grid[row][col] == '#' and neigbors != 2 and neigbors != 3:
                nextgrid[row][col] = "."
            elif grid[row][col] == '.' and neigbors == 3:
                nextgrid[row][col] = '#'
    grid = nextgrid[:]

total = 0
for row in grid:
    for el in row:
        if el == '#':
            total += 1
print total
