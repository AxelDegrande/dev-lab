import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.disable(logging.DEBUG)


compasDirections = ["N", "n", "E", "e", "S", "s", "W", "w"]
userDirections = []



def get_end_coordinates(directions):
    X = 0
    Y = 0

    for i in directions:
        logging.debug(str(i))
        if i == "N":
            Y = Y + 1
        elif i == "S":
            Y = Y - 1
        elif i == "E":
            X = X + 1
        elif i == "W":
            X = X - 1

        logging.debug(str(X))
        logging.debug(str(Y))

    return X, Y                    




while True:
    print("Enter a direction: N, E, S, W:")
    direction = input("> ")
    if direction in compasDirections:
        userDirections.append(direction.upper())

    if direction == "":
        break    


coordinatesX, coordinatesY = get_end_coordinates(userDirections)
print(str(coordinatesX) + " " + str(coordinatesY))