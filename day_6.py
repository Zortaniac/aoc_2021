import re
def str_to_num(n):
  return int(n)

file = open('day_6.txt', 'r')

fishInput = []
for v in file.readline().strip().split(','):
    fishInput.append(int(v))

file.close()

d = 80

fish = fishInput
for i in range(1, d+1):
    newFish = []
    for f in fish:
        if f == 0:
            newFish.append(6)
            newFish.append(8)
        else:
            newFish.append(f-1)
    fish = newFish

print("Part 1: {}".format(len(fish)))

d = 256
days = []
for i in range(0,d+10):
    set = [0,0]
    days.append(set)

fish = fishInput
for f in fish:
    days[f][1] += 1

for i in range(0, d):
    days[i+9][0] += days[i][0]
    days[i+7][1] += days[i][0]
    days[i+9][0] += days[i][1]
    days[i+7][1] += days[i][1]
    days[i][0] = 0
    days[i][1] = 0

print("Part 2: {}".format(sum(x[0] + x[1] for x in days)))
