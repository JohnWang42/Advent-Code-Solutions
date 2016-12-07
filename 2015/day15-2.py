# Day 15 Part 2
import re

def cookiescore(ingrd, amt):
    score = [0, 0, 0, 0]
    cal = 0
    for name, val in ingrd.iteritems():
        for i in range(0, len(score)):
            score[i] += val[i] * amt[name]
        cal += val[4] * amt[name]
        if cal > 500:
            return 0
    mult = 1
    for s in range(0, len(score)):
        if score[s] > 0:
            mult *= score[s]
        else:
            mult = 0
            break
    return mult

data = open('input-day15.txt', 'r').read().split('\n')
reg = r"([A-Za-z]*): capacity ([\-0-9]*), durability ([\-0-9]*), flavor ([\-0-9]*), texture ([\-0-9]*), calories ([\-0-9]*)"
ingrd = {}
total = 100

for row in data:
    info = re.findall(reg, row)[0]
    ingrd[info[0]] = [int(info[1]), int(info[2]), int(info[3]), int(info[4]), int(info[5])]

amt = {}
high = 0
for a in range(100, -1, -1):
    for b in range(100 - a, -1, -1):
        for c in range(100 - a - b, -1 , -1):
            for d in range(100 - a - b - c, -1, -1):
                i = 0
                for name, val in ingrd.iteritems():
                    if i == 0:
                        amt[name] = a
                    if i == 1:
                        amt[name] = b
                    if i == 2:
                        amt[name] = c
                    if i == 3:
                        amt[name] = d
                    i += 1
                newscore = cookiescore(ingrd, amt)
                if high < newscore:
                    high = newscore
print high
