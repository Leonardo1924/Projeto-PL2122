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
    parser.index = parser.index + 1
    print(parser.index)
    return t 

def t_END(t):
    r'\\endOU'
    return t 

def t_OU(t):
    r'\\and'

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
    "regexs : regexs REGEX REGEX2 REGEX3"
    pass
def p_regex_empty(p):
    "regexs :"
    pass

def p_gramatica_empty(p):
    "gramatica :"
    pass

def p_listaProducoes_recursivo(p):
    "listaProducoes : listaProducoes NEWLINE producao NEWLINE"
    pass

def p_listaProducoes_elemento(p):
    "listaProducoes : producao"
    pass


def p_listaProducoes_newline(p):
    "listaProducoes : listaProducoes newline"
    print("antes do clear", parser.dicionarioFirstFollow)
    parser.dicionarioLista = []
    print("depois do clear", parser.dicionarioFirstFollow)
    pass

def p_producao(p):
    "producao : ladoEsq ARROW ladoDir"
    pass

def p_ladoEsq (p):
    "ladoEsq : SIMBNAOTERMINAIS"
   
    parser.key = p[1]
    parser.keyOU = p[1]
    print("KEYYYYYY", parser.key)
    key = ''
    keyOU = ''
    pass

def p_newline(p):
    "newline : OU producaoSimples"
    pass
    
def p_producaoSimples(p): 
    "producaoSimples : '|' SIMBTERMINAIS END"
    parser.dicionarioOU.append(p[2])
    print("key",parser.keyOU, "value", parser.dicionarioOU, "key", parser.key, "value", parser.dicionarioLista)
    parser.dicionarioFirstFollow[parser.keyOU+"_ProducaoOU"] = parser.dicionarioOU 
    print("adicionou")
    print(parser.dicionarioFirstFollow)
    
    pass
                                  

    
def p_ladoDir_simbter(p):
    "ladoDir : SIMBTERMINAIS"
    print("antes", parser.dicionarioFirstFollow, "KEY", parser.key)
    parser.dicionarioLista.append(p[1])
    print("key",parser.key, "value", parser.dicionarioLista)
    parser.dicionarioFirstFollow[parser.key] = parser.dicionarioLista
    print(parser.dicionarioFirstFollow)
    print("adicionou")
    print(p[1])
    pass

def p_ladoDir_epsilon(p):
    "ladoDir : EPSILON "
    parser.dicionarioLista.append(p[1])
    pass

def p_ladoDir_rec(p):
    "ladoDir : recursividade SIMBTERMINAIS"
    #p.parser.listaTokens.add(p[2])
    parser.dicionarioLista.append(p[2])
    print("key",parser.key, "value", parser.dicionarioLista)
    parser.dicionarioFirstFollow[parser.key] = parser.dicionarioLista
    print("adicionou")
    print(parser.dicionarioFirstFollow)
    pass
                       
def p_recursividade(p):
    "recursividade : SIMBNAOTERMINAIS"
    parser.dicionarioLista.append(p[1])
    print("key",parser.key, "value", parser.dicionarioLista)
    print("Adicionou")
    pass 
   
 
def p_error(p):
    print("syntax error %s",p)
    parser.error = True
    
    
parser = yacc.yacc()
parser.listaTokens=set()
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
    regex = re.search('(t_)(\w+) :: (r\')(.+)(\')',linha) 
    if regex: 
        tokens_regex[regex.group(2)] = regex.group(4)
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
    


