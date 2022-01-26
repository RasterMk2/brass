import attr
import unicodedata as ucd
from .tokens import NAMES

@attr.s(slots=True, frozen=True)
class BaseToken:
    pos_start: int = attr.ib(eq=False, repr=False)
    pos_end: int = attr.ib(eq=False, repr=False)

@attr.s(slots=True, frozen=True)
class Seperator(BaseToken):
    value: str = attr.ib()
    
    def __repr__(self) -> str:
        return NAMES[self.value]

@attr.s(slots=True, frozen=True)
class Operator(BaseToken):
    value: str = attr.ib()
    
    def __repr__(self) -> str:
        return NAMES[self.value]

@attr.s(slots=True, frozen=True)
class Name(BaseToken):
    name: str = attr.ib()
    
    def __repr__(self) -> str:
        return f'NAME: {self.name}'

@attr.s(slots=True, frozen=True)
class Literal(BaseToken):
    pass

@attr.s(slots=True, frozen=True)
class Number(Literal):
    pass

@attr.s(slots=True, frozen=True)
class Integer(Number):
    value: int = attr.ib()
    
    def __repr__(self) -> str:
        return str(self.value)
    
@attr.s(slots=True, frozen=True)
class Float(Number):
    value: float = attr.ib()
    
    def __repr__(self) -> str:
        return str(self.value)
    
@attr.s(slots=True, frozen=True)
class String(Literal):
    value: str = attr.ib()
    
class EOF(BaseToken):
    pass