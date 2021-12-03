#gamma = 217
#epsilon = 3878


gamma,epsilon = '',''

with open("day-3/input.txt") as f:
    list_of_numbers = [line.strip() for line in f.readlines()]

for position in range(0,len(list_of_numbers[0])):
    one = 0
    zero = 0
    for index in range(0,len(list_of_numbers)):
        if list_of_numbers[index][position] == '0':
            zero += 1
        else:
            one += 1
    if zero > one:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

print('Part 1: {x}'.format(x=int(gamma,2)*int(epsilon,2)))

list_of_numbers_copy = list_of_numbers.copy()
position = 0
while len(list_of_numbers) > 1:
    one = 0
    zero = 0
    ones = []
    zeros = []
    for index in range(0, len(list_of_numbers)):
        if list_of_numbers[index][position] == '0':
            zero += 1
            zeros.append(list_of_numbers[index])
        else:
            one += 1
            ones.append(list_of_numbers[index])
    if zero > one:
        list_of_numbers = zeros
    else:
        list_of_numbers = ones
    position += 1

oxygen = int(list_of_numbers[0], 2)


list_of_numbers = list_of_numbers_copy
position = 0
while len(list_of_numbers) > 1:
    one = 0
    zero = 0
    ones = []
    zeros = []
    for index in range(0, len(list_of_numbers)):
        if list_of_numbers[index][position] == '0':
            zero += 1
            zeros.append(list_of_numbers[index])
        else:
            one += 1
            ones.append(list_of_numbers[index])
    if one < zero:
        list_of_numbers = ones
    else:
        list_of_numbers = zeros
    position += 1

co2 = int(list_of_numbers[0], 2)

print('Part 2: {x}'.format(x=oxygen*co2))