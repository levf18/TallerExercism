class Matrix:
    def __init__(self, matrix_string):
        matriz = matrix_string.split('\n')
        self.matriz = []
        for i in matriz:
            fila = list(map(int, i.split()))
            self.matriz.append(fila)

    def row(self, index):
        return self.matriz[index-1]

    def column(self, index):
        columna = []
        for fila in self.matriz:
            columna.append(fila[index-1])
        return columna
