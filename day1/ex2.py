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

def get_frequency(input_list2):
    freq = {}

    for val in input_list2:
        freq[val] = freq.get(val, 0) + 1

    return freq

def get_similarity_score(input_list1, freq):
    score = 0
    for val in input_list1:
        appeared = freq.get(val, 0)
        score += val * appeared
    return score


def print_solution():
    lines = read_file()
    input_list1, input_list2 = split_to_lists(lines)
    freq = get_frequency(input_list2)
    print(get_similarity_score(input_list1, freq))

print_solution()
