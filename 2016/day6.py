# Day 6
data = open('input-day6.txt', 'r').read().split('\n')
msg = []
for i in range(0, len(data[0])):
    msg.append({})

for row in data:
    for i in range(0, len(row)):
        if row[i] in msg[i]:
            msg[i][row[i]] += 1
        else:
            msg[i][row[i]] = 1

fixedMsg = ''
for pos in msg:
    fixedMsg += sorted(pos.iteritems(), key=lambda (k, v): (v, k))[::-1][0][0]
print fixedMsg
