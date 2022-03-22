#import csv
from fileinput import filename
import os
import re
import ast
#import json
from itertools import islice
import pickle


nome = input ("Enter file csv path :")
arquivo = open(nome,encoding='utf-8')
arquivo2 = open(nome,encoding='utf-8')

firstline = arquivo.readlines()[0].rstrip()
min = re.search('(?:{)(\d)',firstline)
valmin = min.group(1)

max = re.search('(\d)(}:?)',firstline)
valmax = max.group(1)


firstline = re.sub('{\d,?\d?}','lista',firstline)
firstline = re.sub('::','_',firstline)


firstline2 = arquivo2.readlines()[0].rstrip()
funcaoaux = re.search('(::)(\w+)(,)',firstline2)

funcao=""
if (funcaoaux!=None):
    funcao = funcaoaux.group(2)
funcoesValidas = ['max','min','avg','count','sum']
listaKeys = firstline.split(",")

tamanho = len(listaKeys)

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
        while k < len(listaKeys):

                patternNum = 'lista'
                pattern2 = '^.{0}$'
                resultLista = re.search(patternNum, listaKeys[k])
                
                result2 = re.match(pattern2, list[i])
                
              
                print("tamanho lista",len(list))
                if(resultLista and not result2):
                    varlista= '"' + listaKeys[k] + '"'
                    
                   
                    while(re.match('\d+',list[i])):
                        listaNotas.append(int(list[i]))
                        print(i)
                        if(i==len(list)-1):
                          break 
                        else:
                            i+=1
                            
                    k+=1
                elif(result2):
                    i+=1 
                else: 
                    keyaux = '"' + listaKeys[k] + '"'
                    mydic[keyaux] = list[i] 
                    i+=1 
                    k+=1
        
        if (len(listaNotas)>int(valmax) or len(listaNotas)<int(valmin)):
                mydic['"Erro"'] = '"Erro no tamanho da lista"'
                
                
        if (funcao==""):
        
            varlista = re.sub('lista','',varlista)
            mydic[varlista] = listaNotas
            dicionario[j] = mydic
            j=j+1
    
        else: 
            if(funcao in funcoesValidas):
                varlista = re.sub('lista','',varlista)
                fun = str(funcao)
                if(funcao=="sum"):
                    mydic[varlista] = sum(listaNotas)
                elif(funcao=="avg"):
                    mydic[varlista] = sum(listaNotas)/len(listaNotas)
                elif(funcao=="count"):
                    mydic[varlista] = len(listaNotas)
                elif(funcao=="min"):
                    mydic[varlista] = min(listaNotas)
                elif(funcao=="max"):
                    mydic[varlista] = max(listaNotas)
            if (funcao not in funcoesValidas):
                varlista
                mydic[varlista] = listaNotas
        
        print(len(listaNotas))
        print(valmax)    
      
            
dicionario[j] = mydic
j=j+1
        

   
listaNome = nome.split('.')
nome = listaNome[0] + '.json'
if (os.path.isfile(nome)==True):
    os.remove(nome)
   
file = open(nome,'w')        

file.write('[')
file.write('\t')
#print (mydic)
y=0

tamanhodic = len(dicionario)



while y < tamanhodic:
    tamanho2 = len(dicionario[y])
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
