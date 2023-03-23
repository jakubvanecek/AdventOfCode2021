with open('Source/SourceDay9', 'r') as file:
    lines = file.read().splitlines()


line = dict()
lava_pool = dict()
lava_pool_number = 0
largest_3 = []

class Line:
    def __init__(self):
        self.numbers = []
        self.marked_number = []

    def insert_numbers(self, number_to_insert):
        self.numbers.append(number_to_insert)

    def insert_marked(self, number_to_insert):
        self.marked_number.append(number_to_insert)

    def count_result(self):
        return sum(self.marked_number) + len(self.marked_number)

    def lava_places(self, lava_coordinates):
        if lava_coordinates not in self.lava_fields:
            self.lava_fields.append(lava_coordinates)

class LavaPool:
    def __init__(self, initial_lava_field):
        self.lava_filed_coordinates = [initial_lava_field]
        self.total_value = 0

    def add_coordinates(self, lava_coordinates):
        if lava_coordinates not in self.lava_filed_coordinates:
            self.lava_filed_coordinates.append(lava_coordinates)

    def count_value(self):
        self.total_value = len(self.lava_filed_coordinates)





def get_numbers(line_number, number_rank, special):
    compare_0 = line[line_number].numbers[number_rank]
    compare_1, compare_2, compare_3, compare_4 = (9, 9, 9, 9)

    if special == 4:
        compare_1 = line[line_number].numbers[number_rank + 1]
        compare_2 = line[line_number].numbers[number_rank - 1]
        compare_3 = line[line_number - 1].numbers[number_rank]
        compare_4 = line[line_number + 1].numbers[number_rank]
    elif special == 3:
        if line_number == 0 and number_rank not in (0, number_of_characters_in_line - 1):
            compare_1 = line[line_number].numbers[number_rank + 1]
            compare_2 = line[line_number].numbers[number_rank - 1]
            compare_3 = line[line_number + 1].numbers[number_rank]
        elif line_number == number_of_lines - 1 and number_rank not in (0, number_of_characters_in_line - 1):
            compare_1 = line[line_number].numbers[number_rank + 1]
            compare_2 = line[line_number].numbers[number_rank - 1]
            compare_3 = line[line_number - 1].numbers[number_rank]
        elif number_rank == 0:
            compare_1 = line[line_number].numbers[number_rank + 1]
            compare_2 = line[line_number + 1].numbers[number_rank]
            compare_3 = line[line_number - 1].numbers[number_rank]
        else:
            compare_1 = line[line_number].numbers[number_rank - 1]
            compare_2 = line[line_number + 1].numbers[number_rank]
            compare_3 = line[line_number - 1].numbers[number_rank]

    elif special == 2:
        if line_number == 0:
            if number_rank == 0:
                compare_1 = line[line_number].numbers[number_rank + 1]
                compare_2 = line[line_number + 1].numbers[number_rank]
            else:
                compare_1 = line[line_number].numbers[number_rank - 1]
                compare_2 = line[line_number + 1].numbers[number_rank]
        else:
            if number_rank == 0:
                compare_1 = line[line_number].numbers[number_rank + 1]
                compare_2 = line[line_number - 1].numbers[number_rank]
            else:
                compare_1 = line[line_number].numbers[number_rank - 1]
                compare_2 = line[line_number - 1].numbers[number_rank]

    if compare_0 < compare_1 and compare_0 < compare_2 and compare_0 < compare_3 and compare_0 < compare_4:
        line[line_number].insert_marked(compare_0)
        global lava_pool_number
        lava_pool[lava_pool_number] = LavaPool(f"{line_number};{number_rank}")
        lava_pool_number += 1

def run(line_number):
    for number in range(0, number_of_characters_in_line):
        if line_number in (0, number_of_lines - 1):
            if number in (0, number_of_characters_in_line - 1):
                get_numbers(line_number, number, 2)
            else:
                get_numbers(line_number, number, 3)
        else:
            if number in (0, number_of_characters_in_line - 1):
                get_numbers(line_number, number, 3)
            else:
                get_numbers(line_number, number, 4)





number_of_lines = len(lines)
number_of_characters_in_line = len(lines[1])
result_part_1 = 0
result_part_2 = 1

for line_number in range(0, number_of_lines):
    line[line_number] = Line()
    for number in lines[line_number]:
        line[line_number].numbers.append(int(number))


for line_number in range (0, number_of_lines):
    run(line_number)
    result_part_1 += line[line_number].count_result()

for pool_number in lava_pool:
    for coordinates in lava_pool[pool_number].lava_filed_coordinates:
        x, y = coordinates.split(';')
        x = int(x)
        y = int(y)
        if int(x) > 0:
            if int(lines[x-1][y]) < 9:
                lava_pool[pool_number].add_coordinates(f"{x-1};{y}")
        if int(x) < number_of_lines-1:
            if int(lines[x+1][y]) < 9:
                lava_pool[pool_number].add_coordinates(f"{x+1};{y}")
        if int(y) > 0:
            if int(lines[x][y-1]) < 9:
                lava_pool[pool_number].add_coordinates(f"{x};{y-1}")
        if int(y) < number_of_characters_in_line-1:
            if int(lines[x][y+1]) < 9:
                lava_pool[pool_number].add_coordinates(f"{x};{y+1}")

    lava_pool[pool_number].count_value()

all_basins = []

for lava_number in lava_pool:
    all_basins.append(lava_pool[lava_number].total_value)

all_basins.sort()

for number in range (0,3):
    biggest_in_current_row = 0
    for lava_number in lava_pool:
        if lava_number not in largest_3:
            if lava_pool[lava_number].total_value > biggest_in_current_row:
                biggest_in_current_row = lava_pool[lava_number].total_value
                biggest_row = lava_number

    result_part_2 = result_part_2 * biggest_in_current_row
    largest_3.append(biggest_row)



print(result_part_1)
print(result_part_2)
