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

def sum_lines(line):
    count = 0
    lines_do = line.split("do()")
    for l in lines_do:
        lines_dont = l.split("don't()")
        count += calculate_line(lines_dont[0])

    return count


def connect_to_line(lines):
    one_line = ""
    for line in lines:
        one_line += line
    return one_line


def print_solution():
    lines = read_input("input.txt")
    one_line = connect_to_line(lines)
    result = sum_lines(one_line)
    print(result)


print_solution()