import re


def read_file(file_name):
    file = open(file_name, "r")
    contents = file.read()
    return contents.replace('\n', '')


valid_instructions = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", read_file("input.txt"))

total = 0
do = True
for instruction in valid_instructions:
    do = instruction != "don't()"
    if do:
        if instruction != "do()":
            nums = re.findall(r"\d+", instruction)
            total += int(nums[0]) * int(nums[1])

print(total)
