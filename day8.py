import re

data = open('input-day8.txt', 'r').read().split('\n')
totalCharCode = 0
totalStrData = 0
for line in data:
    totalCharCode += len(line)
    reg = re.compile(ur'(\\x[A-Fa-f0-9]{1,2})|(\\\\)|(\\")|([a-zA-Z0-9])')
    codes = re.findall(reg, line)
    totalStrData += len(codes)
originalCharCount = totalCharCode
print 'Part 1 Answer: ' + str(totalCharCode - totalStrData)

totalCharCode = 0
for line in data:
    newStr = ""
    reg = re.compile(ur'(\\x[A-Fa-f0-9]{1,2})|(\\\\)|(\\")|([a-zA-Z0-9])')
    codes = re.findall(reg, line)
    for char in codes:
        for c in char:
            if(c == ur'\"'):
                newStr += ur'\\' + c
            elif(ur'\x' in c):
                newStr += '\\' + c
            elif(ur'\\' in c):
                newStr += '\\\\' + c
            else:
                newStr += c
    newStr = ur'"\"' + newStr + ur'\""'
    totalCharCode += len(newStr)
print 'Part 2 Answer: ' + str(totalCharCode - originalCharCount)
