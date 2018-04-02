import ply.lex as lex
import ply.yacc as yacc

tokens = (
  'IF',
  'LPAREN',
  'RPAREN',
  'ELSE',
  'END',
  'NAME',
  'ASSIGN',
  'OPERATOR',
  'NUMBER',
)

t_OPERATOR    = r'\+|-|>=|=<|>|<|!='
t_LPAREN      = r'\('
t_RPAREN      = r'\)'
t_ASSIGN      = r'='
t_NUMBER      = r'[0-9]+'
t_ignore      = ' \t'

def t_IF(t):  
  r'if'
  return t
def t_ELSE(t):  
  r'else'
  return t
def t_END(t):  
  r'end'
  return t
def t_NAME(t):  
  r'[a-zA-Z_][a-zA-Z0-9_]*'
  return t

def t_newline(t):
  r'\n+'
  t.lexer.lineno += t.value.count("\n")

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)


def p_program(p):
  '''program : statement'''
def p_statement(p):
  '''statement :  assignment
               |  if'''
def p_assignment(p):
  '''assignment : NAME ASSIGN expression'''
def p_if(p):
  '''if : IF LPAREN expression RPAREN assignment END
        | IF LPAREN expression RPAREN assignment ELSE assignment END'''

def p_expression(p):
  '''expression : expression OPERATOR expression'''
  print p

def p_expression_name(p):
  '''expression : NAME'''
    
def p_expression_num(p):
  '''expression : NUMBER'''

def p_error(t):
  print("Syntax error at '%s'" % t.value)
  exit()

lexer = lex.lex()
s = "if (j>=0) j=j+10 end"

parser = yacc.yacc()
parser.parse(s,debug=1)
print "This code is grammatically correct!"

