from os import path, walk


grid = []

with open('day_15.txt', 'r') as lines:
    for line in lines:
        row = []
        for c in line.strip():
            row.append(int(c))
        grid.append(row)


class Walker():
    def __init__(self, grid):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0]) 
        self.max = self.height+self.width
        self.best = self.height*9+self.width*9
        self.maxLength = self.height*9+self.width*9
            
    def getBestSurrounding(self, x, y):
        if x == len(self.grid[0])-1 and y == len(self.grid)-1:
            return 0
        values = []
        if (x, y-1) in self.cache:
            values.append(self.cache[(x, y-1)])
        if (x, y+1) in self.cache:
            values.append(self.cache[(x, y+1)])
        if (x-1, y) in self.cache:
            values.append(self.cache[(x-1, y)])
        if (x+1, y) in self.cache:
            values.append(self.cache[(x+1, y)])
        if len(values) == 0:
            print(f"Humh? {x} {y} {self.cache}")
        return min(values)

    def findBest(self):
        self.cache = {}
        self.cache[(self.width-1, self.height-1)] = 0
        changed = True
        while changed:
            changed = False
            for i in reversed(range(0, self.width)):
                for j in reversed(range(i, self.height)):

                    best = self.grid[j][i] + self.getBestSurrounding(i, j)
                    if (i, j) not in self.cache or best < self.cache[(i, j)]:
                        changed = True
                    self.cache[(i, j)] = best

                    best = self.grid[i][j] + self.getBestSurrounding(j, i)
                    if (j, i) not in self.cache or best < self.cache[(j, i)]:
                        changed = True
                    self.cache[(j, i)] = best

        return self.cache[(0, 0)] - self.grid[0][0]



walker = Walker(grid)
print("Part 1: {}".format(walker.findBest()))

large_grid = []
for i in range(0, 5):
    for n in range(0, len(grid)):
        row = []
        for j in range(0, 5):
            row += [((x+j-1)%9)+1 for x in [((y+i-1)%9)+1  for y in grid[n]]]
        large_grid.append(row)

walker = Walker(large_grid)
print("Part 2: {}".format(walker.findBest()))