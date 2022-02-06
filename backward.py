import var

  
class Backward():
    
    def handleInput(self,rule):
     flag = True
     while flag:
        ans =  input(rule).lower()
        if ans == "sim" or ans == "não":
           flag = False
           return ans
       
    def search(self, mt):

        if "garganta_inflamada" == mt:
            ans = self.handleInput(var.questions["dor_de_garganta"][0])
            var.questions["dor_de_garganta"][1] = True
            if ans == "sim":
                var.vars["dor_de_garganta"] = True
                var.vars["garganta_inflamada"] = True
       
        if "cansaço" == mt:
            ans = self.handleInput(var.questions["privação_de_sono"][0])
            var.questions["privação_de_sono"][1] = True
            if ans == "sim":
                var.vars["cansaço"] = True
                var.vars["privação_de_sono"] = True



Backward()