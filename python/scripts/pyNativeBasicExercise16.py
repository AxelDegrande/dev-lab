import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
#logging.disable(logging.DEBUG)

data = 121

data_rev = int(str(data)[::-1])

if data == data_rev:
    print("The value " + str(data) + " is a Palindrome.")
else:   
    print("The value " + str(data) + " is not aPalindrome.")





