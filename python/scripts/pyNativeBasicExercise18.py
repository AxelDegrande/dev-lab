import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.disable(logging.DEBUG)

value = 1238
reversedSum = 0
logging.debug(len(str(value)))

for i in range(len(str(value))):
    extractLastDigit = value % 10
    extractOtherDigit = value // 10
    reversedSum = (reversedSum * 10) +extractLastDigit
    value = extractOtherDigit
    logging.debug(reversedSum)

print(reversedSum)


