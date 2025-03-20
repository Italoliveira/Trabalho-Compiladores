import ply.lex as lex

keywords = {
    'BREAK', 'DEFAULT', 'FUNC', 'INTERFACE', 'SELECT', 'CASE', 'DEFER', 'GO', 'MAP',
    'STRUCT', 'CHAN', 'ELSE','PACKAGE', 'SWITCH', 'CONST','IF', 'RANGE', 'TYPE', 
    'CONTINUE', 'FOR', 'IMPORT', 'RETURN', 'VAR', 'TRUE', 'FALSE'
}

types = {"int", "int8", "int16", "int32", "int64", "uint", "uint8", "uint16", "uint32", "uint64", 
         "uintptr", "float32", "float64", "complex64", "complex128", "bool", "string", "byte", 
         "rune", "error", "any"}

tokens = list(keywords) + [
    'ID', 'LBRACE', 'RBRACE', 'LPAREN', 'RPAREN', 'SEMICOLON', 'EQUAL', 'COLON_EQUAL', 'LBRACKET', 'RBRACKET', 
    'COLON', 'DOT', 'COMMA', 'STRING', 'NUMBER', 'INCREMENT', 'DECREMENT', 'NOT', 'POINTER', 'ADDRESS',
    'ARITH_OP', 'REL_OP', 'LOG_OP', 'ASSIGN_OP', 'COMMENT', 'TYPES', 'UNDERSCORE', 'COMMENT_BLOCK',
    'CHANNEL_OP', 'RUNE', 'COMPILER_DIRECTIVE'
]

symbol_table = {}

def t_INCREMENT(t):
    r'\+\+'
    return t

def t_DECREMENT(t):
    r'--'
    return t

t_NOT = r'!'  
t_POINTER = r'\*'  
t_ADDRESS = r'&'  

t_LBRACKET = r'\['  
t_RBRACKET = r'\]'  
t_LBRACE = r'\{'  
t_RBRACE = r'\}'  
t_LPAREN = r'\('  
t_RPAREN = r'\)'  
t_SEMICOLON = r';'  
t_EQUAL = r'='  
t_COLON_EQUAL = r':='  
t_COLON = r':'  
t_DOT = r'\.'  
t_COMMA = r','  

t_STRING = r'\"([^\\"]|\\.)*\"|`[^`]*`'

t_NUMBER = r'0[bB][01]+|0[xX][0-9a-fA-F]+|0[oO][0-7]+|[+-]?[0-9]+(\.[0-9]*)?([eE][+-]?[0-9]+)?|[+-]?[0-9]+(\.[0-9]*)?i'

def t_COMMENT(t):
    r'//.*'
    pass  

def t_COMMENT_BLOCK(t):
    r'/\*[\s\S]*?\*/'
    pass  

def t_RUNE(t):
    r"'([^\\']|\\.)'"
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value.upper() in keywords:
        t.type = t.value.upper() 
    elif t.value.lower() in types: 
        t.type = 'TYPES'
    else:
        t.type = 'ID'
        symbol_table[t.value] = {'type': 'ID', 'line': t.lineno, 'position': t.lexpos}
    return t

def t_TYPES(t):
    r'(?:u?int(?:8|16|32|64)?|uintptr|float(?:32|64)|complex(?:64|128)|bool|string|byte|rune|error|any)'
    return t

def t_TRUE(t):
    r'true'
    t.type = 'TRUE'
    return t

def t_FALSE(t):
    r'false'
    t.type = 'FALSE'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t\r'

t_ARITH_OP = r'\+|\-|\/|%'

t_REL_OP = r'==|!=|<=|>=|<|>'

t_LOG_OP = r'&&|\|\|'

t_ASSIGN_OP = r'\+=|-=|\*=|/=|%='

def t_CHANNEL_OP(t):
    r'<-|->'
    return t

def t_error(t):
    if t.value[0] == '-' and len(t.value) > 1 and t.value[1] == '>':
        print(f"Erro léxico: Operador '->' inválido na linha {t.lineno}, posição {t.lexpos}")
    else:
        print(f"Erro léxico: Caractere inválido '{t.value[0]}' na linha {t.lineno}, posição {t.lexpos}")
    t.lexer.skip(1)

lexer = lex.lex()