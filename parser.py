from sly import Parser
from compiler import AstralCompiler
class AstralParser(Parser):
    tokens = AstralCompiler.tokens

    precedence = (('left', '+', '-'), 
        ('left', '*', '/'), 
        ('right', 'UMINUS'),
    )

    def __init__(self):
        self.env =  {  }

    @_('')
    def statement(self, y):
        pass

    @_('var_assign')
    def statement(self, y):
        return y.var_assign
    
    @_('NAME "=" expr')
    def var_assign(self, y):
        return ('var_assign', y.NAME, y.expr)

    @_('NAME "=" STRING')
    def var_assign(self, y):
        return ('var_assign', y.NAME, y.STRING)

    @_('expr')
    def statement(self, y):
        return (y.expr)
  
    @_('expr "+" expr')
    def expr(self, y):
        return ('add', y.expr0, y.expr1)
  
    @_('expr "-" expr')
    def expr(self, y):
        return ('sub', y.expr0, y.expr1)
  
    @_('expr "*" expr')
    def expr(self, y):
        return ('mul', y.expr0, y.expr1)

    @_('expr "/" expr')
    def expr(self, y):
        return ('div', y.expr0, y.expr1)
  
    @_('"-" expr %prec UMINUS')
    def expr(self, y):
        return y.expr
  
    @_('NAME')
    def expr(self, y):
        return ('var', y.NAME)
  
    @_('NUMBER')
    def expr(self, y):
        return ('num', y.NUMBER)