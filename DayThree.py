file = open("Source/SourceDay3")
Lines = file.readlines()

for Column in range(0,12):
    globals()[f'Column{Column}'] = 0

x = ''
y = ''

for Line in Lines:
    for Column in range(0,12):
        if int(Line[Column]) == 1:
            globals()[f'Column{Column}']= globals()[f'Column{Column}']+1
        else:
            globals()[f'Column{Column}'] = globals()[f'Column{Column}'] - 1

for Column in range(0,12):
    if globals()[f'Column{Column}'] > 0:
        x = x + str(1)
    else:
        x = x + str(0)

    if x[Column] == str(1):
        y = y + str(0)
    else:
        y = y + str(1)

print(int(x,2)*int(y,2))


