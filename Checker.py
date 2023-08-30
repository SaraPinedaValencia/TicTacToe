class Checker:
    def __init__(self, size: int):
        self.size = size
        self.plantilla_x = [[0 for i in range(size)] for j in range(size)]
        self.plantilla_y = [[0 for i in range(size)] for j in range(size)]

        self.plantilla_diagonal_1 = [[0 for i in range(size)] for j in range(size)]
        self.plantilla_diagonal_2 = [[0 for i in range(size)] for j in range(size)]

        self.comparador_nulos = [[None for i in range(size)] for j in range(size)]

    def llenar_plantillas(self, turno: int, posicion_actual_x: int, posicion_actual_y: int):

        if turno % 2 == 1:
            if self.plantilla_x[posicion_actual_x][posicion_actual_y] is not None:
                self.plantilla_x[posicion_actual_x][posicion_actual_y] = 1

            if self.plantilla_y[posicion_actual_x][posicion_actual_y] is not None:
                self.plantilla_y[posicion_actual_x][posicion_actual_y] = 1

            if self.plantilla_diagonal_1[posicion_actual_x][posicion_actual_y] is not None:
                self.plantilla_diagonal_1[posicion_actual_x][posicion_actual_y] = 1

            if self.plantilla_diagonal_2[posicion_actual_x][posicion_actual_y] is not None:
                self.plantilla_diagonal_2[posicion_actual_x][posicion_actual_y] = 1

        if turno % 2 == 0:
            if self.plantilla_x[posicion_actual_x][posicion_actual_y] is not None:
                self.plantilla_x[posicion_actual_x][posicion_actual_y] = 2

            if self.plantilla_y[posicion_actual_x][posicion_actual_y] is not None:
                self.plantilla_y[posicion_actual_x][posicion_actual_y] = 2

            if self.plantilla_diagonal_1[posicion_actual_x][posicion_actual_y] is not None:
                self.plantilla_diagonal_1[posicion_actual_x][posicion_actual_y] = 2

            if self.plantilla_diagonal_2[posicion_actual_x][posicion_actual_y] is not None:
                self.plantilla_diagonal_2[posicion_actual_x][posicion_actual_y] = 2


    def ponedor_de_nones_x(self, posicion_actual_x: int):
        contador_j1 = 0
        contador_j2 = 0
        for i in range(self.size):
            if self.plantilla_x[posicion_actual_x][i] == 1:
                contador_j1 += 1

            if self.plantilla_x[posicion_actual_x][i] == 2:
                contador_j2 += 1

        if contador_j1 > 0 and contador_j2 > 0:
            for j in range(self.size):
                self.plantilla_x[posicion_actual_x][j] = None

        if contador_j1 > 0 and contador_j2 == 0:
            pass

        if contador_j2 > 0 and contador_j1 == 0:
            pass

        contador_j1 = 0
        contador_j2 = 0

    def ponedor_de_nones_y(self, posicion_actual_y: int):
        contador_j1 = 0
        contador_j2 = 0
        for i in range(self.size):
            if self.plantilla_y[i][posicion_actual_y] == 1:
                contador_j1 += 1

            if self.plantilla_y[i][posicion_actual_y] == 2:
                contador_j2 += 1

        if contador_j1 > 0 and contador_j2 > 0:
            for j in range(self.size):
                self.plantilla_y[j][posicion_actual_y] = None

        if contador_j1 > 0 and contador_j2 == 0:
            pass

        if contador_j2 > 0 and contador_j1 == 0:
            pass

        contador_j1 = 0
        contador_j2 = 0

    def ponedor_nones_diagonal_1(self):
        contador_j1 = 0
        contador_j2 = 0

        for filas in range(self.size):
            if self.plantilla_diagonal_1[filas][filas] == 1:
                contador_j1 += 1

            if self.plantilla_diagonal_1[filas][filas] == 2:
                contador_j2 += 1

        if contador_j1 > 0 and contador_j2 > 0:
            for filas in range(self.size):
                for columnas in range(self.size):
                    self.plantilla_diagonal_1[filas][columnas] = None

        if contador_j1 > 0 and contador_j2 == 0:
            pass

        if contador_j2 > 0 and contador_j1 == 0:
            pass

        contador_j1 = 0
        contador_j2 = 0

    def ponedor_nones_diagonal_2(self):
        contador_j1 = 0
        contador_j2 = 0

        for filas in range(self.size):
            columnas = self.size - filas -1
            if self.plantilla_diagonal_2[filas][columnas] == 1:
                contador_j1 += 1

            if self.plantilla_diagonal_2[filas][columnas] == 2:
                contador_j2 += 1



        if contador_j1 > 0 and contador_j2 > 0:
            for filas in range(self.size):
                for columnas in range(self.size):
                    self.plantilla_diagonal_2[filas][columnas] = None

        if contador_j1 > 0 and contador_j2 == 0:
            pass

        if contador_j2 > 0 and contador_j1 == 0:
            pass

        contador_j1 = 0
        contador_j2 = 0


    def ganador_x(self):
        contador_j1: int = 0
        contador_j2: int = 0

        for filas in range(self.size):

            for columnas in range(self.size):
                if self.plantilla_x[filas][columnas] == 1:
                    contador_j1 += 1

                if self.plantilla_x[filas][columnas] == 2:
                    contador_j2 += 1

            if contador_j1 == self.size:
                contador_j1 = 0
                contador_j2 = 0
                return 1

            if contador_j2 == self.size:
                contador_j1 = 0
                contador_j2 = 0
                return 2

            else:
                contador_j1 = 0
                contador_j2 = 0

    def ganador_y(self):
        contador_j1: int = 0
        contador_j2: int = 0

        for filas in range(self.size):
            for columnas in range(self.size):
                if self.plantilla_y[columnas][filas] == 1:
                    contador_j1 += 1

                if self.plantilla_y[columnas][filas] == 2:
                    contador_j2 += 1

            if contador_j1 == self.size:
                contador_j1 = 0
                contador_j2 = 0
                return 1

            if contador_j2 == self.size:
                contador_j1 = 0
                contador_j2 = 0
                return 2

            else:
                contador_j1 = 0
                contador_j2 = 0

    def ganador_diagonal_1(self):
        contador_j1 = 0
        contador_j2 = 0

        for filas in range(self.size):
            if self.plantilla_diagonal_1[filas][filas] == 1:
                contador_j1 += 1

            if self.plantilla_diagonal_1[filas][filas] == 2:
                contador_j2 += 1

        if contador_j1 == self.size:
            contador_j1 = 0
            contador_j2 = 0
            return 1

        if contador_j2 == self.size:
            contador_j1 = 0
            contador_j2 = 0
            return 2

        else:
            contador_j1 = 0
            contador_j2 = 0

    def ganador_diagonal_2(self):
        contador_j1 = 0
        contador_j2 = 0

        for filas in range(self.size):
            columnas = self.size - filas - 1
            if self.plantilla_diagonal_2[filas][columnas] == 1:
                contador_j1 += 1

            if self.plantilla_diagonal_2[filas][columnas] == 2:
                contador_j2 += 1

        if contador_j1 == self.size:
            contador_j1 = 0
            contador_j2 = 0
            return 1

        if contador_j2 == self.size:
            contador_j1 = 0
            contador_j2 = 0
            return 2

        else:
            contador_j1 = 0
            contador_j2 = 0


    def es_imposible_ganar(self):
        # si el contador llega a 4 , es imposible ganar

        contador = 0

        if self.plantilla_x == self.comparador_nulos:
            contador += 1

        if self.plantilla_y == self.comparador_nulos:
            contador += 1

        if self.plantilla_diagonal_1 == self.comparador_nulos:
            contador += 1

        if self.plantilla_diagonal_2 == self.comparador_nulos:
            contador += 1

        if contador == 4:
            return True

        if contador < 4:
            return False