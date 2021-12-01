list_of_numbers = open("day-1/input.txt", "r").readlines();



def PartOne(input_file):
    return sum([1 for i in range(1, len(input_file)) if int(input_file[i])>int(input_file[i-1])])

def PartTwo(input_file):
    return sum([1 for i in range(3, len(input_file)) if int(input_file[i])>int(input_file[i-3])])

print(PartOne(list_of_numbers))
print(PartTwo(list_of_numbers))