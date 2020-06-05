reservadas = {
    'goto' : 'RGOTO',
    'unset' : 'RUNSET',
    'print' : 'IMPRIMIR',
    'if' : 'IF',
    'exit' : 'SALIR',
    'read' : 'LEER',
    'int' : 'TINT',
    'float': 'TFLOAT',
    'char' : 'TCHAR',
    'abs' : 'VABSOL',
    'array' : 'ARREGLO',
    'xor' : 'XOR'
}

tokens  = [
    'PTCOMA',
    'DOSPTS',
    'CORCHA',
    'CORCHC',
    'PARA',
    'PARC',
    'IGUAL',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'MODULO',
    'NOT',
    'AND',
    'OR',
    'CEJA',
    'MENORQ',
    'MAYORQ',
    'DOBIGUAL',
    'NOIGUAL',
    'MAYORIGUALQ',
    'MENORIGUALQ',
    'POTENC',
    'ROTIZQ',
    'ROTDER',
    'DECIMAL',
    'ENTERO',
    'CADENA',
    'LABEL',
    'VARIABLE'
] + list(reservadas.values())

# Tokens
t_PTCOMA    = r';'
t_DOSPTS    = r':'
t_CORCHA   = r'\['
t_CORCHC   = r'\]'
t_PARA    = r'\('
t_PARC    = r'\)'
t_IGUAL     = r'='
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDIDO  = r'/'
t_MODULO    = r'%'
t_NOT       = r'!'
t_AND       = r'&'
t_OR        = r'\|'
t_CEJA      = r'~'
t_MENORQ    = r'<'
t_MAYORQ    = r'>'
t_DOBIGUAL  = r'=='
t_NOIGUAL   = r'!='
t_MAYORIGUALQ = r'>='
t_MENORIGUALQ = r'<='
t_POTENC    = r'^'
t_ROTIZQ    = r'<<'
t_ROTDER    = r'>>'

Lerr=[]
from CError import CError
def t_DECIMAL(t):
    r'-?\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        Lerr.append(CError('Lexico','Error en el valor float',0,t.lexer.lineno))
        t.value = 0
    return t

def t_ENTERO(t):
    r'-?\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        Lerr.append(CError('Lexico','Error en el valor entero',0,t.lexer.lineno))
        t.value = 0
    return t

def t_CADENA(t):
    r'(\".*?\")|(\'.*?\')'
    t.value = t.value[1:-1] # remuevo las comillas
    return t 

def t_LABEL(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'LABEL')    # Check for reserved words
     return t

def t_VARIABLE(t):
     r'\$(([tavs][0-9]+)|ra|sp)'
     t.type = reservadas.get(t.value.lower(),'VARIABLE')    # Check for reserved words
     return t

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'#.*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def find_column(input,token):
    last_cr = input.rfind('\n',0,token.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    Lerr.append(CError('Lexico','Caracter invalido \''+t.value[0]+'\'',0,t.lexer.lineno))
    t.lexer.skip(1)

# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()


# Asociación de operadores y precedencia
precedence = (
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO'),
    ('right','UMENOS'),
    )

# Definición de la gramática

from Expresion import *
from Instruccion import *


def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]

def p_instrucciones_lista(t) :
    'instrucciones    : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
    t[0] = [t[1]]

def p_instruccion(t) :
    '''instruccion      : imprimir_instr
                        | definicion_instr
                        | asignacion_instr
                        | mientras_instr
                        | if_instr
                        | if_else_instr'''
    t[0] = t[1]

def p_instruccion_imprimir(t) :
    'imprimir_instr     : IMPRIMIR PARIZQ expresion_cadena PARDER PTCOMA'
    t[0] =Imprimir(t[3])

def p_instruccion_definicion(t) :
    'definicion_instr   : NUMERO ID PTCOMA'
    t[0] =Definicion(t[2])

def p_asignacion_instr(t) :
    'asignacion_instr   : ID IGUAL expresion_numerica PTCOMA'
    t[0] =Asignacion(t[1], t[3])

def p_mientras_instr(t) :
    'mientras_instr     : MIENTRAS PARIZQ expresion_logica PARDER LLAVIZQ instrucciones LLAVDER'
    t[0] =Mientras(t[3], t[6])

def p_if_instr(t) :
    'if_instr           : IF PARIZQ expresion_logica PARDER LLAVIZQ instrucciones LLAVDER'
    t[0] =If(t[3], t[6])

def p_if_else_instr(t) :
    'if_else_instr      : IF PARIZQ expresion_logica PARDER LLAVIZQ instrucciones LLAVDER ELSE LLAVIZQ instrucciones LLAVDER'
    t[0] =IfElse(t[3], t[6], t[10])

def p_expresion_binaria(t):
    '''expresion_numerica : expresion_numerica MAS expresion_numerica
                        | expresion_numerica MENOS expresion_numerica
                        | expresion_numerica POR expresion_numerica
                        | expresion_numerica DIVIDIDO expresion_numerica'''
    if t[2] == '+'  : t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MAS)
    elif t[2] == '-': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MENOS)
    elif t[2] == '*': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.POR)
    elif t[2] == '/': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.DIVIDIDO)

def p_expresion_unaria(t):
    'expresion_numerica : MENOS expresion_numerica %prec UMENOS'
    t[0] = ExpresionNegativo(t[2])

def p_expresion_agrupacion(t):
    'expresion_numerica : PARIZQ expresion_numerica PARDER'
    t[0] = t[2]

def p_expresion_number(t):
    '''expresion_numerica : ENTERO
                        | DECIMAL'''
    t[0] = ExpresionNumero(t[1])

def p_expresion_id(t):
    'expresion_numerica   : ID'
    t[0] = ExpresionIdentificador(t[1])

def p_expresion_concatenacion(t) :
    'expresion_cadena     : expresion_cadena CONCAT expresion_cadena'
    t[0] = ExpresionConcatenar(t[1], t[3])

def p_expresion_cadena(t) :
    'expresion_cadena     : CADENA'
    t[0] = ExpresionDobleComilla(t[1])

def p_expresion_cadena_numerico(t) :
    'expresion_cadena     : expresion_numerica'
    t[0] = ExpresionCadenaNumerico(t[1])

def p_expresion_logica(t) :
    '''expresion_logica : expresion_numerica MAYQUE expresion_numerica
                        | expresion_numerica MENQUE expresion_numerica
                        | expresion_numerica IGUALQUE expresion_numerica
                        | expresion_numerica NIGUALQUE expresion_numerica'''
    if t[2] == '>'    : t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MAYOR_QUE)
    elif t[2] == '<'  : t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MENOR_QUE)
    elif t[2] == '==' : t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.IGUAL)
    elif t[2] == '!=' : t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.DIFERENTE)

def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()


def parse(input) :
    return parser.parse(input)