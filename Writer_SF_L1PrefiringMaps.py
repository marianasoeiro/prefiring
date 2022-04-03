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
n_all = uproot.open("L1PrefiringMaps.root")["L1prefiring_jetemptvseta_2017BtoF"].numpy()
# print(file['L1prefiring_jetpt_2016BCD']._members())
print(file['L1prefiring_jetemptvseta_2017BtoF'].pandas())
# print(file['L1prefiring_jetpt_2016BCD'].values.shape())
##Adquirir informacaoo da estrutura interna do seu arquivo root
#print(dict(file.classes()))
##[OPCIONAL] Acessando informacoes dos histogramas
#print(file['L1prefiring_jetpt_2017F'].edges)    #acesso aos limites dos bins
#print(file['L1prefiring_jetpt_2017F'].values)   #acesso aos valores dos bins
#print(file['L1prefiring_jetemptvseta_2017BtoF'].errors)
#listas que vao conter os valores do max e min do eixo X e Y bem como o valor nesses intervalos.
x_min = []
x_max = []
y_min = []
y_max = []
valores = []
err = []

#Histogram names
nomes = ['L1prefiring_jetemptvseta_2017BtoF','L1prefiring_jetptvseta_2017BtoF','L1prefiring_photonptvseta_2017BtoF','L1prefiring_jetptvseta_2016BtoH','L1prefiring_jetemptvseta_2016BtoH','L1prefiring_photonptvseta_2016BtoH','L1prefiring_jetptvseta_UL2017BtoF','L1prefiring_jetemptvseta_UL2017BtoF','L1prefiring_photonptvseta_UL2017BtoF','L1prefiring_jetptvseta_UL2016preVFP','L1prefiring_jetemptvseta_UL2016preVFP','L1prefiring_photonptvseta_UL2016preVFP','L1prefiring_jetptvseta_UL2016postVFP','L1prefiring_jetemptvseta_UL2016postVFP','L1prefiring_photonptvseta_UL2016postVFP']

def salvar_lista(nome):
    x_min = []
    x_max = []
    y_min = []
    y_max = []
    valores = []
    err = []
    for x in range(len(file[nome].edges[0])-1):
    #print('valor do bins no eixo X ',file[nome].edges[0][x])
        for y in range(len(file[nome].edges[1])-1):
        #print('valor do bins no eixo Y ',file[nome].edges[1][x])
            x_min.append(float(file[nome].edges[0][x]))
            x_max.append(float(file[nome].edges[0][x+1]))
            y_min.append(float(file[nome].edges[1][y]))
            y_max.append(float(file[nome].edges[1][y+1]))
            valores.append(float(file[nome].values[x][y]))
            err.append(float(math.sqrt(file[nome].variances[x][y])))
    return x_min,x_max,y_min,y_max,valores,err


lista_canal = []
for nome in nomes:
    x_min,x_max,y_min,y_max,valores,err = salvar_lista(nome)
    lista_canal.append([
        dict(x_min=x_min[i],x_max=x_max[i],y_min=y_min[i],y_max=y_max[i],valor=valores[i],erro = err[i])
        for i in range(len(valores))
    ])

#print(lista_canal)
dict_salvar = {nomes[0]: lista_canal[0],nomes[1]: lista_canal[1],nomes[2]: lista_canal[2],nomes[3]: lista_canal[3],nomes[4]: lista_canal[4],nomes[5]: lista_canal[5],nomes[6]: lista_canal[6],nomes[7]: lista_canal[7],nomes[8]: lista_canal[8],nomes[9]: lista_canal[9],nomes[10]: lista_canal[10],nomes[11]: lista_canal[11],nomes[12]: lista_canal[12],nomes[13]: lista_canal[13],nomes[14]: lista_canal[14]
}
#print(lista_canal,type(lista_canal))
#print(dict_salvar)

with open("L1PrefiringMaps.json", "w") as f:
    json.dump(dict_salvar,f,indent=4)

 
