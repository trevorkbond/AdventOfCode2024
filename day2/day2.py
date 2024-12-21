def read_file(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    return lines

def process_lines(lines):
    lines_list = []
    for line in lines:
        new_line = line.strip().split(" ")
        for i in range(len(new_line)):
            new_line[i] = int(new_line[i])
        lines_list.append(new_line)
    return lines_list

def diff_in_sign(num1, num2):
    if num1 < 0 and num2 < 0:
        return False
    elif num1 > 0 and num2 > 0:
        return False
    return True

def above_threshhold(min_val, max_val):
    if min_val < -3:
        return True
    if max_val > 3:
        return True
    return False

def report_is_safe(diffs):
    max_diff = max(diffs)
    min_diff = min(diffs)
    if max_diff == 0 or min_diff == 0:
        return False
    elif diff_in_sign(min_diff, max_diff):
        return False
    elif above_threshhold(min_diff, max_diff):
        return False
    return True

def generate_diffs(report):
    diffs = []
    for i in range(len(report) - 1):
        diffs.append(report[i] - report[i + 1])
    return diffs

reports = process_lines(read_file("input.txt"))

num_safe = 0
for report in reports:
    diffs = generate_diffs(report)
    if report_is_safe(diffs):
        num_safe += 1
        continue
    potential_diffs = []
    for i in range(len(report)):
        temp_report = report[:]
        temp_report.pop(i)
        potential_diffs.append(generate_diffs(temp_report))
    potential_diffs_safe = False
    for potential_diff in potential_diffs:
        if report_is_safe(potential_diff):
            potential_diffs_safe = True
            break
    if potential_diffs_safe:
        num_safe += 1


print(num_safe)