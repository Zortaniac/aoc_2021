template = []
rules = {}

with open('day_14.txt', 'r') as lines:
    template = next(lines).strip()
    next(lines)
    for line in lines:
        current = line.strip()
        parts = current.split(" -> ")
        rules[parts[0]] = parts[1]

def run_n_times(tmpl, n):
    for s in range(1, n+1):
        new_template = []
        for c in range(0, len(tmpl)-1):
            pair = f"{tmpl[c]}{tmpl[c+1]}"
            new_template.append(tmpl[c])
            new_template.append(rules[pair])
        new_template.append(tmpl[len(tmpl)-1])
        tmpl = new_template
        print(f"Completed round {s}")

    occurrence = {}

    for c in tmpl:
        if c not in occurrence:
            occurrence[c] = 0
        occurrence[c] += 1

    most_common = 0
    least_common = len(tmpl)
    for key in occurrence:
        o = occurrence[key]
        if o > most_common:
            most_common = o
        if o < least_common:
            least_common = o
    return most_common-least_common

def generate(token):
    r = rules[token]
    return [token[0]+r, r+token[1], token[1]]

def gen_n_times(tmpl, n):
    for s in range(1, n+1):
        new_template = []
        for c in range(0, len(tmpl)-1):
            pair = f"{tmpl[c]}{tmpl[c+1]}"
            new_template.append(tmpl[c])
            new_template.append(rules[pair])
        new_template.append(tmpl[len(tmpl)-1])
        tmpl = new_template
    return ''.join(tmpl)

def calc_pair(pair, n):
    res = gen_n_times(pair, n)
    occurrence = {}
    for i in range(len(res)-1):
        c = res[i]
        if c not in occurrence:
            occurrence[c] = 0
        occurrence[c] += 1
    return occurrence
    

def run_40_times(input):
    occurrence = {}
    tmpl = []
    blocks = []
    cache = {}

    """Prepare"""
    for c in range(0, len(input)-1):
        pair = f"{input[c]}{input[c+1]}"
        tmpl.append(pair)

    print(tmpl)
    for t in tmpl:
        blocks.append(gen_n_times(t, 20))

    for b in blocks:
        for n in range(0, len(b)-1):
            pair = b[n] + b[n+1]
            if pair not in cache:
                print(f"Cache pair {pair}")
                cache[pair] = calc_pair(pair, 20)
            for k in cache[pair]:
                if k not in occurrence:
                    occurrence[k] = 0
                occurrence[k] += cache[pair][k]
    
    b = blocks[len(blocks)-1]
    last = b[len(b)-1]
    if last not in occurrence:
        occurrence[last] = 1
    else:
        occurrence[last] += 1
    return occurrence


def run_4_times(input):
    occurrence = {}
    tmpl = []
    blocks = []
    cache = {}

    """Prepare"""
    for c in range(0, len(input)-1):
        pair = f"{input[c]}{input[c+1]}"
        tmpl.append(pair)

    print(tmpl)
    for t in tmpl:
        blocks.append(gen_n_times(t, 2))
    print (blocks)
    for b in blocks:
        for n in range(0, len(b)-1):
            pair = b[n] + b[n+1]
            if pair not in cache:
                print(f"Cache pair {pair}")
                cache[pair] = calc_pair(pair, 2)
            for k in cache[pair]:
                if k not in occurrence:
                    occurrence[k] = 0
                occurrence[k] += cache[pair][k]

    b = blocks[len(blocks)-1]
    last = b[len(b)-1]
    if last not in occurrence:
        occurrence[last] = 1
    else:
        occurrence[last] += 1
    return occurrence

print(f"Part 1: {run_n_times(template[:], 10)}")

result =  run_40_times(template[:]).values()
print(f"Part 2: {max(result)-min(result)}")
