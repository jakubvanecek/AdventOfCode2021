
file = open('Source/SourceDay11', 'r')

lines = file.read().splitlines()

min = 0
y_max = len(lines)
x_max = len(lines[0])

# matrix line count
matrix = []
matrix_mask = []

matrix_line = []
matrix_mask_line = []


for line in lines:
    for x in line:
        matrix_line.append(int(x))
        matrix_mask_line.append(0)
        if len(matrix_line) % x_max == 0:
            matrix.append(matrix_line)
            matrix_mask.append(matrix_mask_line)

            matrix_line = []
            matrix_mask_line = []

shine = 0
turn = 0
to_move = [-1, 0, 1]

while turn < 10000:

    for y in range (0, len(matrix)):
        for x in range(0, len(matrix[y])):
            matrix[y][x] += 1

    did_light = 1

    while did_light == 1:
        did_light = 0
        for y in range (0, len(matrix)):
            for x in range(0, len(matrix[y])):
                if matrix[y][x] > 9 and matrix_mask[y][x] != 1:
                    matrix_mask[y][x] = 1
                    shine += 1
                    did_light = 1

                    for new_x in to_move:
                        new_x += x
                        for new_y in to_move:
                            new_y += y

                            if new_x >= min and new_y >= min and new_x < x_max and new_y < y_max and (new_x != x or new_y != y):
                                matrix[new_y][new_x] += 1


    not_all = True

    for y in range (0, len(matrix)):
        for x in range(0, len(matrix[y])):
            if matrix[y][x] < 10:
                not_all = False

            if matrix[y][x] > 9 and matrix_mask[y][x] == 1:
                matrix[y][x] = 0
                matrix_mask[y][x] = 0

    turn += 1

    if turn == 100:
        print(f'{shine} pro 100 skok')

    if not_all == True:
        print(f'{turn} vsichni najednou')
        turn = 10000







