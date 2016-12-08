# Day 17
data = open('input-day17.txt', 'r').read().split('\n')
containers = []
for row in data:
    containers.append(int(row))

containers = [20, 15, 10, 5, 5]

target = 25
combos = 0
for i in range(0, len(containers)):
    empty = containers[:]
    total = containers[i]
    used = [containers[i]]
    empty.remove(containers[i])
    skip = 0
    while total < target:
        if skip == len(empty) or len(empty) == 0:
            total = -1
            break
        curr = empty[skip]
        if total + curr > target:
            skip += 1
        else:
            total += curr
            used.append(curr)
            empty.remove(curr)
    if total == target:
        print used
        combos += 1
        # count alternatives that could be made by switching same size containers
        for u in used:
            combos += empty.count(u)
# print combos
print sum(containers[i] for i in [1, 2, 4])
