import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.disable(logging.DEBUG)

data_str = "Emma is good developer. Emma is a writer"


logging.debug(data_str.count("Emma"))
emmaCounter = data_str.count("Emma")

print("Emma appeared " + str(emmaCounter) + " times.")




