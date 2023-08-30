from Checker import Checker
from Tictactoe import TicTacToe

class Juego:

    def __init__(self, size):
        self.size = size

    def main(self):

        mi_tablero = TicTacToe(self.size)

        verificador = Checker(self.size)

        turno = 1


        while True:

            # turno x
            if turno % 2 == 1:
                print()
                while True:
                    posicion_actual_en_x_jugador_1 = int(input("ingrese la posicion x en la cual quiere posicionar su X en el tablero: "))
                    posicion_actual_en_y_jugador_1 = int(input("ingrese la posicion y en la cual quiere posicionar su X en el tablero: "))

                    mi_tablero.make_move_x(posicion_actual_en_x_jugador_1, posicion_actual_en_y_jugador_1)

                    mi_tablero.print_board()


                    if (posicion_actual_en_x_jugador_1 > self.size) or (posicion_actual_en_y_jugador_1 > self.size) :
                        print("posicion invalida")

                    if (posicion_actual_en_x_jugador_1 < self.size) and (posicion_actual_en_y_jugador_1 < self.size):

                        verificador.llenar_plantillas(turno, posicion_actual_en_x_jugador_1, posicion_actual_en_y_jugador_1)

                        verificador.ponedor_de_nones_x(posicion_actual_en_x_jugador_1)
                        verificador.ponedor_de_nones_y(posicion_actual_en_y_jugador_1)
                        verificador.ponedor_nones_diagonal_1()
                        verificador.ponedor_nones_diagonal_2()

                        if verificador.ganador_x() == 1:
                            print("¡¡La X han ganado!!")
                            return 1

                        if verificador.ganador_y() == 1:
                            print("¡¡La X han ganado!!")
                            return 1

                        if verificador.ganador_diagonal_1() == 1:
                            print("¡¡La X han ganado!!")
                            return 1

                        if verificador.ganador_diagonal_2() == 1:
                            print("¡¡La X han ganado!!")
                            return 1

                        if verificador.es_imposible_ganar() is True:
                            print("Ninguno de los dos jugadores puede ganar")
                            return

                        turno += 1

                        break

            #turno o
            if turno % 2 == 0:
                while True:
                    posicion_actual_en_x_jugador_2 = int(input("ingrese la posicion x en la cual quiere posicionar su O en el tablero: "))
                    posicion_actual_en_y_jugador_2 = int(input("ingrese la posicion y en la cual quiere posicionar su O en el tablero: "))

                    mi_tablero.make_move_o(posicion_actual_en_x_jugador_2, posicion_actual_en_y_jugador_2)

                    mi_tablero.print_board()


                    if (posicion_actual_en_x_jugador_2 > self.size) or (posicion_actual_en_y_jugador_2 > self.size):
                        print("posicion invalida")

                    if (posicion_actual_en_x_jugador_2 < self.size) and (posicion_actual_en_y_jugador_2 < self.size):

                        verificador.llenar_plantillas(turno, posicion_actual_en_x_jugador_2, posicion_actual_en_y_jugador_2)

                        verificador.ponedor_de_nones_x(posicion_actual_en_x_jugador_2)
                        verificador.ponedor_de_nones_y(posicion_actual_en_y_jugador_2)
                        verificador.ponedor_nones_diagonal_1()
                        verificador.ponedor_nones_diagonal_2()

                        if verificador.ganador_x() == 2:
                            print("¡¡La O ha ganado!!")
                            return 2

                        if verificador.ganador_y() == 2:
                            print("¡¡La O ha ganado!!")
                            return 2

                        if verificador.ganador_diagonal_1() == 2:
                            print("¡¡La O ha ganado!!")
                            return 2

                        if verificador.ganador_diagonal_2() == 2:
                            print("¡¡La O ha ganado!!")
                            return 2

                        if verificador.es_imposible_ganar() is True:
                            print("Ninguno de los dos jugadores puede ganar")
                            return

                    turno += 1

                    break