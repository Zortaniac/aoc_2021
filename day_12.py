connections = []

with open('day_12.txt', 'r') as lines:
    try:
        for line in lines:
            current = line.strip().split("-")
            connections.append((current[0], current[1]))
            if current[0] != 'start' and current[1] != 'end':
                connections.append((current[1], current[0]))
    except StopIteration:
        pass


def walk(cc, existing_connections, twice):
    if cc == "end":
        return ["end"], ["end"]

    results2 = []
    if cc == cc.lower():
        if twice == '' and cc != 'start':
            for t in [c for c in existing_connections if c[0] == cc and c[1] != 'end']:
                for r in walk(t[1], existing_connections, cc)[1]:
                    results2.append(f"{cc}-{r}")

        existing_connections = [c for c in existing_connections if c[1] != cc]

    results1 = []
    for t in [c for c in existing_connections if c[0] == cc]:
        results = walk(t[1], existing_connections, twice)
        [results1.append(f"{cc}-{r}") for r in results[0]]
        [results2.append(f"{cc}-{r}") for r in results[1]]
    return results1, results2


total = walk('start', connections, '')
print("Part 1: {}".format(len(set(total[0]))))
print("Part 2: {}".format(len(set(total[1]))))
