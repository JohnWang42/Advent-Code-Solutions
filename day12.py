import re
import json

def sumJson(data, sum = 0):
    total = 0
    inval = False
    if isinstance(data, dict):
        for key, value in data.iteritems():
            if str(value) == 'red':
                inval = True
                break
            if isinstance(value, dict) or isinstance(value, list):
                total += sumJson(value)
            else:
                if isinstance(value, int):
                    total += value
    else:
        for element in data:
            if isinstance(element, dict) or isinstance(element, list):
                total += sumJson(element)
            else:
                if isinstance(element, int):
                    total += element
    if inval:
        total = 0
    return total


data = open('input-day12.txt', 'r').read()
numbers = map(int, re.findall('([0-9]+|-[0-9]+)', data))
print "First Part Answer: " + str(sum(numbers))

jsonData = json.loads(data)
print "Second Part Answer: " + str(sumJson(jsonData))
