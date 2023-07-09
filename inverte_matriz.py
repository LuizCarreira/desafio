""""Modulo inverte_matriz"""

from typing import List


class InverteMatriz:
    """"Classe InverteMatriz.

    Esta classe contem o metodo inverte que inverte as diagonais de uma matriz quadrada

    Exemplo
    -------
    >> from inverte_matriz import InverteMatrix
    >> matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >> obj = InverteMatriz(matriz)
    >> print(str(obj))
    Matriz = [[1, 2, 3]
              [4, 5, 6]
              [7, 8, 9]]
    >> obj.inverte()
    >> print(str(obj))
    Matriz = [[9, 2, 7]
              [4, 5, 6]
              [3, 8, 1]]
    """

    def __init__(self, matriz: List[List[int]]) -> None:
        self._matriz = matriz

    @property
    def matriz(self) -> List[List[int]]:
        return self._matriz

    @matriz.setter
    def matriz(self, mat: List[List[int]]) -> None:
        self._matriz = mat

    def inverte(self):
        """"Inverte as diagonais de uma matriz quadrada.
        """
        ordem_matriz = len(self._matriz)

        l1 = list(range(ordem_matriz))
        l2 = l1.copy()

        num_iteracoes = (ordem_matriz // 2)

        # inverte diagonal principal
        produto_cartesiano = list(zip(l1, l2))
        p1 = 0
        p2 = ordem_matriz - 1

        for i in range(num_iteracoes):
            aux = self._matriz[produto_cartesiano[p1][0]][produto_cartesiano[p1][1]]
            self._matriz[produto_cartesiano[p1][0]][produto_cartesiano[p1][1]] = \
                self._matriz[produto_cartesiano[p2][0]][produto_cartesiano[p2][1]]
            self._matriz[produto_cartesiano[p2][0]][produto_cartesiano[p2][1]] = aux
            p1 += 1
            p2 -= 1

        # inverte diagonal secundaria
        produto_cartesiano = list(zip(l1, l2[::-1]))
        p1 = 0

        for i in range(num_iteracoes):
            aux = self._matriz[produto_cartesiano[p1][0]][produto_cartesiano[p1][1]]
            self._matriz[produto_cartesiano[p1][0]][produto_cartesiano[p1][1]] = \
                self._matriz[produto_cartesiano[p1][1]][produto_cartesiano[p1][0]]
            self._matriz[produto_cartesiano[p1][1]][produto_cartesiano[p1][0]] = aux
            p1 += 1

    def __str__(self):
        msg = ""
        ordem_matriz = len(self._matriz)
        for i in range(ordem_matriz):
            if i == 0:
                msg += "Matriz: [" + str(self._matriz[i]) + "\n"
            elif i == ordem_matriz - 1:
                msg += "         " + str(self._matriz[i]) + "]"
            else:
                msg += "         " + str(self._matriz[i]) + "\n"

        return msg


if __name__ == '__main__':
    matriz = [[3, 5, -3, 6], [4, 1, 7, -4], [-9, -1, -7, 3], [7, 2, 1, 2]]
    obj = InverteMatriz(matriz)
    print(str(obj))
    obj.inverte()
    print(str(obj))
