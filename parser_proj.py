'''Analizador Sintactico'''

import lex
import symbols


TAS = {}

def move():
    '''Le pide al analizador lexico el siguiente componente lexico.'''
    global look
    look = lex.scan()

def error(s='Syntax Error'):
    raise Exception(lex.line,s)

def match(token):
    global look
    if look == token:
        move()
    else:
        error("Syntax error")


stack = ['$']#,program]
look = None
top = stack[-1]
move()
lu=[]
while top != '$':
    if callable(top):
        top()
    elif top.atrib == look.atrib:
        lu.append(stack.pop())
        move()
    top = stack[-1]
print(lu)