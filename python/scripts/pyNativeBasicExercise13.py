data = [10, 20, 33, 46, 55]
divisibleList = []

for value in data:
    isDivisible = value % 5
    if isDivisible == 0:
        divisibleList.append(value)

print(str(divisibleList))    
