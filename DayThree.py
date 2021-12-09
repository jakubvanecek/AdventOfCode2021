file = open("Source/SourceDay3")
Lines = file.read().splitlines()

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

## part 2

Part2 = open("Source/SourceDay3", "r")
Lines2 = Part2.read().splitlines()

Group0 = []
Group1 = []
Bit0 = 0
Bit1 = 0
Oxygen = []
C02 = []

for Part in Lines2:
    if int(Part[0]) == 1:
        Group1.append(Part)
        Bit1 = Bit1 + 1
    else:
        Bit0 = Bit0 + 1
        Group0.append(Part)

if Bit1>Bit0:
    Oxygen =  Group1
    CO2 = Group0
else:
    Oxygen = Group0
    CO2 = Group1

z = 0
rank = 0

for i in range(2):
    Type = []
    rank = 0

    if z == 1:
        Type = CO2
        CO2 = []
        Value = 0
    else:
        Type = Oxygen
        Oxygen = []
        Value = 1

    for total in range (1, 15):
        Bit0 = 0
        Bit1 = 0
        Group0 = []
        Group1 = []
        rank = rank+1

        for Sec in Type:
            if int(Sec[rank]) == 1:
                Group1.append(Sec)
                Bit1 = Bit1 + 1
            else:
                Bit0 = Bit0 + 1
                Group0.append(Sec)

        if Value == 0:
            if Bit1 > Bit0:
                Type = Group0
            elif Bit1 == Bit0:
                Type = Group0
            else:
                Type = Group1
        else:
            if Bit1 > Bit0:
                Type = Group1
            elif Bit1 == Bit0:
                Type = Group1
            else:
                Type = Group0

        z = len(Type)
        if z == 1:
            break

    if Oxygen == []:
        Oxygen = Type
    else:
        CO2 = Type

print (int(Oxygen[0],2)*int(CO2[0],2))







