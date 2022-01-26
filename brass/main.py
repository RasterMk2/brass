from pygments import lex
from logger import init_logger
from lexer import Lexer
from bparser import Parser

import click

from pathlib import Path
import logging
import colorama
import prettyprinter

prettyprinter.install_extras(['attrs'])

from typing import Optional

colorama.init()

init_logger()

logger = logging.getLogger("brass")
logger.setLevel(logging.DEBUG)

@click.command()
@click.option('-i', '--input', 'inp', type=Path, default=None)
def main(inp: Path):
    if not(inp.exists() and inp.is_file()):
        logger.critical('Could not find input file \"{}\".'.format(inp))
        exit()
    
    lexer = Lexer()
    parser = Parser()
    
    with open(inp) as f:
        tokens = lexer.lex(f.read())
    
    #ast = parser.parse(tokens)    
    prettyprinter.pprint(tokens)
    
    # print(tokens)


if __name__ == "__main__":
    main()
