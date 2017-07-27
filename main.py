'''Front end del interprete, recibe el codigo fuente de un programa como entrada y lo ejecuta.'''

import lex,parser_proj,interpreter,sys

try:
    source = sys.argv[1]
except(IndexError):
    source = "example.pstlv"
with open(source) as f:
    string = f.read()
lexer = lex.Lexer(string)
(AST,struc)=parser_proj.Parser(lexer).parse()

inte = interpreter.Interpreter(AST)

inte.translate()
def preorden(ast):
    print(ast)
    for child in ast.children:
        preorden(child)

with open("inter.py", "r") as f:
    prog = f.read()
    exec(prog)
# preorden(AST)