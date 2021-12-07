file = open('day_5.txt', 'r')

connections = []
max_x = 0
max_y = 0
with file as lines:
    try:
        while True:                 #Just to fake a lot of readlines and hit the end
            current = next(lines).strip()
            parts = current.split("->")
            xy1 = parts[0].strip().split(",")
            xy2 = parts[1].strip().split(",")
            x1 = int(xy1[0].strip())
            y1 = int(xy1[1].strip())
            x2 = int(xy2[0].strip())
            y2 = int(xy2[1].strip())
            connections.append(((x1, y1), (x2, y2)))
            if max_x < x1:
                max_x = x1
            if max_x < x2:
                max_x = x2
            if max_y < y1:
                max_y = y1
            if max_y < y2:
                max_y = y2
            
    except StopIteration:
        print("Loaded")

print("max_x {} max_y {}".format(max_x, max_y))

matrix = [[0]*(max_x+1) for _ in range(max_y+1)]

for ((x1, y1), (x2, y2)) in connections:
    #print("process {},{} -> {},{}".format(x1, y1, x2, y2))
    if x1 == x2:
        y_start = min(y1, y2)
        y_end = max(y1, y2)
        for y in range(y_start, y_end+1):
            matrix[y][x1] += 1
    elif y1 == y2:
        x_start = min(x1, x2)
        x_end = max(x1, x2)
        for x in range(x_start, x_end+1):
            matrix[y1][x] += 1

count_dangerous = 0

for y in matrix:
    for x in y:
        if x >= 2:
            count_dangerous += 1
        #if x == 0:
        #    print(".", end="")
        #else:
        #    print("{}".format(x), end="")
    #print("")

print("Part 1: {}".format(count_dangerous))

matrix = [[0]*(max_x+1) for _ in range(max_y+1)]

for ((x1, y1), (x2, y2)) in connections:
    #print("process {},{} -> {},{}".format(x1, y1, x2, y2))
    if x1 == x2:
        y_start = min(y1, y2)
        y_end = max(y1, y2)
        for y in range(y_start, y_end+1):
            matrix[y][x1] += 1
    elif y1 == y2:
        x_start = min(x1, x2)
        x_end = max(x1, x2)
        for x in range(x_start, x_end+1):
            matrix[y1][x] += 1
    elif abs(x1-x2) == abs(y1-y2):
        x_action = -1
        if x1< x2:
            x_action = 1
        y_action = -1
        if y1< y2:
            y_action = 1
        for i in range(0, abs(x1-x2)+1):
            matrix[y1+(y_action*i)][x1+(x_action*i)] += 1

count_dangerous = 0
for y in matrix:
    for x in y:
        if x >= 2:
            count_dangerous += 1
        #if x == 0:
        #    print(".", end="")
        #else:
        #    print("{}".format(x), end="")
    #print("")

print("Part 2: {}".format(count_dangerous))