import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
#logging.disable(logging.DEBUG)

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
result = []

for i in list1:
    if i % 2 != 0: #Uneven
        result.append(i)

for i in list2:
    if i % 2 == 0:
        result.append(i)

print(str(result))        



