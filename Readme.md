# Introdução

Este repositório contém dois arquivos 
principais, `busca_matriz.py` e 
`inverte_matriz.py`. Dentro de cada arquivo, 
é possível encontrar um algoritmo que 
resolve cada um dos dois desafios 
propostos. Para a solução dos problemas, 
não foi utlizado nenhuma biblioteca de 
terceiros. Foi usado apenas a 
biblioteca padrão da linguagem Python 
bem como seus elementos nativos.

# Modelo de Dados

 A linguagem Python não oferece uma
 estrutura do tipo matriz. Portanto, para
 a solução dos problemas, foi usado
 uma lista de listas.
 
Por exemplo, para representar a matriz:
 
        [1 2 3]
    A = [4 5 6]
        [7 8 9]

É preciso criar uma lista de listas:

    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
# Inverte Matriz

O arquivo `inverte_matriz.py` contém
uma classe chamada `InverteMatriz`.
Essa classe possui um método chamado
`inverte`. Esse método inverte as 
diagoanais de uma matriz quadrada.
Dentro do arquivo, é possível
encontrar como usá-lo

Dada a matriz:

        [1 2 3]
    A = [4 5 6]
        [7 8 9]

A resposta será

        [9 2 7]
    A = [4 5 6]
        [3 8 1]
        
# Busca Matriz

O arquivo `busca_matriz.py` possui uma
classe chamada `BuscaMatriz`. Essa classe
possui um método chamado `busca`. Esse
método busca quantas vezes uma matriz B
aparece em uma matriz A.

Dado a matriz A:

        [1 2 1]
        [4 1 2]
        [5 4 1]
        
E a matriz B:

        [1 2]
        [4 1]

A resposta será

    2

# Observação

Como mencionado anteriormente, nenhuma biblioteca
de terceiros foi utilizada. Para além disso,
as soluções propostas não consideraram nenhuma
restrição de complexidade ou de espaço.
