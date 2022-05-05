
B = [21,23,13,35,65,87,45,23,12]
A = [0,1,0,1,1,0,0,1,0]

##pokuspkous

for i in (0,3,6):
    if (A[i] + A[i+1] + A[i+2] == 3):
        print("A vyhrava")
for i in (0, 1, 2):
    if (A[i] + A[i+3] + A[i+6] == 3):
        print("A vyhrava")
x = 0
nevybrane = 0
for a in A:
    if a == 0:
        nevybrane = nevybrane + B[x]
    x+=1
print(nevybrane)