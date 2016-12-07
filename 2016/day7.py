# Day 7
import re
data = open('input-day7.txt', 'r').read().split('\n')
reg = r"(\[*[a-z]+\]*)"
count = 0

def checkABBA(line):
    for i in range(0, len(line) - 3):
        if line[i] + line[i + 1] == line[i + 3] + line[i + 2] and line[i] != line[i + 1]:
            return True
    return False


for row in data:
    ip = re.findall(reg, row)
    outside = False
    inside = False
    for grp in ip:
        if grp[0] == '[':
            inside = not checkABBA(grp.replace('[', '').replace(']', ''))
            if not inside:
                break
        else:
            outside = outside or checkABBA(grp)
    if outside and inside:
        count += 1
print count