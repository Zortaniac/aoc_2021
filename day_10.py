
file = open('day_10.txt', 'r')

lines = [x.strip() for x in file.readlines()]

points = [{
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}, {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}]


def parse(line):
    stack = []
    for c in line:
        if c in ['(', '[', '{', '<']:
            stack.append(c)
        else:
            top = stack.pop()
            if not ((top == '(' and c == ')')
                    or (top == '[' and c == ']')
                    or (top == '{' and c == '}')
                    or (top == '<' and c == '>')):
                return (-1, c)

    return (0, stack)


def calcInvalid(line):
    (v, c) = parse(line)
    if v == -1:
        return points[0][c]
    else:
        return 0


def calcMissing(line):
    (v, s) = parse(line)
    score = 0
    if v == 0 and len(s) > 0:
        while len(s) > 0:
            c = s.pop()
            score *= 5
            score += points[1][c]
    return score


print("Part 1: {}".format(sum([calcInvalid(x) for x in lines])))

result = [x for x in [calcMissing(x) for x in lines] if x > 0]
result.sort()

print("Part 2: {}".format(result[len(result)/2]))
