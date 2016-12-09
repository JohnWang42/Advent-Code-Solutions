# Day 9
import re
data = open('input-day9.txt', 'r').read()
expreg = r"\(([0-9]+)x([0-9]+)\)"
stringreg = r"([A-Z]+)"
total = 0
while len(data) > 0:
    if data[0] == '(':
        expand = re.search(expreg, data).groups()
        strlen = int(expand[0])
        exp = int(expand[1])
        rmv = len(expand[0]) + len(expand[1]) + 3
        total += strlen * exp
        data = data[(strlen + rmv):]
    else:
        rmv = re.search(stringreg, data)
        total += len(rmv.group(0))
        data = data[(len(rmv.group(0))):]
print total
