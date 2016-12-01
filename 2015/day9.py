import re

def route(nodes, path):
    if(len(path) == len(nodes)):
        return path
    short = -1
    nextNode = None
    neighbors = nodes[path[len(path) - 1]]
    for n in neighbors:
        if short == -1 or short > neighbors[n]:
            if not n in path:
                short = neighbors[n]
                nextNode = n
    path.append(nextNode)
    return route(nodes, path)
def routeLong(nodes, path):
    if(len(path) == len(nodes)):
        return path
    longest = 0
    nextNode = None
    neighbors = nodes[path[len(path) - 1]]
    for n in neighbors:
        if longest < neighbors[n]:
            if not n in path:
                longest = neighbors[n]
                nextNode = n
    path.append(nextNode)
    return routeLong(nodes, path)

def calcDist(path, nodes):
    dist = 0
    for i, p in enumerate(path):
        if(i < len(path) - 1):
            dist += nodes[path[i]][path[i + 1]]
    return dist

data = open('input-day9.txt', 'r').read().split('\n')
nodes = {}
for line in data:
    if(line):
        nodeInfo = re.findall('(.*) to (.*) = ([0-9]*)', line)[0]
        origin = nodeInfo[0]
        dest = nodeInfo[1]
        dist = int(nodeInfo[2])
        if nodes.get(origin):
            nodes[origin][dest] = dist
        else:
            nodes[origin] = {dest : dist}
        if nodes.get(dest):
            nodes[dest][origin] = dist
        else:
            nodes[dest] = {origin : dist}
short = -1
longest = 0
for n in nodes:
    curr = calcDist(route(nodes, [n]), nodes)
    curr2 = calcDist(routeLong(nodes, [n]), nodes)
    if short == -1 or short > curr:
        short = curr
    if longest < curr2:
        longest = curr2
print "Shortest Route: " + str(short)
print "Longest Route: " + str(longest)
