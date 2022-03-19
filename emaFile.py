#import csv
import os
import re
import ast
#import json
import pickle


#for linha in linhas:

#print(firstline)



#os.remove('ficheiro.jsp')
#file.write('[\n')
#file.write('{\n')
#file.write(firstline)

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
        while i<tamanho:
            #print(i)
             list = linha.split(",")
             mydic[lista[i]] = list[i]
             #print(linha[i])
             i=i+1
        l = str(mydic)
       # print(l)    
        listaparajson.append(l)   
    
file = open('ficheiro.jsp','w')        
#print(listaparajson)
length = len(listaparajson)
#print(length)
j=0
while(j<length):
    if(j==0): 
        j+=1
    else: 
        lst = listaparajson[j]
        #print(len(lst))
        #for i in range(len(lst)):
        # j = int(i)
            #  lst.insert(j,"\n")
        print(lst)
        file.write(lst)
        j+=1
  
#s = pickle.loads(mydic)
#s = json.dumps(mydic)
#print(listaparajson)
#s = pickle.dumps(mydic)
#d = pickle.loads(s)
#l = str(mydic)

#file.write(l)
