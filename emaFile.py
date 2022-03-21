#import csv
from fileinput import filename
import os
import re
import ast
#import json
from itertools import islice
import pickle



arquivo = open('alunos.csv',encoding='utf-8')
#arquivo2 = open('alunos.csv',encoding='utf-8')

firstline = arquivo.readlines()[0].rstrip()
lista = firstline.split(",")

tamanho = len(lista)

i=0


listaparajson = []
file = open('alunos.csv',encoding='utf-8')
texto = file.readlines()
dicionario = {}
j = 0
for linha in texto:
        i=0
        #print(linha)
        #linha.split("\n")
        listaNotas= []
        mydic = {}
        while i<tamanho:
            #print(i)
            #print(linha)
            list = linha.rstrip('\n').split(",")
            #print(list[i])
            pattern = '\d+'
            pattern2 = 'tpc'
            result2 = re.match(pattern2,lista[i])
            result = re.match(pattern, list[i])
            if(result):
                listaNotas.append(int(list[i]))
            #print(list)
            if(not result2):
               mydic[lista[i]] = list[i]
            i=i+1
        mydic["Notas"] = listaNotas
        dicionario[j] = mydic
        j=j+1
    
    #s    print(mydic)
       # l = str(mydic)
       # print(l) 
 
    

if (os.path.isfile('ficheiro.jsp')==True):
    os.remove('ficheiro.jsp')
   
file = open('ficheiro.jsp','w')        

file.write('[')
file.write('\t')
#print (mydic)
k=0
print(dicionario)
tamanhodic = len(dicionario)
print(tamanhodic)
while k < tamanhodic-1:
    k=k+1
    file.write('\n')
    file.write('\t')
    file.write('{')
    file.write('\n')
    for key in dicionario[k]:
        dic = {}
        dic = dicionario[k]
        file.write('\t')
        file.write('\t')
        file.write(key)
        file.write(':')
        value = dic[key]
        file.write(str(value))
        file.write('\n')
    file.write('\t')
    file.write('},')
file.write('\n')

file.write('\t')
file.write('}')
file.write('\n')

file.write(']')
