# Day 2 Part 2
data = open('input-day2.txt', 'r').read().split('\n')
# keypad data arranged so that 0,0 correlates to the bottom left of the keypad
keypad = [
    [-1, -1, 'D', -1, -1],
    [-1, 'A', 'B', 'C', -1],
    [5, 6, 7, 8, 9],
    [-1, 2, 3, 4, -1],
    [-1, -1, 1, -1, -1]
]
position = [2,2]
code = ''

for row in data:
    for instr in row:
        if instr == 'U' and position[1] < 4 and keypad[position[1] + 1][position[0]] != -1:
            position[1] += 1
        if instr == 'D' and position[1] > 0 and keypad[position[1] - 1][position[0]] != -1:
            position[1] -= 1
        if instr == 'L' and position[0] > 0 and keypad[position[1]][position[0] - 1] != -1:
            position[0] -= 1
        if instr == 'R' and position[0] < 4 and keypad[position[1]][position[0] + 1] != -1:
            position[0] += 1
    print position
    code += str(keypad[position[1]][position[0]])
print code
            