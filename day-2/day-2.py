input = open("day-2/input.txt", "r").readlines();

depth, horizontal, part_2_depth = 0,0,0


for line in input:
    line=line.split()
    if line[0] == "up":
        depth -= int(line[1])
    elif line[0] == "down":
        depth += int(line[1])
    else:
        horizontal += int(line[1])
        part_2_depth += (int(line[1])*depth)

print('Part 1: {x}'.format(x=depth * horizontal))
print('Part 2: {y} '.format(y=part_2_depth * horizontal))