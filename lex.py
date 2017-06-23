class Tag():
    EQ, ID, WHILE, LT, GT, AND, OR, NOT, LE, GE, DO, IF, THEN, END, PERIOD, ELSE, ASSIGN, NUM, TRUE, FALSE, WRITE, READ, NE, TYPE = 'EQ','ID','WHILE','LT','GT','AND','OR','NOT','LE','GE','DO','IF','THEN','END','PERIOD','ELSE','ASSIGN','NUM','TRUE','FALSE','WRITE','READ','NE','TYPE'
                                                                                                                                    #257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280

class Token:
    '''Single tokens not defined in the grammar'''
    def __init__(self,t, **kwds):
        self.tag = t
        super().__init__(**kwds)

    def __str__(self):
        return str(self.tag)

class Num(Token):
    '''Constant'''
    def __init__(self,v,**kwds):
        super().__init__(Tag.NUM,**kwds)
        self.value = v

    def __str__(self):
        return str(self.value)

class Word(Token):
    '''Any kind of keyword, identifier or operator'''
    def __init__(self,s,t,**kwds):
        super().__init__(t,**kwds)
        self.lexeme = s

    def __str__(self):
        return self.lexeme

#Define environment constants
_and = Word(s='&&', t=Tag.AND)
_or = Word(s='||', t=Tag.OR)
_ne = Word(s='!=', t=Tag.NOT)
_eq = Word(s='==', t=Tag.EQ)
_le = Word(s='<=', t=Tag.LE)
_ge = Word(s='>=', t=Tag.GE)
_True = Word(s='true', t=Tag.TRUE)
_False = Word(s='false', t=Tag.FALSE)


#Main class
class Lex():
    line = 1
    end = False
    peek = ' '
    words = {}

    def reserve(self,w):
        self.words[w.lexeme] = w

    def __init__(self,string):
        '''Reserves keywords and sets up variables'''
        self.reserve(Word(s='si', t=Tag.IF))
        self.reserve(Word(s='sino', t=Tag.ELSE))
        self.reserve(Word(s='mientras', t=Tag.WHILE))
        self.reserve(Word(s='hacer', t=Tag.DO))
        self.reserve(_True)
        self.reserve(_False)
        self.string=string
        self.itstring=self.gen()

    def gen(self):
        '''Returns a character of the input string at a time'''
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
        '''Scans the string and returns the first token it finds'''

        #Recognizes and strips spaces, tabs or new lines
        while self.peek == ' ' or self.peek == '\t' or self.peek == '\n':
            if self.peek == '\n':
                self.line += 1
            self.readch()
        #Recognizes relational or logical operators
        if self.peek == '&':
            return _and if self.readch('&') else Token('&')
        elif self.peek == '|':
            return _or if self.readch('|') else Token(t='|')
        elif self.peek == '=':
            return _eq if self.readch('=') else Token(t='=')
        elif self.peek == '!':
            return _ne if self.readch('=') else Token(t='!')
        elif self.peek == '<':
            return _le if self.readch('=') else Token(t='<')
        elif self.peek == '>':
            return _ge if self.readch('=') else Token(t='>')
        #Recognizes a number
        if self.peek.isdigit():
            value = 0
            while self.peek.isdigit():
                value = 10*value + int(self.peek)
                self.readch()
            if self.peek != '.':
                return Num(v=value)
            d = 10.0
            self.readch()
            while self.peek.isdigit():
                value = value + int(self.peek) / d
                d *= 10.0;
                self.readch()
            return Num(v=value)
        #Recognizes an identifier or keyword
        if self.peek.isalpha() or self.peek == '_':
            buff = ''
            while self.peek.isdigit() or self.peek.isalpha() or self.peek == '_':
                buff += self.peek
                self.readch()
            w = self.words.get(buff)
            if w:
                return w
            w = Word(s=buff, t=Tag.ID)
            self.words[buff] = w
            return w
        #Recognizes the period by itself
        if self.peek == ".":
            self.readch()
            return Word(s='.',t=Tag.PERIOD)

        tok = Token(t=self.peek)
        self.peek = ' '
        return tok

string = '''si 2 == 4
culo = a.'''
if __name__ == '__main__':
    l=[]
    lex = Lex(string)
    while not lex.end:
        tok = lex.scan()
        l.append(tok.tag)
    print(l)
    print(lex.line)
    print(lex.words['si'])


