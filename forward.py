from readFile import read

class forward():

    dor_de_cabeca = False
    garganta_inflamada = False
    dor_de_garganta = False
    tosse = False
    cansaco = False
    dor_de_ouvido = False
    privacao_de_sono = False
    diagnoses = []
    
    def __init__(self):
        self.__knowledgeBase = read()
        self.start()

    def start(self):
        for rule in self.__knowledgeBase.getRules():
            print(rule.IF, rule.THEN)
            
    def isValid(self,symptoms):
        
         if symptoms == 'dor_de_cabeça':
              self.dor_de_cabeca = True
         elif symptoms == 'dor_de_cabeça E garganta_inflamada E tosse':
             if self.dor_de_cabeca and self.garganta_inflamada and self.tosse:
                 self.diagnoses.append('diagnóstico = gripe')
         elif symptoms == 'cansaço E dor_de_cabeça':
             if self.cansaco and self.dor_de_cabeca:
                 self.diagnoses.append('diagnóstico = mononucleose_infecciosa')
         elif symptoms == 'cansaço E garganta_inflamada':
             if self.cansaco and self.garganta_inflamada:
                 self.diagnoses.append('diagnóstico = amigdalite')
         elif symptoms == 'cansaco':
             if self.cansaco:
                 self.diagnoses.append('diagnóstico = estresse')
         elif symptoms == 'dor_de_garganta':
             if self.dor_de_garganta:
                 self.garganta_inflamada = True
                 self.diagnoses.append('garganta_inflamada')
         elif symptoms == "garganta_inflamada E dor_de_garganta E dor_de_ouvido":
             if self.garganta_inflamada and self.dor_de_garganta and self.dor_de_ouvido:
                 self.diagnoses.append('diagnóstico = faringite _estreptocócica')
         elif symptoms == "privação_de_sono":
             if self.privacao_de_sono:
                 self.cansaco = True
                 self.diagnoses.append('cansaço')
         elif symptoms == 'cansaço E privação_de_sono':
             if self.cansaco and self.privacao_de_sono:
                 self.diagnoses.append('diagnóstico = apneia_de_sono')
         elif symptoms == 'dor_de_ouvido':
             if self.dor_de_ouvido:
                 self.diagnoses.append('diagnóstico = otite')
         elif symptoms == 'garganta_inflamada':
             if self.garganta_inflamada:
                 self.diagnoses.append('receitar = Anti-inflamatórios')
                  
             
         
    def checkOut(self):
        for rule in self.__knowledgeBase.getRules():
             self.isValid(rule.IF)


forward()
