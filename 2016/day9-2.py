# Day 9 Part 2
import re
data = open('input-day9.txt', 'r').read()
expreg = r"\(([0-9]+)x([0-9]+)\)"
stringreg = r"([A-Z]+)"

def explode(strIn):
    total = 0
    if strIn[0] == '(':
        # find string length and expansion factor
        expand = re.search(expreg, strIn).groups()
        strlen = int(expand[0])
        exp = int(expand[1])
        # calculate length of string length and exp factor
        rmv = len(expand[0]) + len(expand[1]) + 3
        # get string we are exploding
        expStr = strIn[rmv:(strlen + rmv)]
        # remove processed data
        strIn = strIn[(strlen + rmv):]
        total += exp * explode(expStr)
    else:
        # calculate length of a regular string
        rmv = re.search(stringreg, strIn)
        total += len(rmv.group(0))
        strIn = strIn[(len(rmv.group(0))):]
    # if there is data left continure processing
    if len(strIn) > 0:
        total += explode(strIn)
    return total

print explode(data)
