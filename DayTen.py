import statistics

file = open('Source/SourceDay10', 'r')
lines = file.readlines()


class Line:
    def __init__(self, line_value):
        self.corrupted_sign = ''
        self.line_of_signs = line_value
        self.numbers = 0
        self.deleted = 0
        self.repaired_sequence = []
        self.find_corrupted_sign()
        self.result2 = self.get_repair_points()

    def find_corrupted_sign(self):
        for sign_rank in range(0, len(self.line_of_signs)):
            sign_rank -= self.deleted
            if sign_rank == len(self.line_of_signs):
                break
            else:
                if ')' in self.line_of_signs[sign_rank]:
                    self.check_if_sign_is_corrupted('(', sign_rank)
                elif ']' in self.line_of_signs[sign_rank]:
                    self.check_if_sign_is_corrupted('[', sign_rank)
                elif '}' in self.line_of_signs[sign_rank]:
                    self.check_if_sign_is_corrupted('{', sign_rank)
                elif '>' in self.line_of_signs[sign_rank]:
                    self.check_if_sign_is_corrupted('<', sign_rank)
                if len(self.corrupted_sign) > 0:
                    break

    def check_if_sign_is_corrupted(self, sign, sign_rank):
        if sign_rank > 0:
            if self.line_of_signs[sign_rank-1] != sign:
                self.corrupted_sign = self.line_of_signs[sign_rank]
            else:
                to_replace = sign + self.line_of_signs[sign_rank]
                self.line_of_signs = self.line_of_signs.replace(to_replace, '')
                self.deleted += 2

    def repair_sequence(self):
        self.deleted = 0
        for sign_rank in range(0, len(self.line_of_signs)):
            sign_rank = len(self.line_of_signs) - sign_rank - 1
            if '(' in self.line_of_signs[sign_rank]:
                self.repaired_sequence.append(1)
            elif '[' in self.line_of_signs[sign_rank]:
                self.repaired_sequence.append(2)
            elif '{' in self.line_of_signs[sign_rank]:
                self.repaired_sequence.append(3)
            elif '<' in self.line_of_signs[sign_rank]:
                self.repaired_sequence.append(4)


    def get_points(self):
        if len(self.corrupted_sign) > 0:
            if ')' in self.corrupted_sign:
                return 3
            elif ']' in self.corrupted_sign:
                return 57
            elif '}' in self.corrupted_sign:
                return 1197
            elif '>' in self.corrupted_sign:
                return 25137
        else:
            return 0

    def get_repair_points(self):
        result = 0
        if len(self.corrupted_sign) == 0:
            self.repair_sequence()
            for point in self.repaired_sequence:
                result = result * 5 + point
        return result





checked_lines = dict()
checked_lines_total = 0
result = 0
result2 = []

for line in lines:
    checked_lines[checked_lines_total] = Line(line)
    if checked_lines[checked_lines_total].corrupted_sign is not None:
        result += checked_lines[checked_lines_total].get_points()
    if checked_lines[checked_lines_total].result2 > 0:
        result2.append(checked_lines[checked_lines_total].result2)
    checked_lines_total += 1

print(result)
print(statistics.median(result2))


