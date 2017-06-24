from lex import *
from symbols import *


class Parser:
    look = None
    top = None

    def __init__(self, l=Lex()):
        self.lex = l
        self.move()

    def move(self):
        self.look = self.lex.scan()

    def error(self, s):
        raise Exception(self.lex.line,s)

    def match(self, t):
        if self.look == t:
            self.move()
        else:
            self.error("Syntax error")

