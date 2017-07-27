'''Traductor, toma un arbol de analisis sintactico y lo traduce a codigo de Python 3'''
import sys


class Interpreter(object):
    '''Clase principal del traductor.'''
    def __init__(self, ast):
        self.ast = ast
        self.indent = 0

    def translate(self):
        '''Metodo que traduce el arbol a codigo. Llama a preorder con el arbol de AS.'''
        _bef = sys.stdout
        with open("inter.py", "w") as f:
            sys.stdout = f
            print("from funcs import *")
            self.preorder(self.ast)
        sys.stdout = _bef

    def preorder(self,tree):
        '''Este metodo toma el arbol y lo recorre generando codigo.'''
        if tree.data == 'sentencia':
            print()
            print('    '*self.indent,end='')
        elif tree.data == '(':
            print('(',end=' ')
        elif tree.data == ')':
            print(')',end=' ')
        elif tree.data == '=':
            print('=',end=' ')
        elif tree.data == '*':
            print('*',end=' ')
        elif tree.data in ['OPR','OPS','OPREL','OP2','OP3','OPLOG','OPNOT']:
            print(tree.children[0].data.atrib,end=' ')
        elif tree.data == 'lectura':
            print(tree.children[4].children[0].data.atrib,end=' =')
        elif tree.data == 'READ':
            print("read",end='')
        elif tree.data == 'WRITE':
            print()
            print('print',end=' ')
        elif tree.data == 'CADENA':
            print('"{}",'.format(tree.children[0].data.atrib),end='')
        elif tree.data == 'ID':
            print(tree.children[0].data.atrib,end=' ')
        elif tree.data == 'CONST':
            print(tree.children[0].data.atrib,end=' ')
        elif tree.data == 'IF':
            print('if',end=' ')
        elif tree.data == 'THEN':
            print(':', end= '\n')
        elif tree.data == 'WHILE':
            print('while',end=' ')
        elif tree.data == 'DO':
            print(':', end= '\n')
        elif tree.data == '{':
            self.indent+=1
        elif tree.data == '}':
            self.indent-=1
        for child in tree.children:
            self.preorder(child)

