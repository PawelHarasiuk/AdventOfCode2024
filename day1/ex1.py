def read_file():
    with open("input.txt", 'r') as f:
        lines = f.readlines()

    return lines

def split_to_lists(lines):
    input_list1, input_list2 = [], []

    for line in lines:
        split_line = line.strip().split("   ")
        input_list1.append(int(split_line[0]))
        input_list2.append(int(split_line[1]))

    return input_list1, input_list2

def calculate_distances(input_list1, input_list2):
    l1 = sorted(input_list1)
    l2 = sorted(input_list2)
    total = sum([abs(x1 - x2) for x1, x2 in zip(l1, l2)])

    return total

def print_solution():
    lines = read_file()
    input_list1, input_list2 = split_to_lists(lines)
    print(calculate_distances(input_list1, input_list2))

print_solution()