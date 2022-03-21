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
               keyaux = '"' + lista[i] + '"'
               mydic[keyaux] = list[i]
            i=i+1
        mydic['"Notas"'] = listaNotas
        dicionario[j] = mydic
        j=j+1
    
    #s    print(mydic)
       # l = str(mydic)
       # print(l) 
 
    
print(dicionario)
if (os.path.isfile('ficheiro.json')==True):
    os.remove('ficheiro.json')
   
file = open('ficheiro.json','w')        

file.write('[')
file.write('\t')
#print (mydic)
k=0
print(dicionario)
tamanhodic = len(dicionario)
tamanho2 = len(dicionario[k])
print(tamanhodic)
while k < tamanhodic-1:
    k=k+1
    file.write('\n')
    file.write('\t')
    file.write('{')
    file.write('\n')
    
    j=0
    for key in dicionario[k]:
        j+=1
        if (j==tamanho2):
              dic = {}
              dic = dicionario[k]
              file.write('\t')
              file.write('\t')
              file.write(key)
              file.write(':')
              value = dic[key]
              file.write(str(value))
              file.write('\n')
              
        else: 
          dic = {}
          dic = dicionario[k]
          file.write('\t')
          file.write('\t')
          file.write(key)
          file.write(':')
          value = dic[key]
          file.write(str(value))
          file.write(',')
          file.write('\n')
         
    print(k)
    if(k != tamanhodic-1):   
        file.write('\t')
        file.write('},')
      

file.write('\t')
file.write('}')
file.write('\n')

file.write(']')
