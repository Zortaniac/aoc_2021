import re
def str_to_num(n):
  return int(n)

file = open('day_4.txt', 'r')

numbers = []
for v in file.readline().strip().split(','):
    numbers.append(int(v))
blocks = []

block = []

class Bingo:
    def __init__(self, rows):
        self.rows = rows

    def sum(self, status):
        sum = 0
        for i in range(5):
            for j in range(5):
                if not status[i][j]:
                    sum += self.rows[i][j]
        return sum
    def test(self, status):
        for r in status:
            if all(ele for ele in r):
                return True
        for i in range(5):
            counter = 0
            for j in range(5):
                if status[j][i]:
                    counter += 1
            if counter == 5:
                return True
        return False


    def play(self, nums):
        counter = 0
        status = []
        for i in range(5):
            row = []
            for j in range(5):
                row.append(False)
            status.append(row)
        last_num = 0
        for n in nums:
            counter += 1
            last_num = n
            for r in self.rows:
                i = self.rows.index(r)
                for c in r:
                    j = r.index(c)
                    if r[j] == n:
                        status[i][j] = True
                        break
            if self.test(status):
                break
        return (counter, status, last_num)


with file as lines:
    try:
        block = []
        while True:                 #Just to fake a lot of readlines and hit the end
            current = next(lines).strip()
            if not current:
                if len(block) > 0:
                    blocks.append(Bingo(block))
                block = []
            else:
                row = []
                for v in re.split('\s+', current):
                    row.append(int(v))
                block.append(row)
    except StopIteration:
        if len(block) > 0:
            blocks.append(Bingo(block))

min_rounds = len(numbers)
score = 0
for b in blocks:
    rounds, status, last_num = b.play(numbers)
    if rounds < min_rounds:
        min_rounds = rounds
        score = b.sum(status) * last_num

print("Part 1: {}".format(score))

min_rounds = 0
score = 0
for b in blocks:
    rounds, status, last_num = b.play(numbers)
    if rounds > min_rounds:
        min_rounds = rounds
        score = b.sum(status) * last_num

print("Part 2: {}".format(score))

