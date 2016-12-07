# Day 7 Part 2
import re
data = open('input-day7.txt', 'r').read().split('\n')
reg = r"(\[*[a-z]+\]*)"
count = 0

#check for ABAs and return array of BABs
def checkABA(line):
    aba = []
    for i in range(0, len(line) - 2):
        if line[i] == line[i + 2] and line[i] != line[i + 1]:
            aba.append(line[i:i + 2])
    return aba


for row in data:
    ip = re.findall(reg, row)
    inside = []
    outside = []
    abas = []
    for grp in ip:
        if grp[0] == '[':
            inside.append(grp.replace('[', '').replace(']', ''))
        else:
            outside.append(grp)
    for ot in outside:
        for a in checkABA(ot):
            abas.append(a)
    if len(abas) > 0:
        for insd in inside:
            valid = False
            for insdAba in checkABA(insd):
                for outAba in abas:
                    if insdAba[0] == outAba[1] and insdAba[1] == outAba[0]:
                        valid = True
                        break
                if valid:
                    break
            if valid:
                count += 1
                break
print count
