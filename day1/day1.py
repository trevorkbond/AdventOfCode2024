DELIMITER = "   "


def read_file(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    return lines


def process_lines(lines):
    list1 = []
    list2 = []
    for line in lines:
        locations = line.split(DELIMITER)
        list1.append(int(locations[0]))
        list2.append(int(locations[1]))
    return list1, list2


list1, list2 = process_lines(read_file("location_ids.txt"))
sorted1 = sorted(list1)
sorted2 = sorted(list2)

total_dif = 0
for i in range(len(sorted1)):
    total_dif += abs(sorted1[i] - sorted2[i])

unique_left_list = list(dict.fromkeys(sorted1))

similarity_score = 0
for val in unique_left_list:
    similarity_score += val * sorted2.count(val)

print(similarity_score)
