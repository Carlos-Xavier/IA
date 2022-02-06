import var

class Forward():
    def search(self, addDiagnoses):
        
        if var.vars["dor_de_cabeça"]:
            addDiagnoses('receitar = analgésico')
        if var.vars["dor_de_cabeça"] and var.vars["garganta_inflamada"] and var.vars["tosse"]:
            addDiagnoses('diagnóstico = gripe')
        if var.vars["cansaço"] and var.vars["dor_de_cabeça"]:
            addDiagnoses('diagnóstico = mononucleose_infecciosa')
        if var.vars["cansaço"] and var.vars["garganta_inflamada"]:
            addDiagnoses('diagnóstico = amigdalite')
        if var.vars["cansaço"]:
            addDiagnoses('diagnóstico = estresse')
        if var.vars["garganta_inflamada"] and var.vars["dor_de_garganta"] and var.vars["dor_de_ouvido"]:
            addDiagnoses('diagnóstico = faringite_estreptocócica')
        if var.vars["cansaço"] and var.vars["privação_de_sono"]:
            addDiagnoses('diagnóstico = apneia_de_sono')
        if var.vars["dor_de_ouvido"]:
            addDiagnoses('diagnóstico = otite')
        if var.vars["garganta_inflamada"]:
            addDiagnoses('receitar = Anti-inflamatórios')
        
