from .types import *
from .tokens import *

import logging

logger = logging.getLogger('brass')

def index_to_coordinates(s, index):
    """Returns (line_number, col) of `index` in `s`."""
    if not len(s):
        return 1, 1
    sp = s[:index+1].splitlines(keepends=True)
    return len(sp), len(sp[-1])

class Lexer:
    def __init__(self):
        self.text = ''
        self.pos = -1
        self.current_char = None
        
    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
        
    def lex(self, code: str):
        self.text = code
        
        self.pos = -1
        self.current_char = None
        
        self.advance()
        
        tokens = []
        
        while self.current_char != None:
            if self.current_char in ' \t\n':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == '"':
                tokens.append(self.make_string())
            elif self.current_char in NAME_CHARS_START:
                tokens.append(self.make_name())    
            
            elif self.current_char in operators:
                tokens.append(Operator(self.pos, self.pos, self.current_char)) 
                self.advance()
                
            elif self.current_char in seperators:
                tokens.append(Seperator(self.pos, self.pos, self.current_char))
                self.advance()  
            else:
                char = self.current_char
                coords = index_to_coordinates(self.text, self.pos)
                logger.critical(f'Illegal character "{char}" on Ln {coords[0]}, Col {coords[1]}.')
                exit()
                
        tokens.append(EOF(self.pos, self.pos))
            
        return tokens
            
    def make_number(self):
        num_str = ''
        dot_count = 0
        pos_start = 0
        
        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else: 
                num_str += self.current_char
            self.advance()
                
        if dot_count:
            return Float(pos_start, self.pos, float(num_str))
        else:
            return Integer(pos_start, self.pos, int(num_str))
        
    def make_string(self):
        temp = ''
        pos_start = 0
        
        self.advance()
        
        while self.current_char != None and self.current_char != '"':
            temp += self.current_char
            self.advance()
            
        self.advance()
        return String(pos_start, self.pos, temp)
    
    def make_name(self):
        temp = ''
        pos_start = 0
        
        while self.current_char != None and self.current_char in NAME_CHARS:
            temp += self.current_char
            self.advance()
            
        return Name(pos_start, self.pos, temp)