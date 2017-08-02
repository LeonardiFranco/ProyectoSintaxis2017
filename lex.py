'''Toma como entrada el codigo fuente del programa y devuelve un componente lexico a la vez.'''


from collections import namedtuple

token = namedtuple('Token', ['tag', 'atrib'])
def id(tag, lexeme):
    return token(tag, lexeme)

def num(value):
    return token('CONST', value)

class Lexer(object):
    '''Clase principal del analizador lexico'''
    def __init__(self, string):
        '''Metodo constructor de la clase, establece palabras reservadas y variables de la instancia.'''
        self.line = 1
        self.end = False
        self.peek = ' '
        self.words={}
        self.itstring = iter(string)
        self.reserve(self.env['IF'])
        self.reserve(self.env['ELSE'])
        self.reserve(self.env['THEN'])
        self.reserve(self.env['WHILE'])
        self.reserve(self.env['DO'])
        self.reserve(self.env['END'])
        self.reserve(self.env['READ'])
        self.reserve(self.env['WRITE'])
        self.reserve(self.env['AND'])
        self.reserve(self.env['OR'])
        self.reserve(self.env['NOT'])

    def reserve(self,w):
        '''Reserva palabras en la tabla de simbolos'''
        self.words[w.atrib] = w

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
        'OPR' : token(tag='OPR', atrib='-'),
        'OPS' : token(tag='OPS', atrib='+'),
        'AND' : id(tag='OPLOG',lexeme='and'),
        'OR' : id(tag='OPLOG', lexeme='or'),
        'NOT' : id(tag='OPNOT', lexeme='not'),
        'NE' : token(tag='OPREL', atrib='!='),
        'EQ' : token(tag='OPREL', atrib='=='),
        'LE' : token(tag='OPREL', atrib='<='),
        'GE' : token(tag='OPREL', atrib='>='),
        'POT' : token(tag='OP3', atrib='**'),
        'RAIZ' : token(tag='OP3', atrib='//'),
        'IF' : id(tag='IF', lexeme='si'),
        'THEN' : id(tag='THEN', lexeme='entonces'),
        'ELSE' : id(tag='ELSE', lexeme='sino'),
        'WHILE' : id(tag='WHILE', lexeme='mientras'),
        'DO' : id(tag='DO', lexeme='hacer'),
        'END' : id(tag='END', lexeme='fin'),
        'READ' : id(tag='READ', lexeme='leer'),
        'WRITE' : id(tag='WRITE', lexeme='escribir'),
        '(' : token(tag='(', atrib='('),
        ')' : token(tag=')', atrib=')'),
        '{' : token(tag='{', atrib='{'),
        '}' : token(tag='}', atrib='}'),
        ',' : token(tag=',', atrib=','),
        'LT' : token(tag='OPREL', atrib='<'),
        'ASIG' : token(tag='=', atrib='='),
        'GT' : token(tag='OPREL', atrib='>'),
        'MUL' : token(tag='OP2', atrib='*'),
        'DIV' : token(tag='OP2', atrib='/'),
    }

    def error(self,s='Error lexico'):
        '''Eleva un error lexico.'''
        raise Exception(self.line,s)


    def scan(self):
        '''Metodo principal del Analizador Lexico, cada vez que se lo llama devuelve un componente lexico.'''
        #Elimina espacios
        while self.peek == ' ' or self.peek == '\t' or self.peek == '\n':
            if self.peek == '\n':
                self.line += 1
            self.readch()

        #Reconoce operadores
        if self.peek == '=':
            return self.env['EQ'] if self.readch('=') else self.env['ASIG']
        elif self.peek == '!':
            return self.env['NE'] if self.readch('=') else token(tag='!',atrib='!')
        elif self.peek == '<':
            return self.env['LE'] if self.readch('=') else self.env['LT']
        elif self.peek == '>':
            return self.env['GE'] if self.readch('=') else self.env['GT']
        elif self.peek == '*':
            return self.env['POT'] if self.readch('*') else self.env['MUL']
        elif self.peek == '/':
            return self.env['RAIZ'] if self.readch('/') else self.env['DIV']

        #Reconoce un numero
        if self.peek.isdigit():
            value = 0.0
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

        #Reconoce un identificador o palabra reservada
        if self.peek.isalpha() or self.peek == '_':
            buff = ''                                                               #Reconocio una letra o un guion bajo, establece un buffer
            while self.peek.isdigit() or self.peek.isalpha() or self.peek == '_':   #Pregunta si es un digito, una letra o un guion
                buff += self.peek                                                   #Mientras lo sea lo va poniendo en el buffer
                self.readch()                                                       #Lee el proximo caracter
            w = self.words.get(buff)                                                #Busca la palabra reconocida en la TS
            if w:                                                                   #Si esta la devuelve
                return w
            w = id(lexeme=buff, tag='ID')                                           #Si no, crea la estructura
            self.reserve(w)                                                         #Y la inserta en la TS
            return w                                                                #Luego la devuelve

        #Reconoce cadenas entre comillas
        if self.peek == '"':
            buff = ''
            self.readch()
            while self.peek != '"':
                buff += self.peek
                self.readch()
            self.readch()
            return id('CADENA',buff)

        #Reconoce caracteres individuales
        if self.peek == '+':
            self.readch()
            return self.env['OPS']
        if self.peek == '-':
            self.readch()
            return self.env['OPR']
        if self.peek in ['{','(','}',')',',']:
            car = self.peek
            self.readch()
            return self.env[car]

        return self.error() if not self.end else True


if __name__ == '__main__':
    l=[]
    lex = Lexer(open("example.pstlv").read())
    while not lex.end:
        tok = lex.scan()
        l.append(tok.tag)
    print(l)
    print(lex.line)