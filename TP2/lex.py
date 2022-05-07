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
          'NEWLINE'
]

literals = ["|"]

def t_NEWLINE(t):
    r' \\n'
    return t 
  
def t_REGEX(t):
    r't_\w+' 
    print("entrou1")
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
    print("entrou")
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
    "gramatica : REGEX REGEX2 REGEX3 GRAM listaProducoes"
    pass

def p_gramatica_empty(p):
    "gramatica :"
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
    print(p[2])
    pass
                                  
def p_ladoEsq (p):
    "ladoEsq : SIMBNAOTERMINAIS"
    pass
    
def p_ladoDir_simbter(p):
    "ladoDir : SIMBTERMINAIS"
    print(p[1])
    pass

def p_ladoDir_epsilon(p):
    "ladoDir : EPSILON "
    pass

def p_ladoDir_rec(p):
    "ladoDir : recursividade SIMBTERMINAIS"
    #p.parser.listaTokens.add(p[2])
    print(p[2])
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


tokens_regex = {}


arq = open("C:\\Users\\edi8b\\OneDrive\\Ambiente de Trabalho\\texto2.txt","r+")
f = arq.readlines()
for linha in f:
    parser.parse(linha)
    print(lexer.token())
    print(linha)
    regex = re.search('(t_)(\w+) :: (r\')(.+)(\')',linha) 
    if regex: 
        tokens_regex[regex.group(2)] = regex.group(4)
    if (parser.error== True) :
              print("erro na gramatica construida ")
    else :
        print("sucesso")

try: 
    print(tokens_regex) 
except KeyError: 
    print('key not present') 
 

