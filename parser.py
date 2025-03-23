import ply.yacc as yacc
from lexer import tokens, symbol_table

# Programa principal
def p_program(p):
    '''program : package imports statement'''
    pass

# Definição de pacote
def p_package(p):
    '''package : PACKAGE ID'''
    pass

# Importações
def p_imports(p):
    '''imports : IMPORT STRING
               | IMPORT LPAREN import RPAREN
               | empty'''
    pass

def p_import(p):
    '''import : STRING import
              | empty'''
    pass

# Declarações
def p_statement(p):
    '''statement : function_statement statement
                | variable_global_statement statement
                | struct_statement statement
                | const statement
                | method_statement statement
                | interface_statement statement
                | type_alias statement
                | empty'''
    pass

# Tipo alias
def p_type_alias(p):
    '''type_alias : TYPE ID types'''
    pass

# Interface
def p_interface_statement(p):
    '''interface_statement : TYPE ID INTERFACE LBRACE method_list RBRACE'''
    pass

def p_method_list(p):
    '''method_list : ID LPAREN args RPAREN types method_list
                   | empty'''
    pass

# Métodos
def p_method_statement(p):
    '''method_statement : FUNC LPAREN ID ID RPAREN ID LPAREN args RPAREN LBRACE content RBRACE
                        | FUNC LPAREN ID ID RPAREN ID LPAREN args RPAREN TYPES LBRACE content RBRACE'''
    pass

# Constantes
def p_const(p):
    '''const : CONST LPAREN constant RPAREN'''
    pass

def p_constant(p):
    '''constant : ID EQUAL value constant
                | empty'''
    pass

# Structs
def p_struct_statement(p):
    '''struct_statement : TYPE ID STRUCT LBRACE field RBRACE'''
    pass

def p_field(p):
    '''field : ID types field
             | ID ID DOT ID
             | empty'''
    pass

# Funções
def p_function_statement(p):
    '''function_statement : FUNC ID LPAREN args RPAREN types LBRACE content RBRACE
                          | FUNC ID LPAREN args RPAREN LBRACE content RBRACE'''
    pass

def p_function(p):
    '''function : ID LPAREN parameters RPAREN'''
    pass

def p_parameters(p):
    '''parameters : expression
                  | CHAN TYPES
                  | expression COMMA parameters
                  | empty'''
    pass

# Argumentos
def p_args(p):
    '''args : ID types
            | ID CHAN ID 
            | ID CHAN ID COMMA args
            | ID CHAN types 
            | ID CHAN types COMMA args
            | ID types COMMA args
            | ID COMMA args
            | ID collection_args COMMA args
            | ID collection_args
            | ID POINTER callback
            | p_map_args COMMA args
            | p_map_args
            | empty'''
    pass

def p_collection_args(p):
    '''
        collection_args : LBRACKET RBRACKET POINTER ID
                        | LBRACKET RBRACKET ID
    '''
    pass

def p_map_args(p):
    '''p_map_args : ID POINTER brackets TYPES'''
    pass

def p_brackets(p):
    '''brackets : LBRACKET NUMBER RBRACKET brackets
                | LBRACKET NUMBER RBRACKET
                | LBRACKET STRING RBRACKET brackets
                | LBRACKET STRING RBRACKET
                | LBRACKET ID RBRACKET
                | LBRACKET ID RBRACKET brackets'''
    pass

# Tipos
def p_types(p):
    '''types : TYPES
             | array_statement
             | pointer_statement
             | slice_statement
             | MAP LBRACKET TYPES RBRACKET'''
    pass

def p_pointer_statement(p):
    '''pointer_statement : POINTER types
                         | POINTER ID'''
    pass

def p_array_statement(p):
    '''array_statement : LBRACKET NUMBER RBRACKET TYPES
                       | LBRACKET NUMBER RBRACKET TYPES LBRACE values RBRACE
                       | LBRACKET DOT DOT DOT RBRACKET TYPES
                       | LBRACKET DOT DOT DOT RBRACKET TYPES LBRACE values RBRACE'''
    pass

def p_slice_statement(p):
    '''slice_statement : LBRACKET RBRACKET TYPES
                       | LBRACKET RBRACKET TYPES LBRACE values RBRACE'''
    pass

# Variáveis globais
def p_variable_global_statement(p):
    '''variable_global_statement : VAR ID types'''
    pass

# Valores
def p_values(p):
    '''values : value COMMA values
              | value
              | empty'''
    pass

# Conteúdo de blocos
def p_content(p):
    '''content : empty
               | variable_statement content
               | array_statement content
               | callback content
               | variable_redeclaration content
               | if content
               | for content
               | BREAK content
               | goroutine content
               | increment content
               | decrement content
               | switch content
               | ID channel content
               | return content
               | defer content
               | continue content
               | select content
               | channel content'''
    pass

#Continue
def p_continue(p):
    '''
        continue    :  CONTINUE
    '''
    pass

# Canais
def p_channel(p):
    '''channel : CHANNEL_OP value
               | CHANNEL_OP ID
               | CHANNEL_OP callback
               | CHANNEL_OP struct_declaretion'''
    pass

# Lambdas
def p_lambda(p):
    '''lambda : FUNC LPAREN args RPAREN types LBRACE content RBRACE
              | FUNC LPAREN args RPAREN LBRACE content RBRACE'''
    pass

# Seleção
def p_select(p):
    '''select : SELECT LBRACE select_cases RBRACE'''
    pass

def p_select_cases(p):
    '''select_cases : CASE expression COLON content select_cases
                    | DEFAULT COLON content
                    | empty'''
    pass

# Defer
def p_defer(p):
    '''defer : DEFER callback'''
    pass

# Switch
def p_switch(p):
    '''switch : SWITCH ID LBRACE cases_value default RBRACE
              | SWITCH LBRACE cases_rel default RBRACE'''
    pass

def p_cases_rel(p):
    '''cases_rel : CASE case_condition COLON content cases_rel
                 | empty'''
    pass

def p_case_condition(p):
    '''case_condition : ID REL_OP value
                      | boolean
                      | callback'''
    pass

def p_default(p):
    '''default : DEFAULT COLON content
               | empty'''
    pass

def p_cases_value(p):
    '''cases_value : CASE value COLON content cases_value
                   | empty'''
    pass

# Goroutines
def p_goroutine(p):
    '''goroutine : GO callback
                 | GO lambda LPAREN parameters RPAREN'''
    pass

# Condicionais
def p_if(p):
    '''if : IF expression LBRACE content RBRACE else'''
    pass

def p_else(p):
    '''else : ELSE LBRACE content RBRACE
            | ELSE if
            | empty'''
    pass

# Expressões
def p_expression(p):
    '''expression : value
                  | LPAREN expression RPAREN
                  | expression ARITH_OP expression
                  | expression REL_OP expression
                  | expression LOG_OP expression
                  | expression POINTER expression
                  | NOT expression
                  | ID COLON_EQUAL channel
                  | channel
                  | increment
                  | lambda
                  | decrement
                  | struct
                  | collection_statement
                  | callback
                  | struct_declaretion
                  | address_pointer
                  | ID
                  | collection
                  | map_statement
                  | map'''
    pass

def p_collection(p):
    '''
        collection  : ID LBRACKET ID RBRACKET DOT ID
                    | ID LBRACKET ID RBRACKET 
    '''

# Loops
def p_for(p):
    '''for : FOR LBRACE content RBRACE
           | FOR NOT ID LBRACE content RBRACE
           | FOR expression LBRACE content RBRACE
           | FOR for_declaration SEMICOLON expression SEMICOLON expression LBRACE content RBRACE
           | FOR ID COMMA ID COLON_EQUAL RANGE ID LBRACE content RBRACE
           | FOR UNDERSCORE COMMA ID COLON_EQUAL RANGE ID LBRACE content RBRACE
           | FOR ID COLON_EQUAL RANGE ID LBRACE content RBRACE'''
    pass

def p_for_declaration(p):
    '''for_declaration : ID COLON_EQUAL NUMBER'''
    pass

# Maps
def p_map_statement(p):
    '''map_statement : MAP LBRACKET TYPES RBRACKET map_statement
                     | MAP LBRACKET TYPES RBRACKET TYPES LBRACE map RBRACE
                     | MAP LBRACKET TYPES RBRACKET TYPES'''
    pass

def p_map(p):
    '''map : empty
           | LBRACE map RBRACE
           | LBRACE map RBRACE COMMA map
           | value COLON value
           | value COLON value COMMA map
           | value COLON map
           | value COLON map COMMA map'''
    pass

# Retorno
def p_return(p):
    '''return : RETURN
              | RETURN expression
              | empty'''
    pass

# Structs
def p_struct_declaretion(p):
    '''struct_declaretion : ID LBRACE struct_declaretion_values RBRACE'''
    pass

def p_struct_declaretion_values(p):
    '''struct_declaretion_values : values
                                 | LBRACE struct_declaretion_values RBRACE'''
    pass

def p_collection_statement(p):
    '''
        collection_statement    : LBRACKET RBRACKET POINTER ID LBRACE collection_types RBRACE
                                | LBRACKET RBRACKET ID LBRACE collection_types RBRACE
                                | ADDRESS ID LBRACE collection_types RBRACE
                                | ID LBRACE collection_types RBRACE
    '''
    pass

def p_collection_types(p):
    '''
        collection_types    : ID
                            | ID COMMA collection_types
                            | ID COLON value
                            | ID COLON value COMMA collection_types
    '''
    pass

# Variáveis
def p_variable_statement(p):
    '''variable_statement : VAR ID EQUAL slice_statement
                          | VAR ID EQUAL array_statement
                          | VAR ID types EQUAL expression
                          | VAR ID EQUAL expression
                          | VAR ID ID EQUAL expression
                          | VAR ID callback
                          | ID map_position EQUAL expression
                          | ID COLON_EQUAL expression
                          | map_position COLON_EQUAL expression
                          | ID COLON_EQUAL slice_statement
                          | ID COLON_EQUAL array_statement
                          | VAR ID TYPES'''
    pass

def p_map_position(p):
    '''map_position : LBRACKET STRING RBRACKET map_position
                    | LBRACKET NUMBER RBRACKET map_position
                    | LBRACKET STRING RBRACKET
                    | LBRACKET NUMBER RBRACKET'''
    pass

def p_variable_redeclaration(p):
    '''variable_redeclaration : ID EQUAL expression
                              | ID ASSIGN_OP expression
                              | callback ASSIGN_OP expression
                              | ID DOT ID EQUAL expression'''
    pass

# Booleanos
def p_boolean(p):
    '''boolean : FALSE
               | TRUE'''
    pass

# Ponteiros
def p_pointer(p):
    '''pointer : ID LBRACKET NUMBER RBRACKET
               | ID LBRACKET NUMBER COLON NUMBER RBRACKET'''
    pass

# Incremento e decremento
def p_increment(p):
    '''increment : ID INCREMENT'''
    pass

def p_decrement(p):
    '''decrement : ID DECREMENT'''
    pass

# Ponteiros de endereço
def p_address_pointer(p):
    '''address_pointer : ADDRESS ID'''
    pass

# Structs
def p_struct(p):
    '''struct : ID DOT ID
              | ID DOT struct'''
    pass

# Callbacks
def p_callback(p):
    '''callback : function
                | ID DOT ID LPAREN ID LPAREN ID RPAREN RPAREN
                | ID
                | function DOT callback
                | ID DOT callback
                | empty'''
    pass

# Valores
def p_value(p):
    '''value : NUMBER
             | STRING
             | LBRACE values RBRACE
             | map_varible
             | boolean
             | pointer'''
    pass

def p_map_varible(p):
    '''map_varible : ID brackets'''
    pass

# Regra vazia
def p_empty(p):
    '''empty :'''
    pass

# Tratamento de erros
def p_error(p):
    if p:
        last_cr = p.lexer.lexdata.rfind('\n', 0, p.lexpos)
        lineno = p.lexer.lexdata.count('\n', 0, p.lexpos) + 1
        print(f"Erro de sintaxe no token '{p.value}' (Tipo: {p.type}) na linha {lineno} - {p.lexpos}")
    else:
        print("Erro de sintaxe inesperado no final do arquivo")

# Criar o parser
parser = yacc.yacc()