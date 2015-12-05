data = open('input-day1.txt', 'r').read()
instruct = {'(' : 1, ')' : -1};
floor = 0
negPos = -1
for i, d in enumerate(data):
    floor += instruct[d]
    if(floor < 0 and negPos == -1):
        negPos = i + 1
        trig = True
print "Santa stops at floor: "  + str(floor)
print "Santa enters the basement at line: " + str(negPos)
