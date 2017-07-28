'''Front end del interprete, recibe el codigo fuente de un programa como entrada y lo ejecuta.'''

import lex,parser_proj,interpreter,sys

try:
    source = sys.argv[1]
except(IndexError):
    source = "suma.pstlv"
with open(source) as f:
    string = f.read()
lexer = lex.Lexer(string)
AST=parser_proj.Parser(lexer).parse()

inte = interpreter.Interpreter(AST)

inte.inter()
# preorden(AST)