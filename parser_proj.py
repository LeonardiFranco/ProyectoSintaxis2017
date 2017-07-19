'''Interactua con el analizador lexico para devolver un arbol de analisis sintactico.'''

import lex
#import symbols

env = lex.env

TAS = {
'programa':{
    'ID':['seq', env['END']],
    'READ':['seq', env['END']],
    'WRITE':['seq', env['END']],
    'IF':['seq', env['END']],
    'WHILE':['seq', env['END']],
    'END':['seq', env['END']],
    '}':['seq', env['END']],},
'seq':{
    'ID':['sentencia', 'seq'],
    'READ':['sentencia', 'seq'],
    'WRITE':['sentencia', 'seq'],
    'IF':['sentencia', 'seq'],
    'WHILE':['sentencia', 'seq'],
    'END':[],
    '}':[],
    },
'sentencia':{
    'ID':['asignacion'],
    'READ':['lectura'],
    'WRITE':['escritura'],
    'IF':['condicional'],
    'WHILE':['mientras']
    },
'asignacion':{
    'ID':['ID','=','exparit']
    },
}

def move():
    '''Le pide al analizador lexico el siguiente componente lexico.'''
    global look
    look = lex.scan()

def error(s='Syntax Error'):
    '''Eleva un error sintactico'''
    raise Exception(lex.line,s)

def match(token):
    global look
    if look == token:
        move()
    else:
        error("Syntax error")


stack = ['$','programa']
look = None
top = stack[-1]
move()
lu=[]
#while top != '$':
for _ in range(5):
    if TAS.get(top):
        prod = TAS[top][look.tag]
        stack.pop()
        stack += list(reversed(prod))
        print(stack)
    elif top == look.tag:
        lu.append(stack.pop())
        move()
    top = stack[-1]
print(lu)