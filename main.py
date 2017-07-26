import lex,parser,sys

source = sys.argv[1]
with open(source) as f:
    string = f.read()
lexer = lex.Lexer(string)
(AST,struc)=parser.Parser(lexer).parse()
#print(AST)
print(struc)
# l=[]
# while not lexer.end:
#     tok = lexer.scan()
#     l.append(tok)
# print(l)
# print(lexer.line)
