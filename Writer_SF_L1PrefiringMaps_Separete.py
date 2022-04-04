import os
import sys
import pandas as pd
import uproot3 as uproot
import numpy as np
import time
import json
import os.path
import pandas as pd
import math

#root file

file = uproot.open("L1PrefiringMaps.root")
n_all = uproot.open("L1PrefiringMaps.root")["L1prefiring_photonptvseta_UL2016postVFP"].numpy()

print(file['L1prefiring_photonptvseta_UL2016postVFP'].pandas())

x_min = []
x_max = []
y_min = []
y_max = []
value = []
err = []

#Histogram names
nomes = ['L1prefiring_jetemptvseta_2017BtoF','L1prefiring_jetptvseta_2017BtoF','L1prefiring_photonptvseta_2017BtoF','L1prefiring_jetptvseta_2016BtoH','L1prefiring_jetemptvseta_2016BtoH','L1prefiring_photonptvseta_2016BtoH','L1prefiring_jetptvseta_UL2017BtoF','L1prefiring_jetemptvseta_UL2017BtoF','L1prefiring_photonptvseta_UL2017BtoF','L1prefiring_jetptvseta_UL2016preVFP','L1prefiring_jetemptvseta_UL2016preVFP','L1prefiring_photonptvseta_UL2016preVFP','L1prefiring_jetptvseta_UL2016postVFP','L1prefiring_jetemptvseta_UL2016postVFP','L1prefiring_photonptvseta_UL2016postVFP']

def salvar_lista(nome):
    x_min = []
    x_max = []
    y_min = []
    y_max = []
    value = []
    err = []
    for x in range(len(file[nome].edges[0])-1):
    #print('valor do bins no eixo X ',file[nome].edges[0][x])
        for y in range(len(file[nome].edges[1])-1):
        #print('valor do bins no eixo Y ',file[nome].edges[1][x])
            x_min.append(float(file[nome].edges[0][x]))
            x_max.append(float(file[nome].edges[0][x+1]))
            y_min.append(float(file[nome].edges[1][y]))
            y_max.append(float(file[nome].edges[1][y+1]))
            value.append(float(file[nome].values[x][y]))
            err.append(float(math.sqrt(file[nome].variances[x][y])))
    return x_min,x_max,y_min,y_max,value,err


lista_canal = []
for nome in nomes:
    x_min,x_max,y_min,y_max,value,err = salvar_lista(nome)
    lista_canal.append([
        dict(eta_min= x_min[i],eta_max= x_max[i],pt_min= y_min[i],pt_max= y_max[i],valor= value[i],error = err[i])
        for i in range(len(value))
    ])

# All

#print(lista_canal)
#dict_salvar = {nomes[0]: lista_canal[0],nomes[1]: lista_canal[1],nomes[2]: lista_canal[2],nomes[3]: lista_canal[3],nomes[4]: lista_canal[4],nomes[5]: lista_canal[5],nomes[6]: lista_canal[6],nomes[7]: lista_canal[7],nomes[8]: lista_canal[8],nomes[9]: lista_canal[9],nomes[10]: lista_canal[10],nomes[11]: lista_canal[11],nomes[12]: lista_canal[12],nomes[13]: lista_canal[13],nomes[14]: lista_canal[14]}

#with open("L1PrefiringMaps.json", "w") as f:
    #json.dump(dict_salvar,f,indent=4)

# Separete

#dict_salvar = {nomes[0]: lista_canal[0]}
#with open("output/L1prefiring_jetemptvseta_2017BtoF.json", "w") as f:
    #json.dump(dict_salvar,f,indent=4)
#dict_salvar = {nomes[1]: lista_canal[1]}
#with open("output/L1prefiring_jetptvseta_2017BtoF.json", "w") as f:
    #json.dump(dict_salvar,f,indent=4)
#dict_salvar = {nomes[2]: lista_canal[2]}
#with open("output/L1prefiring_photonptvseta_2017BtoF.json", "w") as f:
    #json.dump(dict_salvar,f,indent=4)
#dict_salvar = {nomes[3]: lista_canal[3]}
#with open("output/L1prefiring_jetptvseta_2016BtoH.json", "w") as f:
    #json.dump(dict_salvar,f,indent=4)
#dict_salvar = {nomes[4]: lista_canal[4]}
#with open("output/L1prefiring_jetemptvseta_2016BtoH.json", "w") as f:
    #json.dump(dict_salvar,f,indent=4)
#dict_salvar = {nomes[5]: lista_canal[5]}
#with open("output/L1prefiring_photonptvseta_2016BtoH.json", "w") as f:
    #json.dump(dict_salvar,f,indent=4)
#dict_salvar = {nomes[6]: lista_canal[6]}
#with open("output/L1prefiring_jetptvseta_UL2017BtoF.json", "w") as f:
    #json.dump(dict_salvar,f,indent=4)
#dict_salvar = {nomes[7]: lista_canal[7]}
#with open("output/L1prefiring_jetemptvseta_UL2017BtoF.json", "w") as f:
    #json.dump(dict_salvar,f,indent=4)
#dict_salvar = {nomes[8]: lista_canal[8]}
#with open("output/L1prefiring_photonptvseta_UL2017BtoF.json", "w") as f:
    #json.dump(dict_salvar,f,indent=4)
#dict_salvar = {nomes[9]: lista_canal[9]}
#with open("output/L1prefiring_jetptvseta_UL2016preVFP.json", "w") as f:
    #json.dump(dict_salvar,f,indent=4)
#dict_salvar = {nomes[10]: lista_canal[10]}
#with open("output/L1prefiring_jetemptvseta_UL2016preVFP.json", "w") as f:
    #json.dump(dict_salvar,f,indent=4)
#dict_salvar = {nomes[11]: lista_canal[11]}
#with open("output/L1prefiring_photonptvseta_UL2016preVFP.json", "w") as f:
    #json.dump(dict_salvar,f,indent=4)
#dict_salvar = {nomes[12]: lista_canal[12]}
#with open("output/L1prefiring_jetptvseta_UL2016postVFP.json", "w") as f:
    #json.dump(dict_salvar,f,indent=4)
#dict_salvar = {nomes[13]: lista_canal[13]}
#with open("output/L1prefiring_jetemptvseta_UL2016postVFP.json", "w") as f:
   # json.dump(dict_salvar,f,indent=4)
dict_salvar = {nomes[14]: lista_canal[14]}
with open("output/L1prefiring_photonptvseta_UL2016postVFP.json", "w") as f:
    json.dump(dict_salvar,f,indent=4)

#print(lista_canal,type(lista_canal))
#print(dict_salvar)



 
