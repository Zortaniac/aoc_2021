dots = []
instructions = []

with open('day_13.txt', 'r') as lines:
    try:
        load_instructions = False
        for line in lines:
            current = line.strip()
            if not current:
                load_instructions = True
                continue
            if load_instructions:
                parts = current[len("fold along "):].split('=')
                instructions.append((parts[0], int(parts[1])))
            else:
                parts = current.split(',')
                dots.append((int(parts[0]), int(parts[1])))
    except StopIteration:
        pass


def fold(instruction, dots):
    new_dots = []
    width = max([x[0] for x in dots])
    height = max([x[1] for x in dots])

    if instruction[0] == "y": # folding in height
        height = max(instruction[1], height - instruction[1])
    else:
        width = max(instruction[1], width - instruction[1])

    for d in dots:
        if instruction[0] == "y":
            if d[1] == instruction[1]:
                continue 
            if d[1] > instruction[1]:
                new_dots.append((d[0], height - d[1] + instruction[1]))
            else:
                new_dots.append((d[0], height-instruction[1] + d[1]))
        else:
            if d[0] == instruction[1]:
                continue
            if d[0] > instruction[1]:
                new_dots.append((width - d[0] + instruction[1], d[1]))
            else:
                new_dots.append((width - instruction[1] + d[0], d[1]))
    return new_dots
    

print("Part 1: {}".format(len(set(fold(instructions[0], dots)))))

for i in instructions:
    dots = fold(i, dots)

width = max([x[0] for x in dots])+1
height = max([x[1] for x in dots])+1
print("Part 2:")
for y in range(height):
    for x in range(width):
        if (x, y) in dots:
            print("#", end='')
        else:
            print('.', end='')
    print('')