
# Using readlines()
file1 = open('Source/SourceDay1', 'r')
Lines = file1.readlines()

delka=len(Lines)

print(delka)

y=0
x = int(Lines[0])


for line in Lines:

    if int(line) > x:
        print(line.strip(), "increased")
        y= y+1
    else:
        print(line.strip(), "decreased")
    x = int(line)
print ("incresed total: ", y)




