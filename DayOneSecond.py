file1 = open('Source/SourceDay1', 'r')
Lines = file1.readlines()

# List promennych
list = []
x = 0

for x in range(5000):
 list.append(str(x))
 x=x+1

# Promenne
PocetRadku = len(Lines)
Porovnani = 0
Vysledek = 0
CisloPromenne = 0
CisloRadku=0
hodnotaA = 0
hodnotaB = 0
hodnotaC = 0
hodnotaD = 0
A = 0
B = 0
C = 0
D = 0
mn = 0


for num in Lines:
    CisloRadku = CisloRadku + 1
    #Prvni namapovani
    if CisloRadku == 1:
        A = list[CisloPromenne]
        CisloPromenne= CisloPromenne + 1
        B = list[CisloPromenne]
        CisloPromenne = CisloPromenne + 1
        C = list[CisloPromenne]
        CisloPromenne = CisloPromenne + 1
        D = list[CisloPromenne]

    # Sloupec A
    if (1+CisloRadku)%4==0:
        hodnotaA = hodnotaA + int(num)
        if (Porovnani!=0):
            if Porovnani < hodnotaA:
                Porovnani = hodnotaA
                Vysledek = Vysledek + 1
                # print(A, ' = ', Porovnani, "increased", Vysledek)
            else:
                Porovnani = hodnotaA
                # print(A, ' = ', Porovnani, "decreased",'a')
        else:
            Porovnani = hodnotaA
            # print(A, ' = ', hodnotaA, 'privni hodnota')
        hodnotaA = 0
        CisloPromenne = CisloPromenne + 1
        A = list[CisloPromenne]

    elif CisloRadku > 0 and CisloRadku%4!=0 and PocetRadku-CisloRadku>=2:
        hodnotaA = hodnotaA + int(num)

    # Sloupec B
    if CisloRadku%4==0:
        hodnotaB = hodnotaB + int(num)
        if Porovnani < hodnotaB:
            Porovnani = hodnotaB
            Vysledek = Vysledek + 1
            # print(B, ' = ', Porovnani, "increased", Vysledek)
        else:
            Porovnani = hodnotaB
            # print(B, ' = ', Porovnani, "decreased",'bb')
        hodnotaB = 0
        CisloPromenne = CisloPromenne + 1
        B = list[CisloPromenne]

    elif CisloRadku > 1 and (CisloRadku-1)%4!=0 and PocetRadku%4!=25:
        hodnotaB = hodnotaB + int(num)



    # Sloupec C
    if (CisloRadku - 1)%4==0 and CisloRadku-2 > 0:
        hodnotaC = hodnotaC + int(num)
        if Porovnani < hodnotaC:
            Porovnani = hodnotaC
            Vysledek = Vysledek + 1
            # print(C, ' = ', Porovnani, "increased ", Vysledek)
        else:
            Porovnani = hodnotaC
            # print(C, ' = ', Porovnani, "decreased", 'c')

        hodnotaC = 0
        CisloPromenne = CisloPromenne + 1
        C = list[CisloPromenne]

    elif CisloRadku > 2 and (CisloRadku-2)%4!=0 and PocetRadku+2-CisloRadku>=3:
        hodnotaC = hodnotaC + int(num)

    # Sloupec D
    if (CisloRadku-2)%4==0 and CisloRadku - 3 > 0:
        hodnotaD = hodnotaD + int(num)
        if Porovnani < hodnotaD:
            Porovnani = hodnotaD
            Vysledek = Vysledek + 1
            # print(D, ' = ', Porovnani, "increased", Vysledek)
        else:
            Porovnani = hodnotaD
            # print(D, ' = ', Porovnani, "decreased", 'd')

        hodnotaD = 0
        CisloPromenne = CisloPromenne + 1
        D = list[CisloPromenne]

    elif CisloRadku > 3 and (CisloRadku-3)%4!=0 and PocetRadku+3-CisloRadku>=3:
        hodnotaD = hodnotaD + int(num)

print("Zvýšeno je celkem: ",Vysledek)





