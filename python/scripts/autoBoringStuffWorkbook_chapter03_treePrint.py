print("How big is the tree?")
treeRows = int(input("> "))
print("")

for row in range(1, treeRows+1):
    print(" " * (treeRows-row) + "*" * ((row*2)-1))
    if (row == treeRows):
        print(" " * (treeRows-1) + "#")
        print(" " * (treeRows-1) + "#")