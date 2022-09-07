class Display:
    def __init__(self):
        self.all_numbers = []
        self.result_numbers = []
        self.result_numbers_translate = []
        self.segments_a = ''
        self.segments_ef = ''
        self.segments_bc = ''

    def load_numbers(self, number):
        self.all_numbers.append(number)

    def load_result_row(self, result):
        self.result_numbers.append(result)

    def add_translated_result(self, translated_result):
        self.result_numbers_translate.append(translated_result)

    def calculate_result_for_part1(self):
        result = 0
        for number in self.result_numbers_translate:
            if number == 1 or number == 4 or number == 7 or number == 8:
                result += 1
        return result

    def calculate_result_for_part2(self):
        result = ''
        for number in self.result_numbers_translate:
            result += str(number)
        return int(result)

    def indenify_display_segment(self):
        for segment in self.all_numbers:
            if len(segment) == 4:
                letters = [l for l in segment]
                for letter in letters:
                    if letter not in self.segments_bc:
                        self.segments_ef += letter
            if len(segment) == 3:
                letters = [l for l in segment]
                for letter in letters:
                    if letter not in self.segments_bc:
                        self.segments_a += letter

    def determine_rest(self):
        for number in self.result_numbers:
            index = self.result_numbers.index(number)
            is_number = 0
            if len(number) == 5:
                letters = [l for l in self.segments_bc]
                for letter in letters:
                    if letter in number:
                        is_number += 1
                if is_number == 2:
                    self.result_numbers_translate[index] = 3
                elif is_number == 1:
                    is_number = 0
                    letters = [l for l in self.segments_ef]
                    for letter in letters:
                        if letter in number:
                            is_number += 1
                    if is_number == 2:
                        self.result_numbers_translate[index] = 5
                    else:
                        self.result_numbers_translate[index] = 2
            elif len(number) == 6:
                letters = [l for l in self.segments_bc]
                for l in self.segments_ef:
                    letters.append(l)
                for letter in letters:
                    if letter in number:
                        is_number += 1
                if is_number == 4:
                     self.result_numbers_translate[index] = 9
                elif is_number < 4:
                    is_number = 0
                    letters = [l for l in self.segments_bc]
                    for letter in letters:
                        if letter in number:
                            is_number += 1
                    if is_number == 2:
                        self.result_numbers_translate[index] = 0
                    else:
                        self.result_numbers_translate[index] = 6

    def determine_bc(self):
        for number in self.all_numbers:
            if len(number) == 2:
                self.segments_bc = number



    def determine_number(self, number):
        length = len(number)

        if length == 2:
            self.segments_bc = number
            return 1
        elif length == 3:
            return 7
        elif length == 4:
            return 4
        elif length == 7:
            return 8
        elif length == 6:
            return 690
        else:
            return 235

with open ("Source/SourceDay8", "r") as file:
    lines = file.read().splitlines()

row = dict()

for line in range(0, len(lines)):
    row[line] = Display()
    line_entries = [entry for entry in lines[line].split(' ') if entry != '|']
    for entry in line_entries:
        if len(row[line].all_numbers) < 10:
            row[line].load_numbers(entry)
        else:
            row[line].load_result_row(entry)

result = 0
result_part_two = 0
for row_number in range(0, len(lines)):
    for entry in row[row_number].result_numbers:
        row[row_number].add_translated_result(row[row_number].determine_number(entry))
    row[row_number].determine_bc()
    row[row_number].indenify_display_segment()
    row[row_number].determine_rest()
    result += row[row_number].calculate_result_for_part1()
    result_part_two += row[row_number].calculate_result_for_part2()

print('Result part one ' + str(result))
print('Result part two ' + str(result_part_two))
