class Tag():
    EQ, ID, WHILE, LT, GT, AND, OR, NOT, LE, GE, DO, IF, THEN, END, PERIOD, ELSE, ASSIGN, NUM, TRUE, FALSE, WRITE, READ, NE, TYPE = 'EQ','ID','WHILE','LT','GT','AND','OR','NOT','LE','GE','DO','IF','THEN','END','PERIOD','ELSE','ASSIGN','NUM','TRUE','FALSE','WRITE','READ','NE','TYPE'
#257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280
class Token():
    def __init__(self,t):
        self.tag = t

    def __str__(self):
        return str(self.tag)

class Num(Token):
    def __init__(self,v):
        super().__init__(Tag.NUM)
        self.value = v

    def __str__(self):
        return str(self.value)

class Word(Token):
    lexeme = ''
    def __init__(self,s,t):
        super().__init__(t)
        self.lexeme = s

    def __str__(self):
        return self.lexeme

_and = Word('&&', Tag.AND)
_or = Word('||', Tag.OR)
_ne = Word('!=', Tag.NOT)
_eq = Word('==', Tag.EQ)
_le = Word('<=', Tag.LE)
_ge = Word('>=', Tag.GE)
_True = Word('true', Tag.TRUE)
_False = Word('false', Tag.FALSE)

class Type(Word):
    # width = 0
    def __init__(self, s, t):
        super().__init__(s,t)

_Num = Type('num', Tag.TYPE)
_Char = Type('char', Tag.TYPE)
_Bool = Type('bool', Tag.TYPE)

class Lex():
    line = 1
    end = False
    peek = ' '
    words = {}

    def reserve(self,w):
        self.words[w.lexeme] = w

    def __init__(self,string):
        self.reserve(Word('si', Tag.IF))
        self.reserve(Word('sino', Tag.ELSE))
        self.reserve(Word('mientras', Tag.WHILE))
        self.reserve(Word('hacer', Tag.DO))
        self.reserve(_True)
        self.reserve(_False)
        # self.reserve(_Num)
        # self.reserve(_Bool)
        # self.reserve(_Char)
        self.string=string
        self.itstring=self.gen()

    def gen(self):
        '''Devuelve un caracter de una cadena a la vez'''
        for c in self.string:
            yield c

    def readch(self, c=None):
        if c:
            self.readch()
            if self.peek != c:
                return False
            self.peek = ' '
            return True
        else:
            try:
                self.peek = next(self.itstring)
            except(StopIteration):
                self.end = True
                self.peek = ''

    def scan(self):
        while self.peek == ' ' or self.peek == '\t' or self.peek == '\n':
            if self.peek == '\n':
                self.line += 1
            self.readch()

        if self.peek == '&':
            return _and if self.readch('&') else Token('&')
        elif self.peek == '|':
            return _or if self.readch('|') else Token('|')
        elif self.peek == '=':
            return _eq if self.readch('=') else Token('=')
        elif self.peek == '!':
            return _ne if self.readch('=') else Token('!')
        elif self.peek == '<':
            return _le if self.readch('=') else Token('<')
        elif self.peek == '>':
            return _ge if self.readch('=') else Token('>')

        if self.peek.isdigit():
            v = 0
            while self.peek.isdigit():
                v = 10*v + int(self.peek)
                self.readch()
            if self.peek != '.':
                return Num(v)
            d = 10.0
            self.readch()
            while self.peek.isdigit():
                v = v + int(self.peek) / d
                d *= 10.0;
                self.readch()
            return Num(v)

        if self.peek.isalpha() or self.peek == '_':
            buff = ''
            while self.peek.isdigit() or self.peek.isalpha() or self.peek == '_':
                buff += self.peek
                self.readch()
            w = self.words.get(buff)
            if w:
                return w
            w = Word(buff, Tag.ID)
            self.words[buff] = w
            return w

        tok = Token(self.peek)
        self.peek = ' '
        return tok

string = '''si 2 == 4
culo = 2'''
if __name__ == '__main__':
    l=[]
    lex = Lex(string)
    while not lex.end:
        tok = lex.scan()
        l.append(tok.tag)
    print(l)
    print(lex.line)


