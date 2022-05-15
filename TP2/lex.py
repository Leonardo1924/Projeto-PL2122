import ply.lex as lex
import re
import collections
import tokenize

tokens = [ 
          'REGEX',
          'REGEX2',
          'REGEX3',
          'GRAM',
          'SIMBTERMINAIS',
          'SIMBNAOTERMINAIS',
          'ARROW',
          'NEWLINE',
          'OU',
          'END',
]

literals = ["|", "$", "&"]

def t_NEWLINE(t):
    r' \\n'
    return t 

def t_END(t):
    r'\\endOU'
    return t 

def t_OU(t):
    r'\\initOU'
    return t

def t_REGEX(t):
    r't_\w+' 
    return t
    
def t_REGEX2(t):
    r'::'
    return t
  
def t_REGEX3(t):
    r'r\'(\\)?\w+\''
    return t  

def t_GRAM(t):
    r'GRAMATICA'
    return t

def t_SIMBTERMINAIS(t):
    r'[a-z]\w* '
    return t

def t_SIMBNAOTERMINAIS(t):
    r'[A-Z]\w* '
    return t

def t_ARROW(t):
    r'\-\>'
    return t

t_ignore = ' \t'

def t_error(t):
	print("Illegal Character: " + t.value[0])
	t.lexer.skip(1)


lexer = lex.lex()
import ply.yacc as yacc 


def p_gramatica(p):
    "gramatica : regexs GRAM listaProducoes"
    pass

def p_regexs(p):
    "regexs : regexs regex"
    pass

def p_regex(p):
    "regex : REGEX REGEX2 REGEX3"
    parser.regexs.append(p[1]+'='+p[3])
    
    pass

def p_regexSim(p):
    "regexs : regex"
    pass

def p_gramatica_empty(p):
    "gramatica :"
    pass


def p_listaProducoes_newline2(p):
    "listaProducoes : listaProducoes lista NEWLINE"
    parser.dicionarioLista = []
    pass

def p_listaProducoes_empty(p): 
    "listaProducoes : producao NEWLINE"
    pass

def p_lista_simp(p):
    "lista : producao"
    parser.dicionarioLista = []
    
def p_lista_elemento(p):
    "lista : lista producao"
    parser.dicionarioLista = []
    pass

def p_producao(p):
    "producao : ladoEsq ARROW ladoDir newlines"
    pass

def p_prod (p):
    "producao : '&' ladoEsq ARROW ladoDir"
    pass

def p_ladoEsq (p):
    "ladoEsq : SIMBNAOTERMINAIS"
    parser.key = p[1]
    parser.keyOU = p[1]
    key = ''
    keyOU = ''
    parser.index = 0
    parser.dicionarioLista = []
    pass


def p_newlines(p):
    "newlines : newlines producaoSimples"
    parser.dicionrioOU = []
    pass

def p_newlines2(p):
    "newlines : producaoSimples"
    parser.dicionarioOU = []
    pass
def p_newlines3(p):
    "newlines : "
    parser.dicionarioOU = []
    pass

def p_producaoSimples(p): 
    "producaoSimples : OU '|' ladoDirOU END "
    parser.index+=1
    pass
    
def p_ladoDirOU(p):
    "ladoDirOU : recursividadeOu2 SIMBTERMINAIS"
    parser.dicionarioOU.append(p[2])
    p.parser.listaTokens.append(p[2])
    parser.dicionarioFirstFollow[parser.keyOU+"_" + str(parser.index) ] = parser.dicionarioOU 
    pass

def p_ladoDirOU_epsilon(p):
    "ladoDirOU : '$'"
    parser.dicionarioOU.append(p[1])
    p.parser.listaTokens.append(p[1])
    parser.dicionarioFirstFollow[parser.keyOU+"_" + str(parser.index) ] = parser.dicionarioOU 
    pass

def p_ladoDirOU_rec(p):
    "ladoDirOU : recursividadeOu recursividadeOu2 SIMBTERMINAIS"  
    parser.dicionarioOU.append(p[3])
    p.parser.listaTokens.append(p[3])
    parser.dicionarioFirstFollow[parser.keyOU+"_" + str(parser.index) ] = parser.dicionarioOU 
    pass

          
def p_recursividadeOU2(p):
    "recursividadeOu2 : recursividadeOu2 SIMBTERMINAIS"
    parser.dicionarioOU.append(p[2])
    parser.dicionarioFirstFollow[parser.keyOU+"_" + str(parser.index) ] = parser.dicionarioOU 
    pass 
           
def p_recursividadeOU2_single(p):
    "recursividadeOu2 :"   
    pass      


def p_recursividadeOU(p):
    "recursividadeOu : SIMBNAOTERMINAIS"   
    parser.dicionarioOU.append(p[1])
    p.parser.listaTokens.append(p[1])
    parser.dicionarioFirstFollow[parser.keyOU+"_" + str(parser.index) ] = parser.dicionarioOU 
    pass      

          
def p_recursividadeOU_single(p):
    "recursividadeOu : recursividadeOu SIMBNAOTERMINAIS"
    parser.dicionarioLista.append(p[2])
    parser.dicionarioFirstFollow[parser.key] = parser.dicionarioLista
    pass 
           
def p_rec_empty(p):
    "recursividade : SIMBNAOTERMINAIS" 
    parser.dicionarioLista.append(p[1])
    parser.dicionarioFirstFollow[parser.key]= parser.dicionarioLista
    pass 
          
def p_recursividade(p):
    "recursividade : recursividade SIMBNAOTERMINAIS"
    parser.dicionarioLista.append(p[2])
    parser.dicionarioFirstFollow[parser.key] = parser.dicionarioLista
    pass 
   
def p_rec2_empty(p):
    "recursividade2 : " 
    pass 
          
def p_recursividade2(p):
    "recursividade2 : recursividade2 SIMBTERMINAIS"
    parser.dicionarioLista.append(p[2])
    parser.dicionarioFirstFollow[parser.key] = parser.dicionarioLista
    pass 
   
def p_ladoDir_rec(p):
    "ladoDir : recursividade recursividade2 SIMBTERMINAIS"
    p.parser.listaTokens.append(p[3])
    parser.dicionarioLista.append(p[3])
    parser.dicionarioFirstFollow[parser.key] = parser.dicionarioLista
    pass

def p_ladoDir_simbter(p):
    "ladoDir : recursividade2 SIMBTERMINAIS"
    parser.dicionarioLista.append(p[2])
    p.parser.listaTokens.append(p[2])
    parser.dicionarioFirstFollow[parser.key] = parser.dicionarioLista
    pass

def p_ladoDir_epsilon(p):
    "ladoDir : '$'"
    parser.dicionarioLista.append(p[1])
    p.parser.listaTokens.append(p[1])
    parser.dicionarioFirstFollow[parser.key]= parser.dicionarioLista
    pass

def p_error(p):
    print("syntax error %s",p)
    parser.error = True
    
    
parser = yacc.yacc()
parser.listaTokens= []
parser.error = False
parser.dicionarioFirstFollow = {}
parser.index = 0
parser.dicionarioLista = []
parser.key = ''
parser.keyOU = ''
parser.dicionarioOU = []
parser.regexs = []

def calculaLook (): 
    temporaryVarForFollow =''
    temporaryVarNextForFollow = ''
    listaAIntersetar = []
    temp = list(parser.dicionarioFirstFollow.keys())[0]
    
  
    for key in parser.dicionarioFirstFollow:
        
        if (not re.search(temp,key)):
            listaAIntersetar=[]
            temp = key
        
        if(re.search("_",key)):
            if(re.search('[A-Z]\w*',parser.dicionarioFirstFollow[key][0])):
                temporaryVarForFollow= parser.dicionarioFirstFollow[key][0]
                temporaryVarNextForFollow = parser.dicionarioFirstFollow[key][1]
                follow(parser.dicionarioFirstFollow[key][0], listaAIntersetar)
                print(parser.dicionarioFirstFollow[key][0],listaAIntersetar)
                if ('$' in listaAIntersetar):
                        condicao2(parser.dicionarioFirstFollow[key][0],temporaryVarNextForFollow)
                        break
                        
             
            else :
                if (parser.dicionarioFirstFollow[key][0] in listaAIntersetar):
                        print('\033[91m'+"GRAMATICA NAO É LL1 (exit4)"+ "\033[1;97m")
                        exit(1)
                listaAIntersetar.append(parser.dicionarioFirstFollow[key][0])        
               
        else:
            if(re.search('[A-Z]\w*',parser.dicionarioFirstFollow[key][0])):
                temporaryVarForFollow= parser.dicionarioFirstFollow[key][0]
                temporaryVarNextForFollow = parser.dicionarioFirstFollow[key][1]
                follow(parser.dicionarioFirstFollow[key][0], listaAIntersetar)
                if ('$' in listaAIntersetar):
                  condicao2(parser.dicionarioFirstFollow[key][0],temporaryVarNextForFollow)
                  break
                   
                
    

            elif(re.search('[a-z]+',parser.dicionarioFirstFollow[key][0])):
                if (parser.dicionarioFirstFollow[key][0] in listaAIntersetar):
                        print('\033[91m'+"GRAMATICA NAO É LL1 (exit3)"+ "\033[1;97m")
                        exit(1)
                listaAIntersetar.append(parser.dicionarioFirstFollow[key][0])
                listaAnt = listaAIntersetar
    
       
        
  
def condicao2(keyVazia,keyFollow):
    keys = list(parser.dicionarioFirstFollow.keys())
    lista=[]
    lista2=[]
    aprocurar= keyVazia+"_"
    
    for key in keys: 
        if(re.match(aprocurar,key)):
             if(re.search('[A-Z]\w*',parser.dicionarioFirstFollow[key][0])):
                  follow(parser.dicionarioFirstFollow[key][0], lista)
             else:
                 lista.append(parser.dicionarioFirstFollow[key][0])              
    follow(keyFollow,lista2)
    a_set = set(lista) 
    b_set = set(lista2) 
  
    if (a_set & b_set): 
         print('\033[91m'+"GRAMATICA NAO É LL1 (exit6)"+ "\033[1;97m")
         exit(6)
      

def follow(keyFollow, lista): 
    

    for key in parser.dicionarioFirstFollow:
        if (key==keyFollow):
            if (parser.dicionarioFirstFollow[key][0] in lista):
                        print('\033[91m'+"GRAMATICA NAO É LL1 (exit2)"+ "\033[1;97m")
                        exit(1)
            
            lista.append(parser.dicionarioFirstFollow[key][0]) 
            
            if (re.search('[A-Z]\w*',parser.dicionarioFirstFollow[key][0])):  #verificar se é SNT
                temporaryVarForFollow= parser.dicionarioFirstFollow[key][0]
                temporaryVarNextForFollow = parser.dicionarioFirstFollow[key][1]
                follow(parser.dicionarioFirstFollow[key][0],lista)
                if('$' in lista):
                     condicao2(parser.dicionarioFirstFollow[key][0],temporaryVarNextForFollow)
                     break
                    
        keyOU = key.split("_") #verificar se o SNT tem mais producoes
       
        if ( len(keyOU)>1 ):
          if(keyOU[0]==keyFollow):
            if (parser.dicionarioFirstFollow[key][0] in lista):
                    print('\033[91m'+"GRAMATICA NAO É LL1 (exit1)"+ "\033[1;97m")
                    exit(1)
    
            lista.append(parser.dicionarioFirstFollow[key][0]) 
            if (re.search('[A-Z]\w*',parser.dicionarioFirstFollow[key][0])):  #verificar se é SNT
    
                temporaryVarForFollow= parser.dicionarioFirstFollow[key][0]
                temporaryVarNextForFollow = parser.dicionarioFirstFollow[key][1]
                follow(parser.dicionarioFirstFollow[key][0],lista)
                if ('$' in lista):
                    condicao2(parser.dicionarioFirstFollow[key][0],temporaryVarNextForFollow)
                    break

   
         
   
arq = open("C:\\Users\\edi8b\\OneDrive\\Ambiente de Trabalho\\texto2.txt","r+")
f = arq.readlines()
i=0
for linha in f:

    parser.parse(linha)
    parser.index = parser.index + 1
    print(parser.dicionarioFirstFollow)
    calculaLook()
    if (parser.error== True) :
              print("erro na gramatica construida ")
    else :
          print("sucesso")

import sys
print("insira o nome do ficheiro que pretende ")
nome = input()
iteratorForTokens = 0
f = open(nome+".py", 'w')
    
f.write("\nimport ply.lex as lex")
f.write('\n\n')
f.write("tokens = [")
i=0
for i in range(len(parser.listaTokens)) :
    if i==len(parser.listaTokens)-1 :
        f.write('"'+parser.listaTokens[i] +'"'+ "]\n")
    else :
        f.write('"'+parser.listaTokens[i]+'"' + ",")

for elem in parser.regexs :
    f.write(elem+ '\n')
    

f.write("\n \nt_ignore = ' \\t\\n' \n\ndef t_error(t): \n")

f.write(" print")
f.write(" ( " + '"' )
f.write("Illegal Character:")
f.write('"' )
f.write( "+ t.value[0]) \n")
f.write(" t.lexer.skip(1) \n \n")
f.write("lexer = lex.lex()\n")
f.write("prox_symbol = lexer.token()\n\n")
temp2 = list(parser.dicionarioFirstFollow.keys())[0]
k=0
for key in parser.dicionarioFirstFollow:
   
 
    if (len(key.split("_")) == 1):
    
         f.write("\ndef rec"+ key+"():"+"\n")
         if (re.search("[A-Z]+",parser.dicionarioFirstFollow[key][0])):
             f.write("\tif prox_symbol.type() == '"+ parser.dicionarioFirstFollow[parser.dicionarioFirstFollow[key][0]][0] + "':\n")
             i=0
             while (i<len(parser.dicionarioFirstFollow[key])):
              result = re.search("[A-Z]+",parser.dicionarioFirstFollow[key][i])
              result2= re.match("[a-z]+\w*|$",parser.dicionarioFirstFollow[key][i])
              if (result):
                  f.write("\t\trec"+result.group()+"()\n")
              if (result2):
                  f.write("\t\trecT('"+result2.group()+"')\n")
              i=i+1
         result4 =  re.match("[a-z]+\w*|\$",parser.dicionarioFirstFollow[key][0])
         if(result4): 
            f.write("\tif prox_symbol=='" + result4.group() +"':\n\t\trecT('"+result4.group()+"')\n")
         j=0
         size = len(list(parser.dicionarioFirstFollow.keys()))
         string = key+"_"
         while(j<size):
              if (not re.search(string, (list(parser.dicionarioFirstFollow.keys())[j]))):
                  j+=1
              else:
                  break
         if(j==size):
             f.write("\n\telse:\n\t\tprint('erro')\n\t\texit(2)\n")      
         
    if(re.search("_",key)):
          if (re.search("[A-Z]+",parser.dicionarioFirstFollow[key][0])):
              f.write("\telif prox_symbol.type() == '"+ parser.dicionarioFirstFollow[parser.dicionarioFirstFollow[key][0]][0] + "':\n")
              i=0
              while (i<len(parser.dicionarioFirstFollow[key])):
                 result = re.search("[A-Z]+",parser.dicionarioFirstFollow[key][i])
                 result2 =  re.match("[a-z]+\w*|$",parser.dicionarioFirstFollow[key][i])
                 if (result):
                   f.write("\t\trec"+result.group()+"()\n")
                 if (result2):
                  f.write("\t\trecT('"+result2.group()+"')\n")
                 i=i+1
          
          else:
              result3 = re.match("[a-z]+\w*",parser.dicionarioFirstFollow[key][0])
              f.write("\n\telif prox_symbol=='" + result3.group() +"':\n\t\trecT('"+result3.group()+"')\n")
          f.write("\n\telse:\n\t\tprint('erro')\n\t\texit(2)\n")  
    

   
                 
f.write('\ndef recT(t):'+ "\n\tglobal prox_symbol\n"+ "\tif prox_symbol=='t':"+ "\n\t\tprox_symbol==lexer.token()"+ "\n\telif t=='$': \n\t\tprint(\'Sucesso')" +"\n\telse: \n\t\tprint(\' erro a reconhecer t\')"+ "\n\t\texit(1) \n\n")

f.write('\n \nrecS()')    
        
