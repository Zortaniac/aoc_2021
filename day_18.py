import ast
import math
import copy


def load_data():
    lists = []

    with open('day_18.txt', 'r') as lines:
        for line in lines:
            lists.append(ast.literal_eval(line.strip()))
    return lists


def add(values, a, idx):
    if not isinstance(values[idx], list):
        values[idx] += a
    else:
        add(values[idx], a, idx)


def explode(values, level):
    if not isinstance(values, list):
        return values, 0, 0, False

    if level > 3 and not isinstance(values[0], list) and not isinstance(values[1], list):
        return 0, values[0], values[1], True

    (values[0], l, r, e) = explode(values[0], level + 1)

    if r > 0:
        if not isinstance(values[1], list):
            values[1] += r
        else:
            add(values[1], r, 0)

    r2 = 0
    if not e:
        (values[1], l2, r2, e) = explode(values[1], level + 1)
        if l2 > 0:
            if not isinstance(values[0], list):
                values[0] += l2
            else:
                add(values[0], l2, 1)

    return values, l, r2, e


def split(values):
    if isinstance(values[0], list):
        if split(values[0]):
            return True
    else:
        if values[0] > 9:
            n = values[0]
            values[0] = [(n // 2), math.ceil(n / 2)]
            return True

    if isinstance(values[1], list):
        if split(values[1]):
            return True
    else:
        if values[1] > 9:
            n = values[1]
            values[1] = [(n // 2), math.ceil(n / 2)]
            return True
    return False


def reduce(values):
    changed = True
    while changed:
        changed = False
        exploded = True
        while exploded:
            (values, _, _, exploded) = explode(values, 0)
            changed |= exploded
        got_split = split(values)
        changed |= got_split
    return values


def calc_mag(values):
    if not isinstance(values, list):
        return values

    return 3*calc_mag(values[0]) + 2*calc_mag(values[1])


data = load_data()
v = data[0]
for a in data[1:]:
    v = [v, a]
    v = reduce(v)


print("Part 1: {}".format(calc_mag(v)))

largest = 0
data = load_data()

for i in range(0, len(data)):
    for j in range(0, len(data)):
        if i == j:
            continue
        d = copy.deepcopy(data)
        v = [d[i], d[j]]
        mag = calc_mag(reduce(v))
        if mag > largest:
            largest = mag

print("Part 2: {}".format(largest))
