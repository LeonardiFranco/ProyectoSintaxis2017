from collections import namedtuple


token = namedtuple('Token', ['tag', 'atrib'])

def id(tag, lexeme):
    return token(tag, lexeme)

def num(value):
    return token('CONST', value)

def reserve(w):
    global words
    words[w.atrib] = w


def readch(c=None):
    global peek, end, itstring
    if c:
        readch()
        if peek !=c:
            return False
        peek = ' '
        return True
    else:
        try:
            peek = next(itstring)
        except(StopIteration):
            end = True
            peek = ''

AND = id(tag='OPLOG',lexeme='and')
OR = id(tag='OPLOG', lexeme='or')
NOT = id(tag='OPLOG', lexeme='not')
NE = id(tag='OPREL', lexeme='<>')
EQ = id(tag='OPREL', lexeme='==')
LE = id(tag='OPREL', lexeme='<=')
GE = id(tag='OPREL', lexeme='>=')
POT = id(tag='OP3', lexeme='**')
RAIZ = id(tag='OP3', lexeme='//')
IF = id(tag='IF', lexeme='si')
THEN = id(tag='THEN', lexeme='entonces')
ELSE = id(tag='ELSE', lexeme='sino')
WHILE = id(tag='WHILE', lexeme='mientras')
DO = id(tag='DO', lexeme='hacer')
END = id(tag='END', lexeme='fin')
READ = id(tag='READ', lexeme='leer')
WRITE = id(tag='WRITE', lexeme='escribir')
LPAREN = id(tag='(', lexeme='(')
RPAREN = id(tag=')', lexeme=')')

def scan():
    global peek, end, words, line

    #Define constants, and reserve words
    AND = id(tag='OPLOG',lexeme='and')
    OR = id(tag='OPLOG', lexeme='or')
    NOT = id(tag='OPLOG', lexeme='not')
    NE = id(tag='OPREL', lexeme='<>')
    EQ = id(tag='OPREL', lexeme='==')
    LE = id(tag='OPREL', lexeme='<=')
    GE = id(tag='OPREL', lexeme='>=')
    POT = id(tag='OP3', lexeme='**')
    RAIZ = id(tag='OP3', lexeme='//')
    IF = id(tag='IF', lexeme='si')
    THEN = id(tag='THEN', lexeme='entonces')
    ELSE = id(tag='ELSE', lexeme='sino')
    WHILE = id(tag='WHILE', lexeme='mientras')
    DO = id(tag='DO', lexeme='hacer')
    END = id(tag='END', lexeme='fin')
    READ = id(tag='READ', lexeme='leer')
    WRITE = id(tag='WRITE', lexeme='escribir')
    reserve(IF)
    reserve(ELSE)
    reserve(THEN)
    reserve(WHILE)
    reserve(DO)
    reserve(END)
    reserve(READ)
    reserve(WRITE)
    reserve(AND)
    reserve(OR)
    reserve(NOT)


    while peek == ' ' or peek == '\t' or peek == '\n':
        if peek == '\n':
            line += 1
        readch()

    #Recognizes relational operators
    if peek == '=':
        return EQ if readch('=') else token(tag='=',atrib='=')
    elif peek == '!':
        return NE if readch('=') else token(tag='!',atrib='!')
    elif peek == '<':
        return LE if readch('=') else token(tag='OPREL',atrib='<')
    elif peek == '>':
        return GE if readch('=') else token(tag='OPREL',atrib='>')
    elif peek == '*':
        return POT if readch('*') else token(tag='OP2', atrib='*')
    elif peek == '/':
        return RAIZ if readch('/') else token(tag='OP2', atrib='/')

    #Recognizes a number
    if peek.isdigit():
        value = 0
        while peek.isdigit():
            value = 10*value + int(peek)
            readch()
        if peek != '.':
            return num(value=value)
        d = 10.0
        readch()
        while peek.isdigit():
            value = value + int(peek) / d
            d *= 10.0;
            readch()
        return num(value=value)

    #Recognizes an identifier or keyword
    if peek.isalpha() or peek == '_':
        buff = ''                                               #Reconocio una letra o un guion bajo, establece un buffer
        while peek.isdigit() or peek.isalpha() or peek == '_':  #Pregunta si es un digito, una letra o un guion
            buff += peek                                        #Mientras lo sea lo va poniendo en el buffer
            readch()                                            #Lee el proximo caracter
        w = words.get(buff)                                     #Busca la palabra reconocida en la TS
        if w:                                                   #Si esta la devuelve
            return w
        w = id(lexeme=buff, tag='ID')                           #Si no, crea la estructura
        words[buff] = w                                         #Y la inserta en la TS
        return w                                                #Luego la devuelve

    #Recognizes strings between ""
    if peek == '"':
        buff = ''
        readch()
        while peek != '"':
            buff += peek
            readch()
        readch()
        return id('CADENA',buff)

    #Recognizes other characters
    tok = token(tag=peek,atrib=peek)
    peek = ' '
    return tok


line = 1
end = False
peek = ' '
words = {}
string = '''a=1
fin'''
itstring = iter(string)

if __name__ == '__main__':
    l=[]
    while not end:
        tok = scan()
        l.append(tok.tag)
    print(l)
    print(line)