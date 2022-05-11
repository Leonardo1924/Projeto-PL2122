tokens = ["macas","a","a","b","c","h"]
import ply.lex as lex
t_num="\d"
 
t_ignore = ' \t\n' 

def t_error(t): 
 print ( "Illegal Character:"+ t.value[0]) 
 t.lexer.skip(1) 
 
def recSdef recS_0def recBdef recB_1def recAdef recA_2