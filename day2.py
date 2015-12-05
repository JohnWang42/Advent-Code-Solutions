data = open('input-day2.txt', 'r').read().split('\n')
for row in range(len(data)):
    if(data[row] == ""):
        data.remove(data[row])
    else:
        data[row] = data[row].split('x')
wrapArea = 0
ribbonLength = 0
for row in data:
    l = int(row[0])
    w = int(row[1])
    h = int(row[2])
    wrapArea += 2 * l * w + 2 * w * h + 2 * h * l
    smallSide = l * w
    side2 = l * h
    side3 = w * h
    if(side2 < smallSide):
        smallSide = side2
    if(side3 < smallSide):
        smallSide = side3
    wrapArea += smallSide
    ribbonLength += l * w * h
    smallSide = 2 * l + 2 * w
    side2 = 2 * l + 2 * h
    side3 = 2 * w + 2 * h
    if(side2 < smallSide):
        smallSide = side2
    if(side3 < smallSide):
        smallSide = side3
    ribbonLength += smallSide
print "Surface Area: " + str(wrapArea)
print "Ribbon Length: " + str(ribbonLength)
