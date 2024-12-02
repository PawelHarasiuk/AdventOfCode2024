def read_file():
    path = "input.txt"
    with open(path, 'r') as file:
        lines = [line.strip().split(" ") for line in file]

    return lines

def is_safe(report):
    asc = True
    desc = True

    for i in range(len(report) - 1):
        diff = int(report[i + 1]) - int(report[i])
        if diff > 0:
            asc = False
        elif diff < 0:
            desc = False
        else:
            return False

        if abs(diff) > 3 or (not asc and not desc):
            return False

    return True

def can_be_save(report):
    for i in range(len(report)):
        if is_safe(report[:i] + report[i + 1:]):
            return True

    return False

def count_safe(reports):
    count = 0
    for report in reports:
        if is_safe(report):
            count += 1
        elif can_be_save(report):
            count += 1

    return count

def print_solution():
    lines = read_file()
    safe = count_safe(lines)
    print(safe)

print_solution()