# Day 2
data = open('input-day2.txt', 'r').read().split('\n')
# keypad data arranged so that 0,0 correlates to the bottom left of the keypad
keypad = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
position = [1,1]
code = ''

for row in data:
    for instr in row:
        if instr == 'U' and position[1] < 2:
            position[1] += 1
        if instr == 'D' and position[1] > 0:
            position[1] -= 1
        if instr == 'L' and position[0] > 0:
            position[0] -= 1
        if instr == 'R' and position[0] < 2:
            position[0] += 1
    print position
    code += str(keypad[position[1]][position[0]])
print code
            