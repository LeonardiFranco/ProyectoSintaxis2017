import lex
import symbols


TAS = {}

def move():
    '''Le pide al analizador lexico el siguiente lexema'''
    global look
    look = lex.scan()

def error(s='Syntax Error'):
    raise Exception(lex.line,s)

def match(token):
    global look
    if look == token:
        move()
    else:
        error("Syntax error")

def program():
    if (look in [lex.IF, lex.WHILE, lex.READ, lex.WRITE, lex.END]) or (look.tag in ['ID','}']):
        stack.pop()
        stack.append(lex.END)
        stack.append(seq)
    else:
        error()

def seq():
    if look in [lex.IF, lex.WHILE, lex.READ, lex.WRITE] or look.tag == 'ID':
        stack.pop()
        stack.append(seq)
        stack.append(sentencia)
    elif look == lex.END or look.tag == '}':
        stack.pop()
    else:
        error()

def sentencia():
    if look.tag == 'ID':
        stack.pop()
        stack.append(asignacion)
    elif look == lex.READ:
        stack.pop()
        stack.append(lectura)
    elif look == lex.WRITE:
        stack.pop()
        stack.append(escritura)
    elif look == lex.IF:
        stack.pop()
        stack.append(condicional)
    elif look == lex.WHILE:
        stack.pop()
        stack.append(ciclo)
    else:
        error()

def asignacion():
    if look.tag == 'ID':
        stack.pop()
        stack.append(exparit)
        stack.append(lex.token('=','='))
        stack.append(look)
    else:
        error()

def identificador():
    if look.tag == 'ID':
        stack.pop()
        stack.append(look)
    else:
        error()

def lectura():
    if look == lex.READ:
        stack.pop()
        stack.append(lex.RPAREN)
        stack.append(identificador)
        stack.append(lex.token(',',','))
        stack.append(cadena)
        stack.append(lex.LPAREN)
        stack.append(lex.READ)
    else:
        error()

def cadena():
    if look.tag == 'CADENA':
        stack.pop()
        stack.append(look)
    else:
        error()

def escritura():
    if look == lex.WRITE:
        stack.pop()
        stack.append(lex.RPAREN)
        stack.append(exparit)
        stack.append(lex.token(',',','))
        stack.append(cadena)
        stack.append(lex.LPAREN)
        stack.append(lex.WRITE)
    else:
        error()

def condicional():
    if look == lex.IF:
        stack.pop()
        stack.append(Else)
        stack.append(bloque)
        stack.append(lex.THEN)
        stack.append(Bool)
        stack.append(lex.IF)
    else:
        error()

def Else():
    if look.tag in ['ID', '}'] or look in [lex.READ, lex.WRITE, lex.IF, lex.WHILE, lex.END]:
        stack.pop()
    elif look == lex.ELSE:
        stack.pop()
        stack.append(bloque)
        stack.append(look)
    else:
        error()

def bloque():
    if look.tag == '{':
        stack.pop()
        stack.append(lex.token('}','}'))
        stack.append(seq)
        stack.append(lex.token('{','{'))
    else:
        error()

def Bool():
    if look in [lex.LPAREN, lex.NOT]:
        stack.pop()
        stack.append(sBool)
        stack.append(condicion)
    else:
        error()

def sBool():
    if look in [lex.DO, lex.THEN]:
        stack.pop()
    elif look in [lex.AND, lex.OR]:
        stack.pop()
        stack.append(sBool)
        stack.append(condicion)
        stack.append(oplog)
    else:
        error()

def oplog():
    if look.atrib == 'or':
        stack.pop()
        stack.append(lex.OR)
    elif look.atrib == 'and':
        stack.pop()
        stack.append(lex.AND)
    else:
        error()

def condicion():
    if look == lex.LPAREN:
        stack.pop()
        stack.append(lex.RPAREN)
        stack.append(exparit)
        stack.append(oprel)
        stack.append(exparit)
        stack.append(lex.LPAREN)
    elif look == lex.NOT:
        stack.pop()
        stack.append(condicion)
        stack.append(lex.NOT)
    else:
        error()

def ciclo():
    if look == lex.WHILE:
        stack.pop()
        stack.append(bloque)
        stack.append(lex.DO)
        stack.append(Bool)
        stack.append(lex.WHILE)
    else:
        error()

def exparit():
    if look.tag in ['ID','CONST','-'] or look == lex.LPAREN:
        stack.pop()
        stack.append(sexparit)
        stack.append(term)
    else:
        error()

def sexparit():
    if look.tag in ['+','-']:
        stack.pop()
        stack.append(sexparit)
        stack.append(term)
        stack.append(op1)
    elif look.tag in ['ID', 'OPREL', '}'] or look in [lex.READ, lex.WRITE, lex.IF, lex.WHILE, lex.END, lex.RPAREN]:
        stack.pop()
    else:
        error()

def term():
    if look.tag in ['ID','CONST','-'] or look == lex.LPAREN:
        stack.pop()
        stack.append(sterm)
        stack.append(neg)
    else:
        error()

def sterm():
    if look.tag == 'OP2':
        stack.pop()
        stack.append(sterm)
        stack.append(neg)
        stack.append(op2)
    elif look.tag in ['ID', 'OPREL', '}','+','-'] or look in [lex.READ, lex.WRITE, lex.IF, lex.WHILE, lex.END, lex.RPAREN]:
        stack.pop()
    else:
        error()

def neg():
    if look.tag in ['ID', '(', 'CONST']:
        stack.pop()
        stack.append(pot)
    elif look.tag == '-':
        stack.pop()
        stack.append(pot)
        stack.append(lex.token('-','-'))
    else:
        error()

def pot():
    if look.tag in ['ID', '(', 'CONST']:
        stack.pop()
        stack.append(spot)
        stack.append(factor)
    else:
        error()

def spot():
    if look.tag == 'OP3':
        stack.pop()
        stack.append(spot)
        stack.append(factor)
        stack.append(op3)
    elif look.tag in ['ID', 'OPREL', '}','+','-', 'OP2'] or look in [lex.READ, lex.WRITE, lex.IF, lex.WHILE, lex.END, lex.RPAREN]:
        stack.pop()
    else:
        error()

def op1():
    if look.atrib == '+':
        stack.pop()
        stack.append(lex.token('OP1','+'))
    elif look.atrib == '-':
        stack.pop()
        stack.append(lex.token('OP1', '-'))
    else:
        error()

def op2():
    if look.atrib == '*':
        stack.pop()
        stack.append(lex.token('OP2','*'))
    elif look.atrib == '/':
        stack.pop()
        stack.append(lex.token('OP2', '/'))
    else:
        error()

def op3():
    if look.atrib == '**':
        stack.pop()
        stack.append(lex.token('OP3','**'))
    elif look.atrib == '//':
        stack.pop()
        stack.append(lex.token('OP3', '//'))
    else:
        error()

def factor():
    if look.tag == 'ID':
        stack.pop()
        stack.append(look)
    elif look == lex.LPAREN:
        stack.pop()
        stack.append(lex.RPAREN)
        stack.append(exparit)
        stack.append(lex.LPAREN)
    elif look.tag == 'CONST':
        stack.pop()
        stack.append(look)
    else:
        error()

def oprel():
    if look.atrib == '<':
        stack.pop()
        stack.append(lex.token('<','<'))
    elif look.atrib == '>':
        stack.pop()
        stack.append(lex.token('>','>'))
    elif look.atrib == '==':
        stack.pop()
        stack.append(lex.EQ)
    elif look.atrib == '>=':
        stack.pop()
        stack.append(lex.GE)
    elif look.atrib == '<=':
        stack.pop()
        stack.append(lex.LE)
    else:
        error()


stack = ['$',program]
look = None
top = stack[-1]
move()
lu=[]
while top != '$':
    if callable(top):
        top()
    elif top.atrib == look.atrib:
        lu.append(stack.pop())
        move()
    top = stack[-1]
print(lu)