from lark import Lark

with open('./calc.lark') as f:
	parser = Lark(f.read(), ambiguity='explicit')


print(parser.parse(input('> ')).pretty())