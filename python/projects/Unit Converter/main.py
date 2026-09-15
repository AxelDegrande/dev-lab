import sys

# Add to this list:
listOfPossibleUnitConversions = [
    "C\N{DEGREE SIGN} to F\N{DEGREE SIGN}", 
    "RPM to rad/s", 
    "bar to Pa"]

unitDict = {}
unitDictIndex = 1


for unit in listOfPossibleUnitConversions:
    unitDict[str(unitDictIndex)] = unit
    unitDictIndex += 1



def main():
    print("----UNIT CONVERTER----")
    print("Created by AD")
    print("")


    while True:
        print("What unit do you want to convert?")

        optionValue = 1
        for index in unitDict:

            print(f"\t {optionValue}. {unitDict[str(optionValue)]}")
            optionValue += 1



if __name__ in '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()    