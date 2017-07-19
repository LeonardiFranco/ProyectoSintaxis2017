'''Toma como entrada el codigo fuente del programa y devuelve un componente lexico a la vez.'''


from collections import namedtuple

line = 1
end = False
peek = ' '
words={}
string = '''a=2-1
fin'''
itstring = iter(string)
token = namedtuple('Token', ['tag', 'atrib'])

def id(tag, lexeme):
    return token(tag, lexeme)

def num(value):
    return token('CONST', value)

def reserve(w):
    global words
    words[w.atrib] = w

def readch(c=None):
    '''Obtiene el proximo caracter del programa de entrada,
    y si tiene un parametro de entrada compara si el proximo caracter es igual al del parametro
    y devuelve el resultado de la comparacion.'''
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

#Environment constants
env = {'AND' : id(tag='OPLOG',lexeme='and'),
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

reserve(env['IF'])
reserve(env['ELSE'])
reserve(env['THEN'])
reserve(env['WHILE'])
reserve(env['DO'])
reserve(env['END'])
reserve(env['READ'])
reserve(env['WRITE'])
reserve(env['AND'])
reserve(env['OR'])
reserve(env['NOT'])

def scan():
    global peek, end, words, line, env

    while peek == ' ' or peek == '\t' or peek == '\n':
        if peek == '\n':
            line += 1
        readch()

    #Recognizes relational operators
    if peek == '=':
        return env['EQ'] if readch('=') else token(tag='=',atrib='=')
    elif peek == '!':
        return env['NE'] if readch('=') else token(tag='!',atrib='!')
    elif peek == '<':
        return env['LE'] if readch('=') else token(tag='OPREL',atrib='<')
    elif peek == '>':
        return env['GE'] if readch('=') else token(tag='OPREL',atrib='>')
    elif peek == '*':
        return env['POT'] if readch('*') else token(tag='OP2', atrib='*')
    elif peek == '/':
        return env['RAIZ'] if readch('/') else token(tag='OP2', atrib='/')

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

    if peek == '+':
        readch()
        return token(tag='OPS',atrib='+')
    if peek == '-':
        readch()
        return token(tag='OPR',atrib='-')
    #Recognizes other characters
    tok = token(tag=peek,atrib=peek)
    peek = ' '
    return tok


if __name__ == '__main__':
    l=[]
    while not end:
        tok = scan()
        l.append(tok.tag)
    print(l)
    print(line)