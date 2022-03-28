from sly import Lexer
from compiler import AstralCompiler
from parser import AstralParser
from execute import Execute

if __name__ == '__main__':
    lexer = AstralCompiler()
    parser = AstralParser()

    print('Astral')
    env = {}

    while True:
        try:
            text = input('Astral -> ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            Execute(tree, env)