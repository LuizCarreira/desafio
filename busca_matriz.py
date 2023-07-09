"""Modulo que implementa a solucao do segundo desafio"""

from typing import List


class BuscaMatriz:
    """Classe BuscaMatriz.

    Essa classe possui o metodo busca que procura quantas vezes a matrizB pode ser encontrada na matrizA.

    Exemplo:
    >> from busca_matriz import Busca_matriz
    >> matrizA = [[1, 2, 1], [4, 1, 4], [7, 4, 9]]
    >> matrizB = [[1], [4]]
    >> obj = BuscaMatriz(matrizA, matrizB)
    >> qtd = obj.busca()
    >> qtd
    3
    """

    def __init__(self, matrizA: List[List[int]], matrizB: List[List[int]]) -> None:
        self._matrizA = matrizA
        self._matrizB = matrizB

    @property
    def matrizA(self) -> List[List[int]]:
        return self._matrizA

    @matrizA.setter
    def matrizA(self, mat: List[List[int]]) -> None:
        self._matrizA = mat

    @property
    def matrizB(self) -> List[List[int]]:
        return self._matrizB

    @matrizB.setter
    def matrizB(self, mat: List[List[int]]) -> None:
        self._matrizB = mat

    def _percorre_matriz(self, altura: int, largura: int):
        """"Gera sub matrizes a partir da matrizA."""
        tamanho_passo = 1

        for linha in range(0, len(self._matrizA) - altura + 1, tamanho_passo):
            for coluna in range(0, len(self._matrizA[0]) - largura + 1, tamanho_passo):
                yield coluna, self._matrizA[linha:linha + altura]

    def busca(self):
        """"Busca a matrizb em sub matrizes da matrizA.

        As sub matrizes tem as mesmas dimensoes da matrizB
        """
        altura = len(self._matrizB)
        largura = len(self._matrizB[0])

        qtd = 0
        for coluna, matriz_extraida in self._percorre_matriz(altura, largura):
            linhas_iguais = 0
            for linha in range(len(matriz_extraida)):
                elementos_iguais = 0
                lista_1 = matriz_extraida[linha][coluna:coluna + largura]
                lista_2 = self._matrizB[linha]
                for e1, e2 in zip(lista_1, lista_2):
                    if e1 == e2:
                        elementos_iguais += 1
                    else:
                        break

                if elementos_iguais != len(lista_1):
                    break

                linhas_iguais += 1

            if linhas_iguais == len(matriz_extraida):
                qtd += 1

        return qtd


if __name__ == '__main__':
    matrizA = [[1, 2, 1], [4, 1, 2], [5, 4, 1]]
    matrizB = [[1, 2], [4, 1]]
    obj = BuscaMatriz(matrizA, matrizB)
    qtd = obj.busca()
    print(qtd)
