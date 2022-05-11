from fileinput import filename
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
    # print("entrou")
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
    # print("entrou2")
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
    print("syntax error: ", p)
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

import collections
import sys

def calcula_keys_intersetar(diccionario):

    lista_keys = []

    # Itera dobre o dicionario e guarda todas as keys numa lista
    for key in diccionario:
        lista_keys.append(key)
        # if (re.search("_",key)):
        #     print("Calcular o lookahead e intersetar com esta key", key)
        #     lista_keys.append(key)#(parser.dicionarioFirstFollow[key][0])            
        # else:
        #     print("RESULTADO de FIRST:", diccionario[key][0])
        #     continue

    # print("Lista de Keys a Intersetar: ", lista_keys)
    return lista_keys


def calcula_ids_intersetar(lista_keys_intersecao):
    lista_intersecao = []
    for element in lista_keys_intersecao:
        # Procura pela parte nominal do id da produção
        id = re.search(r'([A-Za-z]+)(|_\d+)', element)
        if id:
            lista_intersecao.append(id.group(1))
            # print("ID: ",id.group(1))
    # Ao criar um dicionário com as chaves o elemento da lista de ids necessários intersetar, este vai remover todos os ids duplicados
    lista_intersecao = list(dict.fromkeys(lista_intersecao))
    # print("Lista IDs a Intersetar: ", lista_intersecao)
    return lista_intersecao

def verifica_simbolo_nao_terminal(simbolo):
    if re.search(r'[A-Z]+',simbolo):
        return True
    return False

def interseta_listas(lista_a, lista_b, elemento_anterior, elemento_atual):
    for elemento in lista_a:
        if elemento in lista_b:
            print("A gramática não segue as regras para LL1 nas produções ", elemento_anterior, " e ", elemento_atual)
            return True
            # quit()
    return False

def follow(key,diccionario):
    pass

def first(key,diccionario_ids,diccionario):
    ids = diccionario_ids[key]
    diccionario_listas_first = {}
    lista_simbolos_nao_terminais = []
    for id in ids:
        print("ID: ", id)
        # print("ELEMENTOS: ", diccionario[id])
        for i, simbolo in enumerate(diccionario[id]):
            print("SIMBOLO: ", simbolo)
            print("I; ", i)
            if i == 0 and verifica_simbolo_nao_terminal(simbolo):
                # S -> A macas
                lista_simbolos_nao_terminais = first(simbolo,diccionario_ids,diccionario)
                # return lista_simbolos_nao_terminais
            elif i == 0:
                lista_simbolos_nao_terminais.append(simbolo)
                # print("Lista SNT: ", lista_simbolos_nao_terminais)
                # return lista_simbolos_nao_terminais
            else:
                continue
    return lista_simbolos_nao_terminais


    

# def follow(key, diccionario):
#     elementos = diccionario[key]
#     print("Elementos: ", elementos)
#     lista_aux = []
#     indice = 0
#     for value in lista_aux:
#         if indice >= 0 and not verifica_simbolo_nao_terminal(value):
#             lista_atual.append(value)
#         else:
#             if lista_atual == []:
#                 lista_atual = follow(value,diccionario)
#             else:
#                 lista_atual = lista_atual + follow(value,diccionario)
#         indice = indice + 1
#     return elementos

lista_keys_intersetar = []

def calculaLook ():

    diccionario = parser.dicionarioFirstFollow
    tamanhoDic = len(diccionario)
    # print("Tamanho Dicionario: ", tamanhoDic)

    lista_keys_intersetar = calcula_keys_intersetar(diccionario)    
    lista_ids_intersecao = calcula_ids_intersetar(lista_keys_intersetar)
    dicionario_ids = {}
    aux = []

    for id in lista_ids_intersecao:
        for key in lista_keys_intersetar:
            if re.search(id,key):
                aux.append(key)
        dicionario_ids[id] = aux
        aux = []

    print("Dicionarios ids: ", dicionario_ids)
    lista_atual = []
    lista_anterior = []
    key_anterior = ''
    index = 0

    for id in dicionario_ids:
        lista_elementos = first(id,dicionario_ids,diccionario)
        print("ID: ", id, "Lista ENT First: ", lista_elementos)

#     for id in dicionario_ids:
#         ids_intersetar = dicionario_ids[id]
#         # print("Ids Intersetar: ", ids_intersetar)
#         for key in ids_intersetar:
#             print("KEY: ",key)
#             tamanho_ids_intersetar = len(ids_intersetar)
#             if tamanho_ids_intersetar == 1:
#                 continue
#             lista_atual_aux = diccionario[key]
#             indice = 0
#             for value in lista_atual_aux:
#                 if indice >= 0 and not verifica_simbolo_nao_terminal(value):
#                     lista_atual.append(value)
#                 else:
#                     if lista_atual == []:
#                         lista_atual = follow(value,diccionario)
#                         key_anterior = key
#                     else:
#                         lista_atual = lista_atual + follow(value,diccionario)
#                 indice = indice + 1
#             if interseta_listas(lista_anterior, lista_atual, key_anterior, key):
#                 quit()
#             else:
#                 print("index: " , index, " key: ", key, " lista Atual: ", lista_atual)
#                 lista_anterior = lista_atual
#                 lista_atual = []
#                 key_anterior = key
#         index = index + 1
#         lista_anterior = []
#         lista_atual = []
#         key_anterior = ''
        
        
# ficheiro = input("Enter the file path: ")
# arq = open(ficheiro,"r+")
arq = open("texto2.txt","r+")
f = arq.readlines()
i=0
for linha in f:
    print(parser.index)
    parser.parse(linha)
    regex = re.search('(t_\w+) :: (r\')(.+)(\')',linha) 
    if regex: 
        tokens_regex[regex.group(1)] = '"' +regex.group(3) +'"'
    parser.index = parser.index + 1
    print("Dicionario: ", parser.dicionarioFirstFollow)
    calculaLook()
    if (parser.error== True) :
      print("erro na gramatica construida ")
    else :
      print("sucesso")
    
try: 
    print(tokens_regex) 
except KeyError: 
    print('key not present') 
    

nome = input("insira o nome do ficheiro que pretende ")
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
