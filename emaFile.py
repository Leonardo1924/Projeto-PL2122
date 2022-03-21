#import csv
from fileinput import filename
import os
import re
import ast
#import json
from itertools import islice
import pickle


nome = input ("Enter file csv path :")
print(nome)
arquivo = open(nome,encoding='utf-8')
arquivo2 = open(nome,encoding='utf-8')

firstline = arquivo.readlines()[0].rstrip()
firstline = re.sub('{\d,?\d?}','',firstline)
firstline = re.sub('::','_',firstline)

firstline2 = arquivo2.readlines()[0].rstrip()
listaFunc = firstline2.split("::")
funcao = ""
if (len(listaFunc)>1):
    funcao= listaFunc[1]
print(funcao)

funcoesValidas = ['max','min','avg','count','sum']
listaKeys = firstline.split(",")

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
                i+=1
            else: 
                keyaux = '"' + listaKeys[k] + '"'
                k+=1
                mydic[keyaux] = list[i] 
                i+=1 
        
        if (funcao==""):
             keyaux = '"' + listaKeys[k] + '"'
             k+=1
             mydic[keyaux] = listaNotas
             dicionario[j] = mydic
             j=j+1
       
        
        else: 
            if(funcao in funcoesValidas):
                 keyaux = '"' + listaKeys[k] + '"'
                 k+=1
                 fun = str(funcao)
                 if(funcao=="sum"):
                      mydic[keyaux] = sum(listaNotas)
                 elif(funcao=="avg"):
                       mydic[keyaux] = sum(listaNotas)/len(listaNotas)
                 elif(funcao=="count"):
                       mydic[keyaux] = len(listaNotas)
                 elif(funcao=="min"):
                       mydic[keyaux] = min(listaNotas)
                 elif(funcao=="max"):
                       mydic[keyaux] = max(listaNotas)
            if (funcao not in funcoesValidas):
                  keyaux = '"' + listaKeys[k] + '"'
                  k+=1
                  mydic[keyaux] = listaNotas
                 
            dicionario[j] = mydic
            j=j+1
        
       
        
    
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
