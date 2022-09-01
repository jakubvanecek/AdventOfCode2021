import numpy as np

with open ('Source/SourceDay5', 'r') as file:
    lines = file.read().splitlines()


x1 = []
x2 = []
y1 = []
y2 = []

for line in lines:
    line = line.replace(' -> ',',')
    line = line.replace(' -> ', '')
    param1, param2, param3, param4 = line.split(',')
    x1.append(int(param1))
    x2.append(int(param3))
    y1.append(int(param2))
    y2.append(int(param4))

if (max(x1)>max(x2)):
    xMax = max(x1) + 1
else:
    xMax = max(x2) + 1

if (max(y1)>max(y2)):
    yMax = max(y1) + 1
else:
    yMax = max(y2) + 1

print(xMax, yMax)


class Sea:
    def __init__(self):
        self.board = np.zeros((yMax, xMax), dtype=int)
        self.result = 0

    def setVerticalOrHorizontal(self, ventureNumber):
        if (x1[ventureNumber] == x2[ventureNumber] or y1[ventureNumber] == y2[ventureNumber]):
            xx1 = x1[ventureNumber]
            xx2 = x2[ventureNumber]
            yy1 = y1[ventureNumber]
            yy2 = y2[ventureNumber]

            if (xx1 > xx2):
                xx2 = xx1
                xx1 = x2[ventureNumber]
            if (yy1 > yy2):
                yy2 = yy1
                yy1 = y2[ventureNumber]

            if (xx1 != xx2):
                for x in range(int(xx1), int(xx2)+1):
                    self.board[int(yy1), x] = self.board[int(yy1), x] + 1
            if (yy1 != yy2):
                for y in range (int(yy1), int(yy2+1)):
                    self.board[y, xx1] = self.board[y, xx1] + 1
            if (xx1 == xx2 and yy1 == yy2):
                self.board[yy1, xx1] = self.board[yy1, xx1] + 1

    def set_diagonal(self, venture_number):
        xx1 = x1[venture_number]
        xx2 = x2[venture_number]
        yy1 = y1[venture_number]
        yy2 = y2[venture_number]

        x_range = []
        y_range = []

        if((xx1 < xx2 and yy1 > yy2) or (xx1 > xx2 and yy1 < yy2) or (xx1 < xx2 and yy1 < yy2) or (xx1 > xx2 and yy1 > yy2)):
            if ((xx1 < xx2 and yy1 < yy2) or (xx1 > xx2 and yy1 > yy2)):
                if (xx1 > xx2 and yy1 > yy2):
                    xx2 = xx1
                    xx1 = x2[venture_number]

                    yy2 = yy1
                    yy1 = y2[venture_number]

                for x in range(int(xx1), int(xx2) + 1):
                    x_range.append(x)
                for y in range(yy1, yy2 + 1):
                    y_range.append(y)
            elif((xx1 < xx2 and yy1 > yy2) or (xx1 > xx2 and yy1 < yy2)):
                temp_range = []
                if (xx1 > xx2 and yy1 < yy2):
                    xx2 = xx1
                    xx1 = x2[venture_number]

                else:
                    yy2 = yy1
                    yy1 = y2[venture_number]

                for x in range(xx1, xx2 + 1):
                    x_range.append(x)

                for y in range(yy1, yy2 + 1):
                    temp_range.append(y)

                lenght = len(x_range)

                for l in range(0,lenght):
                    y_range.append(temp_range[lenght-l-1])

            lenght = len(x_range)

            for l in range(0,lenght):
                self.board[y_range[l], x_range[l]] = self.board[y_range[l], x_range[l]] + 1




    def checkResult(self):
        result = 0
        for numbers in self.board:
            for number in numbers:
                if (number > 1):
                    result = result + 1
        return result


horizontal = Sea()
for number in range(0,len(x1)):
    horizontal.setVerticalOrHorizontal(number)

result = horizontal.checkResult()
print('Result:' + str(result))

vertical = Sea()
for number in range(0, len(x1)):
    vertical.setVerticalOrHorizontal(number)
    vertical.set_diagonal(number)

result = vertical.checkResult()
print('Result:' + str(result))


