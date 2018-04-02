import ply.lex as lex
import ply.yacc as yacc
import re
start = 'exp'

tokens = (
        
        'NEWLINE',
        'TAB',
        'SPACE',
        'ARRAYEACH',
        'FOR',
        'IN',
        'DOTS',
        'DO',
        'DEF',
        'RETURN',
        'LOOPVAR',
        'PUTS',
        'CASE',
        'WHEN',
        'INPUT',
        'END',
        'ELSE',
        'STRING',
        'COMMA',
        'IDENTIFIER',
        'NUMBER',
        'EQUAL',
        'OPERATOR',
        'LEFTBRACKET',
        'RIGHTBRACKET',
)

literals = '()-'

def t_DOTS(t):
        r'\.\.'
        return t
        

t_ignore = ' \t\v\r' # whitespace

def t_DEF(t):
        r'def'
        return t

def t_RETURN(t):
        r'return'
        return t

def t_INPUT(t):
        r'gets.chomp'
        return t
def t_CASE(t):
        r'case'
        return t

def t_WHEN(t):
        r'when'
        return t

def t_NEWLINE(t):
        r'\n'
        t.lexer.lineno += 1
 
def t_TAB(t):
        r'\s\s\s\s'
        return t

def t_SPACE(t):
        r'\s'
        return t
        
        
def t_ARRAYEACH(t):
        r'[A-Za-z][A-Za-z_]*\.each'
        return t
        
def t_FOR(t):
        r'for'
        return t
def t_IN(t):
        r'in'
        return t

def t_DO(t):
        r'do'
        return t
def t_LOOPVAR(t):
        r'\|[A-Za-z][A-Za-z_]*\|'
        return t
def t_PUTS(t):
        r'puts'
        return t
def t_END(t):
        r'end'
        return t        
        
def t_STRING(t):
        r'"[^"]*"'
        t.value = t.value[1:-1]
        return t
        
def t_ELSE(t):
        r'else'
        return t

def t_COMMA(t):
        r','
        return t
        
def t_IDENTIFIER(t):
        r'[A-Za-z][A-Za-z_]*'
        return t
        
def t_NUMBER(t):
        r'-?[0-9]+(?:\.[0-9]+)?'
        t.value = float(t.value)

        return t
        
def t_EQUAL(t):
        r'='
        return t
        
def t_OPERATOR(t):
        r'<|>|==|!=|\+|\*|/'
        return t

def t_LEFTBRACKET(t):
        r'\['
        return t

def t_RIGHTBRACKET(t):
        r'\]'
        return t

def t_error(t):
        pass

def p_exp_start(p):
    'exp : stmnts exp'
    p[0]=p[1]+ p[2]


def p_exp_empty(p):
    'exp : '
    p[0] = []

def p_exp_stmnts(p):
    'stmnts : stmnt stmnts'
    p[0] = [p[1]] + p[2]

def p_stmnt_empty(p):
    'stmnts : '
    p[0] = []
    
def p_exp_assign(p):
    'stmnt : IDENTIFIER EQUAL val'
    p[0] = ("assign", p[1],p[3])

def p_exp_puts(p):
    'stmnt : PUTS val'
    p[0] = ("puts",p[2])

def p_exp_array(p):
    'stmnt : IDENTIFIER EQUAL LEFTBRACKET vals RIGHTBRACKET'
    p[0] = ("array", p[1], p[4] )

def p_exp_nums(p):
    'vals : arrvals'
    p[0] = p[1]

def p_val_func (p):
    'val : stmnt'
    p[0] = p[1]
    

def p_exp_num(p):
    'vals : '
    p[0] = []

def p_exp_valus(p):
    'arrvals : val COMMA arrvals'
    p[0] = [p[1]]+ p[3]
    
def p_exp_arrval(p):
    'arrvals : val'
    p[0]=[p[1]]

def p_exp_iter(p):
    'stmnt : ARRAYEACH DO LOOPVAR stmnts END'
    p[0]=("arrayeach",p[1],p[3],p[4])

def p_exp_for(p):
    'stmnt : FOR IDENTIFIER IN NUMBER DOTS NUMBER stmnts END'
    p[0]=("for",p[2],p[4],p[6],p[7])

def p_returns(p):
    'stmnt : RETURN val'
    p[0] = ("return", p[2])

def p_whens(p):
    '''whens : WHEN val stmnts whens
             | '''
    if (len(p)>2):
        p[0] = [(p[2],p[3])] + p[4]
    else:
        p[0] = []

def p_deffunction(p):
    ''' stmnt : DEF IDENTIFIER '(' vals ')' stmnts END '''
    p[0] = ("deffunction", p[2], p[4], p[6])
 

def p_functioncall(p):
    ''' stmnt : IDENTIFIER '(' vals ')' '''
    p[0] = ("functioncall", p[1],p[3])

def p_inputs(p):
    ''' stmnt : IDENTIFIER EQUAL INPUT '''
    p[0] = ("inputs", p[1])

def p_exp_case(p):
    'stmnt : CASE val whens ELSE stmnts END'
    p[0] = ("casewhen", p[2], p[3], p[5])
    
def p_exp_val_num(p):
    'val : NUMBER'
    p[0] = ("number", p[1])


def p_exp_val_str(p):
    'val : STRING'
    p[0] = ("string",p[1])
    
def p_exp_val_id(p):
    'val : IDENTIFIER'
    p[0] = ("var",p[1])

def p_exp_val_op(p):
    '''val  : val OPERATOR val
            | val '-' val '''
    p[0]=("binop", p[1],p[2],p[3])

def p_error(p):
    print "Syntax error in input! in line " + str(p.lexer.lineno) 
    exit()

def fileread():
        with open('rubycode2.txt', 'r') as f:
             read_data = f.read()
        f.closed
        return read_data

def update_env(environment, var, val):
    environment[var]=val
    
def env_lookup(environment, var):
    if var in environment:
        return environment[var]
    else:
        return None

functions = {}
toret = None


def eval_exp(environment, tree):
    nodetype = tree[0]
    global functions
    global returned
    global toret

    if (toret):
        return 

    if nodetype == "number":
        return int(tree[1])
    elif nodetype == "string":
        return tree[1]
    elif nodetype == "var":
        return env_lookup(environment, tree[1])
    elif nodetype == "number":
        return tree[1]
    elif nodetype == "assign":
        var=tree[1]
        val=eval_exp(environment,tree[2])
        update_env(environment,var,val)
    elif nodetype == "inputs":
        var = tree[1]
        val = input()
        update_env(environment,var,val)
    elif nodetype == "array":
        temp=[]
        treelen=len(tree[2])
        lvar=0
        
        while lvar!=treelen:
            temp.append( eval_exp(environment, tree[2][lvar]) )
            lvar=lvar+1
        update_env(environment, tree[1], temp)

    elif nodetype == "return":
        toret = eval_exp(environment,tree[1])

    elif nodetype == "deffunction":
        functions[tree[1]] = (tree[2],tree[3])

    elif nodetype == "functioncall":
        temp = environment
        t = {}
        # environment = {}
        if tree[1] in functions:
            function = functions[tree[1]]
            if (len(function[0])==len(tree[2])):
                for i in range(0,len(tree[2])):
                    t[function[0][i][1]] = eval_exp(environment,tree [2][i])
                environment = t
                loopvar=0
                while loopvar!=len(function[1]):
                    eval_exp(environment, function[1][loopvar])
                    loopvar=loopvar+1
                    if (toret):
                        tmp = toret
                        toret = None
                        return tmp 
        environment = temp

    elif nodetype == "arrayeach":
        temp=re.search( '[A-Za-z][A-Za-z_]*',tree[1]).group(0)
        arrayvalues = env_lookup(environment, temp)
        times=0
        var=tree[2][1:-1]
        while times!=len(arrayvalues):
            update_env(environment, var, arrayvalues[times])
            innerlen=0
            while innerlen!=len(tree[3]):
                eval_exp(environment, tree[3][innerlen])
                innerlen=innerlen+1
                
            times=times+1
    elif nodetype == "for":
        forvar = tree[1]
        init = tree[2]
        endat = tree[3]
        
        while init!=endat:
            update_env(environment, forvar, init)
            innerlen=0
            while innerlen!=len(tree[4]):
                eval_exp(environment, tree[4][innerlen])    
                innerlen=innerlen+1
            init = init+1
        
    elif nodetype == "casewhen":
        tocmp = eval_exp(environment,tree[1])
        for conds in tree[2]:
            if (tocmp == conds[0][1]):
                loopvar=0
                while loopvar!=len(conds[1]):
                    eval_exp(environment, conds[1][loopvar])
                    loopvar=loopvar+1
                return
        loopvar=0
        while loopvar!=len(tree[3]):
            eval_exp(environment, tree[3][loopvar])
            loopvar=loopvar+1

    elif nodetype == "binop":
        left_child = tree[1]
        operator = tree[2]
        right_child = tree[3]
        left_val = eval_exp(environment, left_child)
        right_val = eval_exp(environment, right_child)
        if operator == "+":
            return left_val + right_val
        elif operator == "-":
            return left_val - right_val
        elif operator == "*":
            return left_val * right_val
        elif operator == "/":
            return left_val / right_val
    elif nodetype =="puts":
        x=tree[1]
        print eval_exp(environment, x)

rubylexer = lex.lex()
rubyparser = yacc.yacc()
data=fileread()

rubylexer.input(data)
# while True:
#     tok = rubylexer.token()
#     if not tok: break
#     print tok

rubyast = rubyparser.parse(data)
print rubyast
environment = {}
loopvar=0

while loopvar!=len(rubyast):
    eval_exp(environment, rubyast[loopvar])
    loopvar=loopvar+1
