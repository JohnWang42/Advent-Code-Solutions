import re
import copy

def routeHappy(nodes, path):
    if(len(path) == len(nodes)):
        return path
    happiest = None
    nextNode = None
    neighbors = nodes[path[len(path) - 1]]
    for n in neighbors:
        if happiest == None or happiest < neighbors[n]:
            if not n in path:
                happiest = neighbors[n]
                nextNode = n
    path.append(nextNode)
    return routeHappy(nodes, path)

def calcDist(path, nodes):
    dist = 0
    for i, p in enumerate(path):
        if(i < len(path) - 1):
            dist += nodes[path[i]][path[i + 1]]
    #complete loop
    dist += nodes[path[len(path) - 1]][path[0]]
    return dist

data = open('input-day13.txt', 'r').read().split('\n')
nodes = {}
for line in data:
    if(line):
        neg = 1
        nodeInfo = re.findall('(.+) would gain ([0-9]+) happiness units by sitting next to (.+).', line)
        if not nodeInfo:
            neg = -1
            nodeInfo = re.findall('(.+) would lose ([0-9]+) happiness units by sitting next to (.+).', line)
        person1 = nodeInfo[0][0]
        happ = int(nodeInfo[0][1]) * neg
        person2 = nodeInfo[0][2]
        if nodes.get(person1):
            if(nodes[person1].get(person2)):
                nodes[person1][person2] += happ
            else:
                nodes[person1][person2] = happ
        else:
            nodes[person1] = {person2 : happ}
        if nodes.get(person2):
            if(nodes[person2].get(person1)):
                nodes[person2][person1] += happ
            else:
                nodes[person2][person1] = happ
        else:
            nodes[person2] = {person1 : happ}



happiest = None
nodes2 = copy.deepcopy(nodes)
nodes2['me'] = {}
for n in nodes:
    nodes2[n]['me'] = 0
    nodes2['me'][n] = 0
    rt = routeHappy(nodes, [n])
    curr = calcDist(rt, nodes)
    if happiest == None or happiest < curr:
        happiest = curr
print "Overall Change in happiest arrangement: " + str(happiest)

happiest = None
for n in nodes2:
    rt = routeHappy(nodes2, [n])
    curr = calcDist(rt, nodes2)
    if happiest == None or happiest < curr:
        happiest = curr
print "Overall Change in happiest arrangement 2: " + str(happiest)
