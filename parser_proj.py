'''Interactua con el analizador lexico para devolver un arbol de analisis sintactico.'''

from tree import ATree
from tas import TAS


class Parser(object):
    '''Clase principal del Analizador Sintactico.'''
    def __init__(self,lexer):
        '''Metodo constructor del AS'''
        self.lexer = lexer
        self.stack = ['$','programa']
        self.look = None
        self.top = self.stack[-1]
        self.move()
        self.root = ATree(self.top,None)
        self.current_node = self.root
        self.struc = []

    def move(self):
        '''Le pide al analizador lexico el siguiente componente lexico.'''
        self.look = self.lexer.scan()

    def error(self,s='Syntax Error'):
        '''Eleva un error sintactico.'''
        raise Exception(self.lexer.line,s)

    def parse(self):
        '''Metodo principal del Analizador Sintactico, construye el arbol de analisis sintactico y lo devuelve.'''
        while self.top != '$':
            #print(self.stack,self.current_node,self.top, sep= ' // ')
            if self.current_node.children:
                for child in self.current_node.children:
                    if child.data == self.top:
                        self.current_node = child
            while self.current_node.data != self.top:
                if self.current_node.parent != None:
                    self.current_node = self.current_node.parent
                    for child in self.current_node.children:
                        if child.data == self.top:
                            self.current_node = child
            if TAS.get(self.top) != None:
                prod = TAS[self.top].get(self.look.tag)
                if prod != None:
                    for simb in prod:
                        self.current_node.add_child(ATree(simb,self.current_node))
                    self.stack.pop()
                    self.stack += list(reversed(prod))
                else:
                    self.error()
            elif self.top == self.look.tag:
                self.current_node.add_child(ATree(self.look,self.current_node))
                self.struc.append(self.look)
                self.stack.pop()
                self.move()
            else:
                self.error()
            self.top = self.stack[-1]
        return (self.root,self.struc)

# import lex
# print(Parser(lex.Lexer(open("example.pstlv").read())).parse()[1])