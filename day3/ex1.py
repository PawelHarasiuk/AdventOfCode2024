import re


def read_input(path):
    with open(path, 'r') as file:
        return file.readlines()


def calculate_line(line):
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, line)
    count = 0
    if matches:
        for (val1, val2) in matches:
            count += int(val1) * int(val2)
    return count


def sum_lines(lines):
    count = 0
    for line in lines:
        count += calculate_line(line)

    return count


def print_solution():
    lines = read_input("input.txt")
    result = sum_lines(lines)
    print(result)

print_solution()