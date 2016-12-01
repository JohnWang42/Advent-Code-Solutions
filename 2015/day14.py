import re

def calcDist(reindeer, time):
    dist = {}
    for name, r in reindeer.iteritems():
        laps = time / (r['maxtime'] + r['rest'])
        remain = time % (r['maxtime'] + r['rest'])
        currDist = laps * r['maxtime'] * r['speed']
        if remain > r['maxtime']:
            currDist += r['speed'] * r['maxtime']
        else:
            currDist += r['speed'] * remain
        dist[name] = currDist
    return dist

data = open('input-day14.txt', 'r').read().split('\n')
reindeer = {}
scoreboard = {}
for line in data:
    if line:
        speed = re.findall(u'(^[a-zA-Z]+) can fly ([0-9]+) km/s for ([0-9]+) seconds, but then must rest for ([0-9]+) seconds.', line)[0]
        scoreboard[speed[0]] = 0
        reindeer[speed[0]] = {
            'speed' : int(speed[1]),
            'maxtime' : int(speed[2]),
            'rest' : int(speed[3])
        }
results = calcDist(reindeer, 2503)
far = 0
for r in results:
    if results[r] > far:
        far = results[r]
print 'Farthest reindeer: ' +  str(far)

for t in range(1, 2504):
    scorers = []
    results = calcDist(reindeer, t)
    far = 0
    for r in results:
        if results[r] > far:
            far = results[r]
            scorers = [r]
        elif results[r] == far:
            scorers.append(r)
    for s in scorers:
        scoreboard[s] += 1
highscore = 0
for r, s in scoreboard.iteritems():
    if s > highscore:
        highscore = s
print 'Highscore: ' + str(highscore)
