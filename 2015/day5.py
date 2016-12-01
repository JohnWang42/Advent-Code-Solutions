import re
data = open('input-day5.txt', 'r').read().split('\n')
niceCount = 0
for row in data:
    nice = len(re.findall('[aeiou]', row)) >= 3 and len(re.findall('([a-z])\\1', row)) > 0 and len(re.findall('(ab)|(cd)|(pq)|(xy)', row)) == 0
    if(nice):
        niceCount += 1
print "Part 1: " + str(niceCount)

niceCount = 0
for row in data:
    nice = len(re.findall('(..).*\\1', row)) > 0 and len(re.findall('(.).\\1', row)) > 0
    if(nice):
        niceCount += 1
print "Part 2: " + str(niceCount)
