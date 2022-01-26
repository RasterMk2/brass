from lark import Lark

with open('./grammar.lark') as f:
	parser = Lark(f.read(), start='script', lexer='standard', parser='lalr')

with open('./examples/math.brs') as f:
	print(parser.parse(f.read()).pretty())