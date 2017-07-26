'''Toma como entrada el codigo fuente del programa y devuelve un componente lexico a la vez.'''


from collections import namedtuple

token = namedtuple('Token', ['tag', 'atrib'])
def id(tag, lexeme):
    return token(tag, lexeme)

def num(value):
    return token('CONST', value)

class Lexer(object):

    def __init__(self, string):
        def reserve(w):
            self.words[w.atrib] = w
        self.line = 1
        self.end = False
        self.peek = ' '
        self.words={}
        self.itstring = iter(string)
        reserve(self.env['IF'])
        reserve(self.env['ELSE'])
        reserve(self.env['THEN'])
        reserve(self.env['WHILE'])
        reserve(self.env['DO'])
        reserve(self.env['END'])
        reserve(self.env['READ'])
        reserve(self.env['WRITE'])
        reserve(self.env['AND'])
        reserve(self.env['OR'])
        reserve(self.env['NOT'])

    def readch(self,c=None):
        '''Obtiene el proximo caracter del programa de entrada,
        y si tiene un parametro de entrada compara si el proximo caracter es igual al del parametro
        y devuelve el resultado de la comparacion.'''
        if c:
            self.readch()
            if self.peek !=c:
                return False
            self.peek = ' '
            return True
        else:
            try:
                self.peek = next(self.itstring)
            except(StopIteration):
                self.end = True
                self.peek = ''

    #Environment constants
    env = {
        'AND' : id(tag='OPLOG',lexeme='and'),
        'OR' : id(tag='OPLOG', lexeme='or'),
        'NOT' : id(tag='OPNOT', lexeme='not'),
        'NE' : id(tag='OPREL', lexeme='<>'),
        'EQ' : id(tag='OPREL', lexeme='=='),
        'LE' : id(tag='OPREL', lexeme='<='),
        'GE' : id(tag='OPREL', lexeme='>='),
        'POT' : id(tag='OP3', lexeme='**'),
        'RAIZ' : id(tag='OP3', lexeme='//'),
        'IF' : id(tag='IF', lexeme='si'),
        'THEN' : id(tag='THEN', lexeme='entonces'),
        'ELSE' : id(tag='ELSE', lexeme='sino'),
        'WHILE' : id(tag='WHILE', lexeme='mientras'),
        'DO' : id(tag='DO', lexeme='hacer'),
        'END' : id(tag='END', lexeme='fin'),
        'READ' : id(tag='READ', lexeme='leer'),
        'WRITE' : id(tag='WRITE', lexeme='escribir'),
        'LPAREN' : id(tag='(', lexeme='('),
        'RPAREN' : id(tag=')', lexeme=')'),
    }

    def scan(self):

        while self.peek == ' ' or self.peek == '\t' or self.peek == '\n':
            if self.peek == '\n':
                self.line += 1
            self.readch()

        #Recognizes relational operators
        if self.peek == '=':
            return self.env['EQ'] if self.readch('=') else token(tag='=',atrib='=')
        elif self.peek == '!':
            return self.env['NE'] if self.readch('=') else token(tag='!',atrib='!')
        elif self.peek == '<':
            return self.env['LE'] if self.readch('=') else token(tag='OPREL',atrib='<')
        elif self.peek == '>':
            return self.env['GE'] if self.readch('=') else token(tag='OPREL',atrib='>')
        elif self.peek == '*':
            return self.env['POT'] if self.readch('*') else token(tag='OP2', atrib='*')
        elif self.peek == '/':
            return self.env['RAIZ'] if self.readch('/') else token(tag='OP2', atrib='/')

        #Recognizes a number
        if self.peek.isdigit():
            value = 0
            while self.peek.isdigit():
                value = 10*value + int(self.peek)
                self.readch()
            if self.peek != '.':
                return num(value=value)
            d = 10.0
            self.readch()
            while self.peek.isdigit():
                value = value + int(self.peek) / d
                d *= 10.0;
                self.readch()
            return num(value=value)

        #Recognizes an identifier or keyword
        if self.peek.isalpha() or self.peek == '_':
            buff = ''                                               #Reconocio una letra o un guion bajo, establece un buffer
            while self.peek.isdigit() or self.peek.isalpha() or self.peek == '_':  #Pregunta si es un digito, una letra o un guion
                buff += self.peek                                        #Mientras lo sea lo va poniendo en el buffer
                self.readch()                                            #Lee el proximo caracter
            w = self.words.get(buff)                                     #Busca la palabra reconocida en la TS
            if w:                                                   #Si esta la devuelve
                return w
            w = id(lexeme=buff, tag='ID')                           #Si no, crea la estructura
            self.words[buff] = w                                         #Y la inserta en la TS
            return w                                                #Luego la devuelve

        #Recognizes strings between ""
        if self.peek == '"':
            buff = ''
            self.readch()
            while self.peek != '"':
                buff += self.peek
                self.readch()
            self.readch()
            return id('CADENA',buff)

        if self.peek == '+':
            self.readch()
            return token(tag='OPS',atrib='+')
        if self.peek == '-':
            self.readch()
            return token(tag='OPR',atrib='-')
        #Recognizes other characters
        tok = token(tag=self.peek,atrib=self.peek)
        self.peek = ' '
        return tok


if __name__ == '__main__':
    l=[]
    lex = Lexer('''a=1+1
                fin''')
    while not lex.end:
        tok = lex.scan()
        l.append(tok.tag)
    print(l)
    print(lex.line)