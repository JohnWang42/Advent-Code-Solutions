# Day 16
import re

match = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}
data = open('input-day16.txt', 'r').read().split('\n')
auntInfoReg = r"([a-z]+): ([0-9]+)"
auntCount = 1

for row in data:
    info = {}
    auntmatch = True
    for stat in re.findall(auntInfoReg, row):
        auntmatch = match[stat[0]] == int(stat[1])
        if not auntmatch:
            break
    if auntmatch:
        print auntCount
        break
    auntCount += 1
