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
firstline = re.sub('{\d,?\d?}','',firstline)

print(firstline)

listaKeys = firstline.split(",")
print(listaKeys)

tamanho = len(listaKeys)
print(tamanho)
i=0


listaparajson = []
file = open('alunos.csv',encoding='utf-8')
next(file)
texto = file.readlines()
dicionario = {}
j = 0

for linha in texto:
        i=0
        k=0
        #print(linha)
        #linha.split("\n")
        listaNotas= []
        mydic = {}
        list = linha.rstrip('\n').split(",")
        print(list)
        while i < len(list):
            #print(i)
            #print(linha)
            
            #print(list)
            #print(list[i])
            patternNum = '\d+'
            pattern2 = '^.{0}$'
            resultNum = re.match(patternNum, list[i])
            result2 = re.match(pattern2, list[i])
            if(resultNum):
                listaNotas.append(int(list[i]))
                i+=1
            #print(list)
            elif(result2):
                print("entrou")
                i+=1
            else: 
                keyaux = '"' + listaKeys[k] + '"'
                k+=1
                mydic[keyaux] = list[i] 
                i+=1 
           
        keyaux = '"' + listaKeys[k] + '"'
        k+=1
        mydic[keyaux] = listaNotas
        dicionario[j] = mydic
        j=j+1
    
    #s    print(mydic)
       # l = str(mydic)
       # print(l) 
 
    
print(dicionario)

if (os.path.isfile('ficheiro2.json')==True):
    os.remove('ficheiro2.json')
   
file = open('ficheiro2.json','w')        

file.write('[')
file.write('\t')
#print (mydic)
y=0

tamanhodic = len(dicionario)
tamanho2 = len(dicionario[y])

while y < tamanhodic:
    
    file.write('\n')
    file.write('\t')
    file.write('{')
    file.write('\n')
    
    j=0
    for key in dicionario[y]:
        j+=1
        if (j==tamanho2):
              dic = {}
              dic = dicionario[y]
              file.write('\t')
              file.write('\t')
              file.write(key)
              file.write(':')
              value = dic[key]
              file.write(str(value))
              file.write('\n')
              
        else: 
          dic = {}
          dic = dicionario[y]
          file.write('\t')
          file.write('\t')
          file.write(key)
          file.write(':')
          value = dic[key]
          file.write(str(value))
          file.write(',')
          file.write('\n')

    if(y != tamanhodic-1):   
        file.write('\t')
        file.write('},')
    y+=1
    
file.write('\t')
file.write('}')
file.write('\n')

file.write(']') 
