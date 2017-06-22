import analizador_lexico as lexer

string = "9+5-2"#raw_input("Texto a traducir: ") place holder

lex = lexer.Lexer(string)
lex.scan()
#parse = Parser(lex) #hasta que no haga el parser no lo puedo parsear hehe
#parse.program()