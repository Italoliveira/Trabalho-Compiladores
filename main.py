# main.py
import sys
import os
from lexer import lexer, symbol_table  
from parser import parser

def executar(file):

    file_path = f'./codigos/{file}/main.go'

    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            data = file.read()
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
        return

    lexer.input(data)
    os.system("cls")

    tokens = list(lexer)

    max_value_length = max(len(token.value) for token in tokens) if tokens else 10

    print("Tokens encontrados:")
    print(f"{'Tipo':12} | {'Valor':{max_value_length}} | {'Linha':^6} | {'Posição':^8}")
    print("-" * (35 + max_value_length))

    for token in tokens:
        print(f"{token.type:12} | {token.value:{max_value_length}} | {token.lineno:^6} | {token.lexpos:^8}")

    print("\nAnálise Sintática \n")

    result = parser.parse(data)
    print("Parsing concluído.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py <caminho_do_arquivo>")
    else:
        executar(sys.argv[1])
