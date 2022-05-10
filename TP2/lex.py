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

literals = ["|"]

def t_NEWLINE(t):
    r' \\n'
    print(parser.index)
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
    r'r\'\\\w+\''
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

def p_listaProducoes_recursivo(p):
    "listaProducoes : listaProducoes NEWLINE producao "
    print("producoes producao")
    
    pass

def p_listaProducoes_elemento(p):
    "listaProducoes : producao newlines"
    parser.dicionarioLista = []
    pass


def p_listaProducoes_newline(p):
    "listaProducoes : listaProducoes newlines"
    print("entrou")
    parser.dicionarioLista = []
    pass

def p_producao(p):
    "producao : ladoEsq ARROW ladoDir"
    pass

def p_ladoEsq (p):
    "ladoEsq : SIMBNAOTERMINAIS"
    parser.key = p[1]
    parser.keyOU = p[1]
    key = ''
    keyOU = ''
    pass



def p_newlines(p):
    "newlines : producoesSimples OU producaoSimples"
    parser.dicionarioOU = []
    print("entrou2")
    pass

def p_newlinesSimp(p):
    "producoesSimples : "
    pass

def p_producaoSimples(p): 
    "producaoSimples : '|' ladoDirOU END"
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
    if (re.search('\_ProducaoOU',key)!=True):
         f.write("def rec"+ key)
