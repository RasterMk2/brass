from dataclasses import dataclass
from typing import Any

@dataclass 
class NumberNode:
    tok: Any
    
    def __repr__(self) -> str:
        return str(self.tok)
    
@dataclass
class BinOpNode:
    left_node: Any
    op_tok: Any
    right_node: Any
    
    # def __repr__(self) -> str:
    #     return f'{self.left_node}, {self.op_tok}, {self.right_node}'