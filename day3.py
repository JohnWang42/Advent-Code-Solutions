class House:
    def __init__(self, x, y):
        self.x = x
        self.y = y

data = open('input-day3.txt', 'r').read()
santaX = 0
santaY = 0
houses = [House(0, 0)]

#initial pathing
for dir in data:
    if(dir == '^'):
        santaY += 1
    if(dir == '>'):
        santaX += 1
    if(dir == 'v'):
        santaY -= 1
    if(dir == '<'):
        santaX -= 1
    exists = False
    for h in houses:
        if(h.x == santaX and h.y == santaY):
            exists = True
            break
    if(not exists):
        houses.append(House(santaX, santaY))
print "Solo Santa: " + str(len(houses))


#robo santa pathing
santaX = 0
santaY = 0
roboSantaX = 0
roboSantaY = 0
houses = []
for ind, dir in enumerate(data):
    if(ind % 2 == 0):
        if(dir == '^'):
            roboSantaY += 1
        if(dir == '>'):
            roboSantaX += 1
        if(dir == 'v'):
            roboSantaY -= 1
        if(dir == '<'):
            roboSantaX -= 1
        exists = False
        for h in houses:
            if(h.x == roboSantaX and h.y == roboSantaY):
                exists = True
                break
        if(not exists):
            houses.append(House(roboSantaX, roboSantaY))
    else:
        if(dir == '^'):
            santaY += 1
        if(dir == '>'):
            santaX += 1
        if(dir == 'v'):
            santaY -= 1
        if(dir == '<'):
            santaX -= 1
        exists = False
        for h in houses:
            if(h.x == santaX and h.y == santaY):
                exists = True
                break
        if(not exists):
            houses.append(House(santaX, santaY))

print "Santa and RoboSanta: " + str(len(houses))
