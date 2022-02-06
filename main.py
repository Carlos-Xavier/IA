from forward import Forward
from backward import Backward
import var

class Main():
    def __init__(self):
        self.questions = var.questions
        self.backward = Backward()
        self.forward = Forward()
        self.MT = list()
        self.diagnoses = list()
        self.start()

    def addDiagnoses(self, mt):
        if mt not in self.diagnoses:
            self.diagnoses.append(mt)

    def start(self):
        deletados = []
        for item in var.rules:
            items = item.split(' E ')
            temp = [value in deletados for value in items]
            if True in temp: continue

            for rule in items:
                
                if not var.vars[rule]:
                    value = ""
                    if rule != "cansaço" and rule != "garganta_inflamada" and rule != "privação_de_sono":
                        print(self.questions[rule])
                        value = input("Yes or No:\n").lower()
                    

                    if value == "yes":
                        var.vars[rule] = True
                    else:
                        var.vars[rule] = False
                        deletados.append(rule)
        
                    self.forward.search(self.addDiagnoses)
                    self.backward.search(rule)

        print(self.diagnoses)


Main()