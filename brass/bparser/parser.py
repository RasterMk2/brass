from .nodes import BinOpNode, NumberNode
from lexer import Number, Operator, EOF


class AST:
    def __init__(self):
        self.error = None
        self.node = None
        
    def register(self, res):
        if isinstance(res, AST):
            if False:
                pass
    
    def success(self):
        pass
    
    def failure(self):
        pass

class Parser:
    def __init__(self):
        self.tokens = []
        self.tok_idx = -1
        
    def advance(self):
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]
        return self.current_tok
    
    def parse(self, tokens):
        self.tokens = tokens
        self.tok_idx = -1
        self.advance()
        res = self.expr()
        if isinstance(self.current_tok, EOF):
            pass
        return res
    
    def factor(self):
        tok = self.current_tok
        
        if isinstance(tok, Number):
            self.advance()   
            return NumberNode(tok)
        
    def term(self):
        return self.bin_op(self.factor, (Operator(0, 0, '*'), Operator(0, 0, '/')))
    
    def expr(self):
        return self.bin_op(self.term, (Operator(0, 0, '+'), Operator(0, 0, '-')))
    
    def bin_op(self, func, ops):
        left = func()
        
        while self.current_tok in ops:
            op_tok = self.current_tok
            self.advance()
            right = func()
            left = BinOpNode(left, op_tok, right)
            
        return left