file = open('day_8.txt', 'r')

signals = []

class Signal:
    def __init__(self, line):
        parts = line.split(" | ")
        self.pattern = [sorted(x) for x in parts[0].strip().split(' ')]
        self.output = [sorted(x) for x in parts[1].strip().split(' ')]

    def countUniqueOutputs(self):
        counter = 0
        for o in self.output:
            if len(o) == 2: # digit 1
                counter += 1
            elif len(o) == 4: # digit 4
                counter += 1
            elif len(o) == 3: # digit 7
                counter += 1
            elif len(o) == 7: # digit 8
                counter += 1
        return counter

    def findPattern(self):
        lookup = {}
        while len(lookup) < 10:
            for p in self.pattern:
                if len(p) == 2: # digit 1
                    lookup[1] = p
                elif len(p) == 4: # digit 4
                    lookup[4] = p
                elif len(p) == 3: # digit 7
                    lookup[7] = p
                elif len(p) == 7: # digit 8
                    lookup[8] = p
                elif len(p) == 5 and 1 in lookup and 4 in lookup: # digit 5,2,3
                    if len(set(p) - set(lookup[1])) == 3:
                        lookup[3] = p
                    elif len(set(p) - set(lookup[4])) == 2:
                        lookup[5] = p
                    else:
                        lookup[2] = p
                elif len(p) == 6 and 1 in lookup and 5 in lookup: # digit 0,6,9
                    if len(set(p) - set(lookup[1])) == 5:
                        lookup[6] = p
                    elif len(set(p) - set(lookup[5])) == 1:
                        lookup[9] = p
                    else:
                        lookup[0] = p
        pos = 3
        value = 0
        for o in self.output:
            for l in lookup:
                if len(o) == len(lookup[l]) and set(o) == set(lookup[l]):
                    value += l * pow(10, pos)
                    pos -= 1
                    break 
        return value



with file as lines:
    try:
        while True:
            current = next(lines).strip()
            signals.append(Signal(current))
            
    except StopIteration:
        print("Loaded")


sum = 0
for s in signals:
    sum += s.countUniqueOutputs()

print("Part 1: {}".format(sum))


sum = 0
for s in signals:
    sum += s.findPattern()

print("Part 2: {}".format(sum))
