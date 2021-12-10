file = open('day_9.txt', 'r')

map = []

with file as lines:
    try:
        while True:                 #Just to fake a lot of readlines and hit the end
            current = next(lines).strip()
            map.append([int(x) for x in current])
            
    except StopIteration:
        print("Loaded")

width = len(map[0])
height = len(map)
risk = []
lows = []

for i in range(0, height):
    for j in range(0, width):
        low = 9
        if i > 0:
            low = min(map[i-1][j], low)
        if i < (height-1):
            low = min(map[i+1][j], low)
        if j > 0:
            low = min(map[i][j-1], low)
        if j < (width-1):
            low = min(map[i][j+1], low)
        if low > map[i][j]:
            risk.append(map[i][j])
            lows.append((i,j))

print ("Part 1: {}".format(sum(x+1 for x in risk)))

basins = [[x] for x in lows]
changed = True
while changed:
    changed = False
    for b in basins:
        for (i, j) in b:
            if i > 0 and map[i-1][j] < 9 and not (i-1, j) in b:
                b.append((i-1, j))
                changed = True
            if i < (height-1) and map[i+1][j] < 9 and not (i+1, j) in b:
                b.append((i+1, j))
                changed = True
            if j > 0 and map[i][j-1] < 9 and not (i, j-1) in b:
                b.append((i, j-1))
                changed = True
            if j < (width-1) and map[i][j+1] < 9 and not (i, j+1) in b:
                b.append((i, j+1))
                changed = True

sizes = sorted([len(b) for b in basins], reverse=True)
print("Part 2: {}".format(sizes[0]*sizes[1]*sizes[2]))


