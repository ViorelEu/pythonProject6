import pickle

class Bucatarie:
    def __init__(self,nume):
        self.nume=nume
        self.inventar={}

    def adauga_ingredient(self,ingrediente):
        for ingredient, cantitate in ingrediente.keys():
            if ingredient in self.inventar:
                self.inventar[ingredient] += cantitate
            else:
                self.inventar[ingredient]=cantitate
            # with open('inventar.pickle', 'wb') as f:
            #     pickle.dump(self.inventar, f)


    def scade_ingrediente(self,ingrediente):
        for ingredient,cantitate in ingrediente.keys():
            if ingredient not in self.inventar or self.inventar[ingredient]<cantitate:
                raise   ValueError(f"{ingredient} insuficient")
            self.inventar[ingredient]-=cantitate
            # with open('my_object.pickle', 'rb') as f:
            #     loaded_object = pickle.load(f)
