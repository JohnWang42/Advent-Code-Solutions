import re

def process(data):
    answ = ''
    for row in data:
        for group in row:
            if group != '':
                answ += str(len(group)) + str(group[0])
    return answ

inpt = '1321131112'
for i in range(0, 40):
    search = re.findall('(0+)|(1+)|(2+)|(3+)|(5+)|(6+)|(7+)|(8+)|(9+)', inpt)
    inpt = process(search)
print 'Part 1: ' + str(len(inpt))
inpt = '1321131112'
for i in range(0, 50):
    search = re.findall('(0+)|(1+)|(2+)|(3+)|(5+)|(6+)|(7+)|(8+)|(9+)', inpt)
    inpt = process(search)
print 'Part 2: ' + str(len(inpt))
