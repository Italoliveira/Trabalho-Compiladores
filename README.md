# Analisador Léxico e Sintático para Go

Este projeto consiste em um analisador léxico e sintático para arquivos escritos em Go. Ele lê o código-fonte, identifica os tokens e realiza a análise sintática com base em regras definidas.

# Estrutura do Projeto

- main.py: Arquivo principal que executa a análise léxica e sintática.

- lexer.py: Contém a implementação do analisador léxico, responsável por identificar tokens no código.

- parser.py: Contém a implementação do analisador sintático, responsável por verificar a estrutura do código.

- codigos/: Diretório onde devem ser armazenados os arquivos Go a serem analisados.

# Como Funciona o Lexer

O lexer (analisador léxico) lê o código Go e divide-o em tokens, que são unidades mínimas significativas do código, como palavras-chave, identificadores, operadores e símbolos de pontuação.

Após a leitura do arquivo, ele exibe os tokens encontrados no seguinte formato:

Cada linha contém:

- Tipo: Tipo do token (palavra-chave, identificador, símbolo, etc.).

- Valor: O valor específico do token identificado.

- Linha: A linha do código onde o token foi encontrado.

- Posição: A posição do token na linha.

# Como Funciona o Parser

O parser (analisador sintático) verifica se o código-fonte segue as regras da linguagem. Ele usa os tokens extraídos pelo lexer para montar uma estrutura sintática válida.

Se o código estiver correto, o parser exibe:

Caso haja erros, o parser indicará o problema encontrado.

# Como Executar o Projeto

- Certifique-se de ter o Python instalado.

- Clone este repositório:

- Instale as dependências, caso existam (se houver bibliotecas externas, liste-as aqui).

- Adicione um arquivo Go dentro do diretório codigos/, por exemplo:

- Execute o analisador com:

  Onde exemplo é o nome da pasta contendo o código a ser analisado.

- O resultado da análise será exibido no terminal.

# Observações

Se o arquivo não for encontrado, será exibida a mensagem de erro correspondente.

O código-fonte deve estar corretamente formatado para que o parser possa analisá-lo corretamente.

# Autor

Este projeto foi desenvolvido para fins acadêmicos e experimentação com análise léxica e sintática.
