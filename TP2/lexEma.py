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
          'EPSILON',
          'ARROW',
          'NEWLINE',
          'OU',
          'END'
]

literals = ["|", "&"]

def t_NEWLINE(t):
    r' \\n'
    return t 

def t_END(t):
    r'\\endOU'
    parser.index = parser.index + 1
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

def t_EPSILON(t):
    r'\$ '
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
    pass

def p_regexSim(p):
    "regexs : regex"
    pass

def p_gramatica_empty(p):
    "gramatica :"
    pass


def p_listaProducoes_newline2(p):
    "listaProducoes : listaProducoes lista NEWLINE"
    print("producoes")
    parser.dicionarioLista = []
    pass

def p_listaProducoes_empty(p): 
    "listaProducoes : producao NEWLINE"
    print("empty")
    pass

def p_lista_simp(p):
    "lista : producao"
    print("producao")
    parser.dicionarioLista = []
    
def p_lista_elemento(p):
    "lista : lista producao"
    print("producao")
    parser.dicionarioLista = []
    pass

def p_producao(p):
    "producao : ladoEsq ARROW ladoDir newlines"
    print("verificando producao")
    pass

def p_prod (p):
    "producao : '&' ladoEsq ARROW ladoDir "
    print("verificando producao &&")
    pass

def p_ladoEsq (p):
    "ladoEsq : SIMBNAOTERMINAIS"
    print("lado esquerdo", p[1])
    parser.key = p[1]
    parser.keyOU = p[1]
    key = ''
    keyOU = ''
    parser.index = 0
    pass




def p_newlines(p):
    "newlines : newlines producaoSimples"
    parser.dicionarioOU = []
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
    print("terminou ou")
    pass
    
def p_ladoDirOU(p):
    "ladoDirOU : SIMBTERMINAIS"
    parser.dicionarioOU.append(p[1])
    p.parser.listaTokens.append(p[1])
    parser.dicionarioFirstFollow[parser.keyOU+"_" + str(parser.index) ] = parser.dicionarioOU 
    pass

def p_ladoDirOU_epsilon(p):
    "ladoDirOU : EPSILON"
    parser.dicionarioOU.append(p[1])
    p.parser.listaTokens.append(p[1])
    parser.dicionarioFirstFollow[parser.keyOU+"_" + str(parser.index) ] = parser.dicionarioOU 
    pass

def p_ladoDirOU_rec(p):
    "ladoDirOU : recursividadeOu SIMBTERMINAIS"  
    parser.dicionarioOU.append(p[2])
    p.parser.listaTokens.append(p[2])
    parser.dicionarioFirstFollow[parser.keyOU+"_" + str(parser.index) ] = parser.dicionarioOU 
    pass

def p_recursividadeOU(p):
    "recursividadeOu : SIMBNAOTERMINAIS"   
    parser.dicionarioOU.append(p[1])
    p.parser.listaTokens.append(p[1])
    parser.dicionarioFirstFollow[parser.keyOU+"_" + str(parser.index) ] = parser.dicionarioOU 
    pass      

def p_ladoDir_simbter(p):
    "ladoDir : SIMBTERMINAIS"
    parser.dicionarioLista.append(p[1])
    p.parser.listaTokens.append(p[1])
    parser.dicionarioFirstFollow[parser.key] = parser.dicionarioLista
    pass

def p_ladoDir_epsilon(p):
    "ladoDir : EPSILON "
    parser.dicionarioLista.append(p[1])
    p.parser.listaTokens.append(p[1])
    pass

def p_ladoDir_rec(p):
    "ladoDir : recursividade SIMBTERMINAIS"
    p.parser.listaTokens.append(p[2])
    parser.dicionarioLista.append(p[2])
    parser.dicionarioFirstFollow[parser.key] = parser.dicionarioLista
    pass
                       
def p_recursividade(p):
    "recursividade : SIMBNAOTERMINAIS"
    parser.dicionarioLista.append(p[1])
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
tokens_regex = {}

listaAIntersetar = []
def calculaLook (): #está em ciclo infinito
    for key in parser.dicionarioFirstFollow:
        if (re.search("_",key)):
            print(parser.dicionarioFirstFollow[key][0])
            if(re.search('[A-Z]\w*',parser.dicionarioFirstFollow[key][0])):
                print("realizar follow")
              #  follow(parser.dicionarioFirstFollow[key][0])
            else :
                print("estamos perante um first",parser.dicionarioFirstFollow[key][0])
        else:
            print("RESULTADO de FIRST:", parser.dicionarioFirstFollow[key][0])
    print(listaAIntersetar)
    

def follow(keyFollow): #está em ciclo infinito
    print("a procurar",keyFollow)
    for key in parser.dicionarioFirstFollow:
        print("EM BUSCA ...", key)
        if (key==keyFollow):
            print("encontrei key , resultado", parser.dicionarioFirstFollow[key][0])  
            if (re.search('[A-Z]\w*',parser.dicionarioFirstFollow[key][0])):  #verificar se é SNT
                    print("temos que fazer follow")
                    follow(parser.dicionarioFirstFollow[key][0])
        keyOU = key.split("_") #verificar se o SNT tem mais producoes
        print("resultado do split", keyOU)  
        if (keyOU[0]==keyFollow):
            print("procura do OU")
            print("first de ou", parser.dicionarioFirstFollow[key][0])
            if (re.search('[A-Z]\w*',parser.dicionarioFirstFollow[key][0])):  #verificar se é SNT
                print("temos que fazer follow")
                follow(parser.dicionarioFirstFollow[key][0])
    
    
arq = open("C:\\Users\\edi8b\\OneDrive\\Ambiente de Trabalho\\texto2.txt","r+")
f = arq.readlines()
i=0
for linha in f:
    print(parser.index)
    parser.parse(linha)
    regex = re.search('(t_\w+) :: (r\')(.+)(\')',linha) 
    if regex: 
        tokens_regex[regex.group(1)] = '"' +regex.group(3) +'"'
    parser.index = parser.index + 1
    print(parser.dicionarioFirstFollow)
    calculaLook()
    if (parser.error== True) :
              print("erro na gramatica construida ")
    else :
        print("sucesso")
    
try: 
    print(tokens_regex) 
except KeyError: 
    print('key not present') 
    

import sys
print("insira o nome do ficheiro que pretende ")
nome = input()
iteratorForTokens = 0
f = open(nome+".py", 'w')
f.write("tokens = [")
i=0
for i in range(len(parser.listaTokens)) :
    if i==len(parser.listaTokens)-1 :
        f.write('"'+parser.listaTokens[i] +'"'+ "]\n")
    else :
        f.write('"'+parser.listaTokens[i]+'"' + ",")
    
f.write("import ply.lex as lex\n")
for key in tokens_regex:
    f.write(key)
    f.write("=")
    f.write(tokens_regex[key])
    iteratorForTokens+=1

f.write("\n \nt_ignore = ' \\t\\n' \n\ndef t_error(t): \n")

f.write(" print")
f.write(" ( " + '"' )
f.write("Illegal Character:")
f.write('"' )
f.write( "+ t.value[0]) \n")
f.write(" t.lexer.skip(1) \n \n")
for key in parser.dicionarioFirstFollow:
    if (re.search('\_',key)!=True):
         f.write("def rec"+ key)
