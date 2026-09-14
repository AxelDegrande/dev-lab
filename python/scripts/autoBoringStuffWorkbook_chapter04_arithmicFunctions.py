import sys
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
#logging.disable(logging.DEBUG)

try:
    def add(number1, number2):
        totalSum = number1
        for i in range(number2):
            totalSum = plusOne(totalSum)
        return totalSum    


    def multiply(number1, number2):
        totalMultiply = number1
        for i in range(number1):
            for j in range(number2-1):
                totalMultiply = plusOne(totalMultiply)
        return totalMultiply
        


    def plusOne(number):
        return (number + 1)  

except KeyboardInterrupt:
    sys.exit()     


print("First number: ")
usrNumber1 = int(input("> "))
print("Second number: ")
usrNUmber2 = int(input("> "))

endValue = multiply(usrNumber1, usrNUmber2)

print(str(endValue))