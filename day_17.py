grid = []

with open('day_17.txt', 'r') as lines:
    line = next(lines).strip()
    line = line.replace("target area: x=", "")
    parts = line.split(", y=")
    xParts = parts[0].split("..")
    yParts = parts[1].split("..")
    x = (int(xParts[0]), int(xParts[1]))
    y = (int(yParts[0]), int(yParts[1]))

    target =[]
    if x[0] < x[1]:
        target.append([x[0], x[1]])
    else:
        target.append([x[1], x[0]])
    if y[0] < y[1]:
        target.append([y[0], y[1]])
    else:
        target.append([y[1], y[0]])

hits = []
highest_y = min(target[1])

start_y = min(target[1])
end_y = max([abs(n) for n in target[1]])
for x in range(0, max(target[0])+1):
    for y in range(start_y, end_y):
        initial_velocity = [x, y]
        pos = [0, 0]
        velocity = initial_velocity[:]
        max_y = min(target[1])
        while True:
            pos[0] += velocity[0]
            pos[1] += velocity[1]
            if velocity[0] > 0:
                velocity[0] -= 1
            elif velocity[0] < 0:
                velocity[0] += 1
            velocity[1] -= 1
            if pos[1] > max_y:
                max_y = pos[1]
            if target[0][0] <= pos[0] <= target[0][1] and target[1][0] <= pos[1] <= target[1][1]:
                if max_y > highest_y:
                    highest_y = max_y
                hits.append((initial_velocity[0], initial_velocity[1]))
                break
            if start_y > pos[1]:
                break

print("Part 1: {}".format(highest_y))
print("Part 2: {}".format(len(hits)))
