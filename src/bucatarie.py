from src.reteta import Reteta
class Bucatarie:
    def __init__(self,nume,reteta):
        self.nume=nume
        self.inventar={}
    def adauga_ingrediente(self,nume,cantitatea):
        if nume  not in self.inventar.keys():
            self.inventar[nume]= cantitatea
        else:
            self.inventar[nume]+= cantitatea

    def scadere_ingrediente(self,nume,cantitatea):
        if nume in self.inventar.keys():
            if cantitatea <= self.inventar[nume]:
                self.inventar[nume] -= cantitatea
            else:
                raise Exception("Nu sunt destule ingrediente")

    def creati_reteta(self):
        self.reteta=[]
        self.reteta.append()

    def retete_disponibile(self):












