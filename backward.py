import var

class Backward():
    def search(self, mt):

        if "garganta_inflamada" == mt:
            print("Você está com dor de garganta ?")
            value = input("Yes or No:\n").lower()
            if value == "yes":
                var.vars["dor_de_garganta"] = True
                var.vars["garganta_inflamada"] = True
       
        if "cansaço" == mt:
            print("Você está com problemas para dormir ?")
            value = input("Yes or No:\n").lower()
            if value == "yes":
                var.vars["cansaço"] = True
                var.vars["privação_de_sono"] = True


        

        