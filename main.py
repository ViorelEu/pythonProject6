from src.bucatarie import Bucatarie

vio=Bucatarie("Bucataria noastra")
vio.adauga_ingrediente("branza",0.20)
vio.adauga_ingrediente("lapte",20)
vio.adauga_ingrediente("mazare",20)
vio.adauga_ingrediente("pate bucegi",200)
vio.adauga_ingrediente("faina",0.20)
vio.scadere_ingrediente("pere",20)
# vio.scadere_ingrediente("branza",20)
vio.scadere_ingrediente("pate bucegi",20)
vio.creati_reteta("clatite",)
print(vio.inventar)
