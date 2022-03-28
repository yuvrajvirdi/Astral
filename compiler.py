from sly import Lexer
class AstralCompiler(Lexer):
    tokens = { NAME, NUMBER, STRING }
    ignore = '\t '
    literals = { '=', '+', '-', '*', '/', '(', ')', ',', ';' }

    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'

    # number token
    @_(r'\d+')
    def NUMBER(self, x):
        x.value = int(x.value)
        return x

    # comment token
    @_(r'//.*')
    def COMMENT(self, x):
        pass

    # newline token
    @_(r'\n+')
    def newline(self, x):
        self.lineno = x.value.count('\n')


    