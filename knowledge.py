class Rule():
    def __init__(self, IF, THEN):
        self.IF = IF
        self.THEN = THEN
        self.action = self.getAction()

    def getAction(self):
        pass


class Knowledge():
    def __init__(self, MT):
        self.__MT = MT
        self.__rules = list()

    def getMT(self):
        return self.__MT

    def getRules(self):
        return self.__rules

    def addRule(self, IF, THEN):
        self.__rules.append(Rule(IF, THEN))