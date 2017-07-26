'''Interactua con el analizador lexico para devolver un arbol de analisis sintactico.'''

import lex
from tree import ATree

TAS = {
    'programa':{
        'ID':['seq', 'END'],
        'READ':['seq', 'END'],
        'WRITE':['seq', 'END'],
        'IF':['seq', 'END'],
        'WHILE':['seq', 'END'],
        'END':['seq', 'END'],
        '}':['seq', 'END'],
        },
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
    'lectura':{
        'READ':['READ','(','CADENA', ',' ,'ID',')']
        },
    'escritura':{
        'WRITE':['WRITE','(','CADENA', ',' ,'exparit',')']
        },
    'condicional':{
        'IF':['IF','bool','THEN','bloque','else']
        },
    'else':{
        'ID':[],
        'READ':[],
        'WRITE':[],
        'IF':[],
        'ELSE':['ELSE','bloque'],
        'END':[],
        '}':[]
        },
    'ciclo':{
        'WHILE':['WHILE','bool','DO','bloque']
        },
    'bool':{
        '(':['condicion','sbool']
        },
    'sbool':{
        'OPLOG':['OPLOG','condicion','sbool'],
        'THEN':[],
        'DO':[]
        },
    'condicion':{
        '(':['(','exparit','OPREL','exparit',')'],
        'OPNOT':['OPNOT','condicion']
        },
    'bloque':{
        '{':['{','seq','}']
        },
    'exparit':{
        'ID':['term', 'sexparit'],
        '(':['term', 'sexparit'],
        'CONST':['term', 'sexparit'],
        'OPR':['term', 'sexparit'],
        },
    'sexparit':{
        'ID':[],
        'READ':[],
        'WRITE':[],
        'IF':[],
        'WHILE':[],
        'OPR':['OPR','term','sexparit'],
        'OPS':['OPS','term','sexparit'],
        'OPREL':[],
        'END':[],
        ')':[],
        '}':[]
        },
    'term':{
        'ID':['neg', 'sterm'],
        '(':['neg', 'sterm'],
        'CONST':['neg', 'sterm'],
        'OPR':['neg', 'sterm'],
        },
    'sterm':{
        'ID':[],
        'READ':[],
        'WRITE':[],
        'IF':[],
        'WHILE':[],
        'OPR':[],
        'OPS':[],
        'OP2':['OP2','neg','sterm'],
        'OPREL':[],
        'END':[],
        ')':[],
        '}':[]
        },
    'neg':{
        'ID':['pot'],
        '(':['pot'],
        'CONST':['pot'],
        'OPR':['OPR', 'pot'],
        },
    'pot':{
        'ID':['factor','spot'],
        '(':['factor','spot'],
        'CONST':['factor', 'spot'],
        },
    'spot':{
        'ID':[],
        'READ':[],
        'WRITE':[],
        'IF':[],
        'WHILE':[],
        'OPR':[],
        'OPS':[],
        'OP2':[],
        'OP3':['OP3','factor','spot'],
        'OPREL':[],
        'END':[],
        ')':[],
        '}':[]
        },
    'factor':{
        'ID':['ID'],
        '(':['(','exparit',')'],
        'CONST':['CONST']
        },
    }

def move():
    '''Le pide al analizador lexico el siguiente componente lexico.'''
    global look
    look = lex.scan()

def error(s='Syntax Error'):
    '''Eleva un error sintactico.'''
    raise Exception(lex.line,s)


stack = ['$','programa']
look = None
top = stack[-1]
move()
root = ATree(top,None)
current_node = root
#struc = []

while top != '$':
    if current_node.get_children():
        for child in current_node.get_children():
            if child.get_data() == top:
                current_node = child
    while current_node.get_data() != top:
        if current_node.get_parent() != None:
            current_node = current_node.get_parent()
            for child in current_node.get_children():
                if child.get_data() == top:
                    current_node = child
    if TAS.get(top) != None:
        prod = TAS[top].get(look.tag)
        if prod != None:
            for simb in prod:
                current_node.add_child(ATree(simb,current_node))
            stack.pop()
            stack += list(reversed(prod))
        else:
            error()
    elif top == look.tag:
        current_node.add_child(ATree(look,current_node))
        #struc.append(look)
        stack.pop()
        move()
    else:
        error()
    top = stack[-1]