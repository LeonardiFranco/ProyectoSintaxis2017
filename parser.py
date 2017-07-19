import lex
import symbols


TAS = {}

def move():
    global look
    look = lex_e.scan()

def error(s='Syntax Error'):
    raise Exception(lex_e.line,s)

def match(token):
    global look
    if look == token:
        move()
    else:
        error("Syntax error")

def program():
    if (look in [lex_e.IF, lex_e.WHILE, lex_e.READ, lex_e.WRITE, lex_e.END]) or (look.tag in ['ID','}']):
        stack.pop()
        stack.append(lex_e.END)
        stack.append(seq)
    else:
        error()

def seq():
    if look in [lex_e.IF, lex_e.WHILE, lex_e.READ, lex_e.WRITE] or look.tag == 'ID':
        stack.pop()
        stack.append(seq)
        stack.append(sentencia)
    elif look == lex_e.END or look.tag == '}':
        stack.pop()
    else:
        error()

def sentencia():
    if look.tag == 'ID':
        stack.pop()
        stack.append(asignacion)
    elif look == lex_e.READ:
        stack.pop()
        stack.append(lectura)
    elif look == lex_e.WRITE:
        stack.pop()
        stack.append(escritura)
    elif look == lex_e.IF:
        stack.pop()
        stack.append(condicional)
    elif look == lex_e.WHILE:
        stack.pop()
        stack.append(ciclo)
    else:
        error()

def asignacion():
    if look.tag == 'ID':
        stack.pop()
        stack.append(exparit)
        stack.append(lex_e.token('=','='))
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
    if look == lex_e.READ:
        stack.pop()
        stack.append(lex_e.RPAREN)
        stack.append(identificador)
        stack.append(lex_e.token(',',','))
        stack.append(cadena)
        stack.append(lex_e.LPAREN)
        stack.append(lex_e.READ)
    else:
        error()

def cadena():
    if look.tag == 'CADENA':
        stack.pop()
        stack.append(look)
    else:
        error()

def escritura():
    if look == lex_e.WRITE:
        stack.pop()
        stack.append(lex_e.RPAREN)
        stack.append(exparit)
        stack.append(lex_e.token(',',','))
        stack.append(cadena)
        stack.append(lex_e.LPAREN)
        stack.append(lex_e.WRITE)
    else:
        error()

def condicional():
    if look == lex_e.IF:
        stack.pop()
        stack.append(Else)
        stack.append(bloque)
        stack.append(lex_e.THEN)
        stack.append(Bool)
        stack.append(lex_e.IF)
    else:
        error()

def Else():
    if look.tag in ['ID', '}'] or look in [lex_e.READ, lex_e.WRITE, lex_e.IF, lex_e.WHILE, lex_e.END]:
        stack.pop()
    elif look == lex_e.ELSE:
        stack.pop()
        stack.append(bloque)
        stack.append(look)
    else:
        error()

def bloque():
    if look.tag == '{':
        stack.pop()
        stack.append(lex_e.token('}','}'))
        stack.append(seq)
        stack.append(lex_e.token('{','{'))
    else:
        error()

def Bool():
    if look in [lex_e.LPAREN, lex_e.NOT]:
        stack.pop()
        stack.append(sBool)
        stack.append(condicion)
    else:
        error()

def sBool():
    if look in [lex_e.DO, lex_e.THEN]:
        stack.pop()
    elif look in [lex_e.AND, lex_e.OR]:
        stack.pop()
        stack.append(sBool)
        stack.append(condicion)
        stack.append(oplog)
    else:
        error()

def oplog():
    if look.atrib == 'or':
        stack.pop()
        stack.append(lex_e.OR)
    elif look.atrib == 'and':
        stack.pop()
        stack.append(lex_e.AND)
    else:
        error()

def condicion():
    if look == lex_e.LPAREN:
        stack.pop()
        stack.append(lex_e.RPAREN)
        stack.append(exparit)
        stack.append(oprel)
        stack.append(exparit)
        stack.append(lex_e.LPAREN)
    elif look == lex_e.NOT:
        stack.pop()
        stack.append(condicion)
        stack.append(lex_e.NOT)
    else:
        error()

def ciclo():
    if look == lex_e.WHILE:
        stack.pop()
        stack.append(bloque)
        stack.append(lex_e.DO)
        stack.append(Bool)
        stack.append(lex_e.WHILE)
    else:
        error()

def exparit():
    if look.tag in ['ID','CONST','-'] or look == lex_e.LPAREN:
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
    elif look.tag in ['ID', 'OPREL', '}'] or look in [lex_e.READ, lex_e.WRITE, lex_e.IF, lex_e.WHILE, lex_e.END, lex_e.RPAREN]:
        stack.pop()
    else:
        error()

def term():
    if look.tag in ['ID','CONST','-'] or look == lex_e.LPAREN:
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
    elif look.tag in ['ID', 'OPREL', '}','+','-'] or look in [lex_e.READ, lex_e.WRITE, lex_e.IF, lex_e.WHILE, lex_e.END, lex_e.RPAREN]:
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
        stack.append(lex_e.token('-','-'))
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
    elif look.tag in ['ID', 'OPREL', '}','+','-', 'OP2'] or look in [lex_e.READ, lex_e.WRITE, lex_e.IF, lex_e.WHILE, lex_e.END, lex_e.RPAREN]:
        stack.pop()
    else:
        error()

def op1():
    if look.atrib == '+':
        stack.pop()
        stack.append(lex_e.token('OP1','+'))
    elif look.atrib == '-':
        stack.pop()
        stack.append(lex_e.token('OP1', '-'))
    else:
        error()

def op2():
    if look.atrib == '*':
        stack.pop()
        stack.append(lex_e.token('OP2','*'))
    elif look.atrib == '/':
        stack.pop()
        stack.append(lex_e.token('OP2', '/'))
    else:
        error()

def op3():
    if look.atrib == '**':
        stack.pop()
        stack.append(lex_e.token('OP3','**'))
    elif look.atrib == '//':
        stack.pop()
        stack.append(lex_e.token('OP3', '//'))
    else:
        error()

def factor():
    if look.tag == 'ID':
        stack.pop()
        stack.append(look)
    elif look == lex_e.LPAREN:
        stack.pop()
        stack.append(lex_e.RPAREN)
        stack.append(exparit)
        stack.append(lex_e.LPAREN)
    elif look.tag == 'CONST':
        stack.pop()
        stack.append(look)
    else:
        error()

def oprel():
    if look.atrib == '<':
        stack.pop()
        stack.append(lex_e.token('<','<'))
    elif look.atrib == '>':
        stack.pop()
        stack.append(lex_e.token('>','>'))
    elif look.atrib == '==':
        stack.pop()
        stack.append(lex_e.EQ)
    elif look.atrib == '>=':
        stack.pop()
        stack.append(lex_e.GE)
    elif look.atrib == '<=':
        stack.pop()
        stack.append(lex_e.LE)
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