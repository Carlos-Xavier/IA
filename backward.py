from readFile import read

class Backward():
    def __init__(self):
        self.__knowledgeBase = read()
        self.start()

    def start(self):
        for rule in self.__knowledgeBase.getRules():
            print(rule.IF, rule.THEN)
        


Backward()