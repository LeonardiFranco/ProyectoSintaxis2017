import lex,parser_proj,sys

string = '''a=2
fin'''#sys.argv[1]
lexer = lex.Lexer(string)
print(parser_proj.Parser(lexer).parse()[1])