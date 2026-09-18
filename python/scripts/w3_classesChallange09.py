

class Scoreboard:
    def __init__(self, score):
        self.__score = score

    def getScore(self):
        return self.__score


s1 = Scoreboard(0)

print(s1.getScore())
