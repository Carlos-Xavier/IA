from forward import Forward
from backward import Backward
import var

class Main():
    def __init__(self):
        self.backward = Backward()
        self.forward = Forward()
        self.MT = list()
        self.diagnoses = list()
        self.controlUnit()

    def addDiagnoses(self, mt):
        if mt not in self.diagnoses:
            self.diagnoses.append(mt)
            
            
    def handleInput(self,rule):
       flag = True
       while flag:
         ans =  input(rule).lower()
         if ans == "sim" or ans == "não":
             flag = False
             return ans
       
       
    def controlUnit(self):
        deleted = []
        for item in var.rules:
            items = item.split(' E ')
            temp = [value in deleted for value in items]
            if True in temp: continue
            for rule in items:
                if not var.vars[rule]:
                    ans = ""
                    if rule != "cansaço" and rule != "garganta_inflamada" and rule != "privação_de_sono":
                        if var.questions[rule][1] == None:
                            ans = self.handleInput(var.questions[rule][0])
                    if ans == "sim":
                        var.vars[rule] = True
                    else:
                        var.vars[rule] = False
                        deleted.append(rule)
                        
                    self.forward.search(self.addDiagnoses)
                    self.backward.search(rule)

        if len(self.diagnoses) == 0:
            print('Não foi possível determinar seu diagnóstico! Procure uma unidade médica mais próxima.')
        else:    
            print(self.diagnoses)


Main()