with open('Source/SourceDay9', 'r') as file:
    lines = file.read().splitlines()


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


line = dict()

number_of_lines = len(lines)
number_of_characters_in_line = len(lines[1])
result_part_1 = 0

for line_number in range(0, number_of_lines):
    line[line_number] = Line()
    for number in lines[line_number]:
        line[line_number].numbers.append(int(number))



for line_number in range (0, number_of_lines):
    run(line_number)
    result_part_1 += line[line_number].count_result()

print(result_part_1)

