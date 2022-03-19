import csv
import os
import re
import ast
import json
import pickle


#for linha in linhas:

#print(firstline)

os.remove('ficheiro.jsp')
file = open('ficheiro.jsp','a+')
#file.write('[\n')
#file.write('{\n')
#file.write(firstline)

arquivo = open('alunos.csv',encoding='utf-8')
arquivo2 = open('alunos.csv',encoding='utf-8')

firstline = arquivo.readlines()[0].rstrip()
lista = firstline.split(",")
tamanho = len(lista)
mydic = {}
i=0

linhas = csv.reader(arquivo2)
listaparajson = []

for linha in linhas:
    i=0
    #print(linha)
    while i<tamanho:
        #print(i)
        mydic[lista[i]] = linha[i]
        i=i+1
    l = str(mydic)
    listaparajson.append(l)   
    
          
print(listaparajson)
length = len(listaparajson)
print(length)
j=0
while(j<length):
    if(j==0): 
        j+=1
    else: 
        lst = listaparajson[j].split(",")
        print(lst)
        file.write(listaparajson[j])
        file.write("\n")
        j+=1
  
#s = pickle.loads(mydic)
#s = json.dumps(mydic)
#print(listaparajson)
#s = pickle.dumps(mydic)
#d = pickle.loads(s)
#l = str(mydic)

#file.write(l)
