import numpy as np
import math as m

with open("Source/SourceDay7", "r") as file:
    lines = file.read().splitlines()

numbers = [int(line) for line in lines[0].split(',')]

median = np.median(numbers)
average = np.average(numbers)

print(median)
print(average)

result_part1 = 0
result_part2 = 0
helper_for_part2 = 0

# 99763899 right result

for number in numbers:
    result_part1 = result_part1 + abs(number - median)
    # helper_for_part2 = int(abs(number - average))
    # for helper in range(1, helper_for_part2 + 1):
    #     result_part2 = result_part2 + helper


minimal = min(numbers)
maximal = max(numbers)
result = []

for x in range(minimal, maximal+1):
    for number in numbers:
        result_part1 = result_part1 + abs(number - median)
        helper_for_part2 = int(abs(number - x))
        for helper in range(1, helper_for_part2+1):
            result_part2 = result_part2 + helper
    result.append(result_part2)
    result_part2 = 0

final = min(result)
final_number = result.index(final)

print(final_number)

print("Result of part 1 is: " + str(result_part1))
print("Result of part 2 is: " + str(final))