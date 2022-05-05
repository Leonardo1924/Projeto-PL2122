import ply.lex as lex
import re
import collections
import tokenize


tokens = [ 
          'SIMBTERMINAIS',
          'SIMBNAOTERMINAIS',
          'EPSILON',
          'ARROW',
          'NEWLINE',
          'REGEX',
          'DIV'
]

literals = ["|"]

def t_NEWLINE(t):
    r' \\n'
    return t 
  
def t_DIV(t):
    r'&&&&'  
    
def t_REGEX(t):
    r't_.+'
    
def t_SIMBTERMINAIS(t):
    r'[^A-Z\$|\->=]\w* '
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

t_ignore = ' \n\t'

def t_error(t):
	print("Illegal Character: " + t.value[0])
	t.lexer.skip(1)


lexer = lex.lex()

        
import ply.yacc as yacc 


def p_gramatica(p):
    "gramatica : regexs DIV listaProducoes"
    pass

def p_regexs(p):
    "regexs : REGEX"
    print(1)
    pass
    
def p_gramatica_vazia(p):
    "gramatica : " 
    pass

def p_listaProducoes_recursivo(p):
    "listaProducoes : listaProducoes NEWLINE producao"
    pass

def p_listaProducoes_elemento(p):
    "listaProducoes : producao"
    pass
    
def p_listaProducoes_newline(p):
    "listaProducoes : listaProducoes newline"
    pass

def p_producao(p):
    "producao : ladoEsq ARROW ladoDir"
    pass

def p_newline(p):
    "newline : NEWLINE producaoSimples"
    pass
    
def p_producaoSimples(p): 
    "producaoSimples : '|' SIMBTERMINAIS"
    pass
                                  
def p_ladoEsq (p):
    "ladoEsq : SIMBNAOTERMINAIS"
    pass
    
def p_ladoDir_simbter(p):
    "ladoDir : SIMBTERMINAIS"
    pass

def p_ladoDir_epsilon(p):
    "ladoDir : EPSILON "
    pass
def p_ladoDir_rec(p):
    "ladoDir : recursividade SIMBTERMINAIS"
    p.parser.listaTokens.add(p[2])
    pass
                       
def p_recursividade(p):
    "recursividade : SIMBNAOTERMINAIS"
    pass 
    
def p_error(p):
    print("syntax error %s",p)
    parser.error = True
    
    
parser = yacc.yacc()
parser.listaTokens=set()
parser.error = False


import sys


tokens_regex = {}
arq = open("C:\\Users\\edi8b\\OneDrive\\Ambiente de Trabalho\\texto2.txt","r+")


for linha in arq:
    parser.parse(linha)
    parser.sucess = True
    regex = re.search('(t_)(\w+) = (r\')(.+)(\')',linha) 
    if regex: 
        tokens_regex[regex.group(2)] = regex.group(4)
        print(regex.group(2))
        print(regex.group(4))
    if (parser.error== True) :
              print("erro na gramatica construida ")

try: 
    print(tokens_regex) 
except KeyError: 
    print('key not present') 