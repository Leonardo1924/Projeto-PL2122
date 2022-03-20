#import csv
from fileinput import filename
import os
import re
import ast
#import json
import pickle



arquivo = open('alunos.csv',encoding='utf-8')
#arquivo2 = open('alunos.csv',encoding='utf-8')

firstline = arquivo.readlines()[0].rstrip()
lista = firstline.split(",")

tamanho = len(lista)
mydic = {}
i=0


listaparajson = []
file = open('alunos.csv',encoding='utf-8')
texto = file.readlines()
for linha in texto:
        i=0
        #print(linha)
        #linha.split("\n")
        while i<tamanho:
            #print(i)
            print(linha)
            list = linha.rstrip('\n').split(",")
            print(list)
            mydic[lista[i]] = list[i]
            i=i+1
       # print(mydic)
        l = str(mydic)
       # print(l)    
        listaparajson.append(l)   
    

if (os.path.isfile('ficheiro.jsp')==True):
    os.remove('ficheiro.jsp')
   
file = open('ficheiro.jsp','w')        
#print(listaparajson)
length = len(listaparajson)
#print(length)
j=0
file.write('[')
file.write('\n')
while(j<length):
    
    if(j==0): 
        j+=1
    else: 
        lst = listaparajson[j].split(',')
      #  lst.append("\n")
        #print(len(lst))
        i=0
        while i < len(lst):
            file.write("\t")
            pattern = '^{'
            result = re.match(pattern, lst[i])
            pattern2 = '}$'
            result2 = re.search(pattern2, lst[i])
            if result:
                lst[i].split('{')
                file.write('{')
                file.write('\n\t')
                file.write(lst[i][1:])
                file.write('\n')
            elif result2: 
                  lst[i].split('}')
                  file.write(lst[i][0:-1])  
                  file.write('\n\t')
                  file.write('},')
            else:
                 file.write(lst[i])
                 file.write("\n")
            i=i+1
           
      #  print(lst)
      #  file.write(lst)
        file.write("\n")
        j+=1
file.write('\n')
file.write(']')
#s = pickle.loads(mydic)
#s = json.dumps(mydic)
#print(listaparajson)
#s = pickle.dumps(mydic)
#d = pickle.loads(s)
#l = str(mydic)

#file.write(l)
