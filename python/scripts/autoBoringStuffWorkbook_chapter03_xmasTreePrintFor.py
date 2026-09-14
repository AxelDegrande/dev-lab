import random

numLeaves = ""

print("How big is the tree?")
treeRows = int(input("> "))
print("")

for row in range(1, treeRows+1):
    numSpaces = " " * (treeRows-row)

    for i in range(1, (row*2)):
        r = random.randint(1, 10)
        if (r == 1): # If the chance is 1 in 10, place an "o"
            numLeaves = numLeaves + "o"
        else:
            numLeaves = numLeaves + "*"

    print(numSpaces+numLeaves)

    numLeaves = ""            

    if (row == treeRows):
        print(" " * (treeRows-1) + "#")
        print(" " * (treeRows-1) + "#")