
file = open('day_11.txt', 'r')

map = []

with file as lines:
    try:
        while True:
            current = next(lines).strip()
            map.append([int(x) for x in current])
            
    except StopIteration:
        print("", end="")

width =len(map[0])
height = len(map)

round = 0
flashes = 0
flashesPart1 = 0
flashesSynced = 0

while True:
    flashed = []
    changed = True

    for n in range(0, height):
        for m in range(0, width):
            map[n][m] += 1
            
    while changed:
        changed = False
        for n in range(0, height):
            for m in range(0, width):
                if map[n][m] > 9 and not (n, m) in flashed:
                    flashes += 1
                    flashed.append((n, m))
                    if n > 0:
                        map[n-1][m] += 1
                        changed = True
                    if n < (height-1):
                        map[n+1][m] += 1
                        changed = True
                    if m > 0:
                        map[n][m-1] += 1
                        changed = True
                    if m < (width-1):
                        map[n][m+1] += 1
                        changed = True
                    if m > 0 and n > 0:
                        map[n-1][m-1] += 1
                        changed = True
                    if m > 0 and n < (height-1):
                        map[n+1][m-1] += 1
                        changed = True
                    if m < (width-1) and n > 0:
                        map[n-1][m+1] += 1
                        changed = True
                    if m < (width-1) and n < (height-1):
                        map[n+1][m+1] += 1
                        changed = True

    for (n, m) in flashed:
        map[n][m] = 0
    
    round += 1
    
    if round == 100:
        flashesPart1 = flashes

    if len(flashed) == width*height:
        flashesSynced = round
    
    if flashesSynced > 0 and flashesPart1 > 0:
        break

print("Part 1: {}".format(flashesPart1))
print("Part 2: {}".format(flashesSynced))