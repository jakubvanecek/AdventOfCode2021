
File = open("Source/SourceDay2")

Lines = File.readlines()


x = 0
y = 0

for Line in Lines:
    Direction, Distance = Line.rsplit(' ')

    if Direction == "up":
        y = y - int(Distance)
    elif Direction == 'down':
        y = y + int(Distance)
    elif Direction == 'forward':
        x = x + int(Distance)


print('Celkova vzdalenost je: ',y * x)

#Part 2

File = open("Source/SourceDay2")

Lines2 = File.readlines()


Horizontal = 0
Vertical = 0
Aim = 0

for Line in Lines2:
    Direction, Distance = Line.rsplit(' ')

    if Direction == "up":
        Aim = Aim - int(Distance)
    elif Direction == 'down':
        Aim = Aim + int(Distance)
    elif Direction == 'forward':
        Horizontal = Horizontal + int(Distance)
        Vertical = (Aim * int(Distance)) + Vertical


print('Celkova vzdalenost je: ',Vertical * Horizontal)
