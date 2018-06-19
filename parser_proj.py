'''Interactua con el analizador lexico para devolver un arbol de analisis sintactico.'''

from tree import ATree
from tas import TAS


class Parser(object):
    '''Clase principal del Analizador Sintactico.'''
    def __init__(self,lexer):
        '''Metodo constructor del AS'''
        self.lexer = lexer
        self.root = ATree('programa',None)
        self.stack = ['$']
        self.stack.append(self.root)
        self.top = self.stack[-1]
        self.move()

    def move(self):
        '''Le pide al analizador lexico el siguiente componente lexico.'''
        self.look = self.lexer.scan()

    def error(self,s='Syntax Error'):
        '''Eleva un error sintactico.'''
        raise Exception(self.lexer.line,s)

    def parse(self):
        '''Metodo principal del Analizador Sintactico, construye el arbol de analisis sintactico y lo devuelve.'''
        while self.top != '$':
            if TAS.get(self.top.data) != None:
                prod = TAS[self.top.data].get(self.look.tag)
                if prod != None:
                    self.stack.pop()
                    simb = [ATree(p,self.top) for p in prod]
                    self.stack += list(reversed(simb))
                    self.top.children += simb
                else:
                    self.error()
            elif self.top.data == self.look.tag:
                self.top.add_child(ATree(self.look,self.top))
                self.stack.pop()
                self.move()
            else:
                self.error()
            self.top = self.stack[-1]
        return (self.root)

if __name__ == '__main__':
    import lex
    print(Parser(lex.Lexer(open("example.pstlv").read())).parse())