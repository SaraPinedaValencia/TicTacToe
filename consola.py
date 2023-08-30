from juego import Juego

class Consola:
    def __init__(self):
        self.puntaje_j1 = 0
        self.puntaje_j2 = 0

    def setter_calcular_puntaje_j1(self):
        self.puntaje_j1 += 1
        return self.puntaje_j1

    def setter_calcular_puntaje_j2(self):
        self.puntaje_j2 += 1
        return self.puntaje_j2

    def getter_puntaje_j1(self):
        return self.puntaje_j1

    def getter_puntaje_j2(self):
        return self.puntaje_j2


    def imprimir_planta_de_inicio(self):
        print('''
          ___  __   __  _  _ __ 
         |_   _||  _ \ |   || |/ /|   _|
            | |   | |__) |  | |  | ' /   | |  
            | |   |  _  /   | |  |  <    | |  
            | |   | | \ \  | | | . \  | | 
            ||   ||  \_\|__|||\_\|___|

        ''')
        print('''REGLAS DEL JUEGO Y COMO JUGAR:
        a. Se debe Escoger de que tamaño desean su tamblero de juego
        b. El jugador 1 tendra como figura la X y el jugador 2 tendrá la O
        c. El juego les irá indicando cuando poner sus posiciones, recuerden: 
           el primer número corresponde a las filas y el segundo número corresponde a las columnas
        d. El jugador que primero tenga una linea completa con su figura GANA!!
        ''')

    def crear_objeto(self, size):
        mi_juego_actual = Juego(size)
        return mi_juego_actual

    def empezar_juego(self):

        print()
        size = int(input("ingresar el tamaño del tablero: "))
        print()
        mi_juego_actual = self.crear_objeto(size)
        puntaje = mi_juego_actual.main()

        while True:
            print()
            seguir = int(input('''La partida ha finalizado:
1. Seguir jugando
2. Cerrar juego
            
-> '''))
            if seguir == 1:
                if puntaje == 1:

                    print(
                        f"el puntaje del jugador uno es: {self.setter_calcular_puntaje_j1()} y el del jugador dos es: {self.getter_puntaje_j2()}")
                    self.empezar_juego()

                if puntaje == 2:
                    print(
                        f"el puntaje del jugador uno es: {self.getter_puntaje_j1()} y el del jugador dos es: {self.setter_calcular_puntaje_j2()}")
                    self.empezar_juego()

            else:
                return


jueguito = Consola()
jueguito.imprimir_planta_de_inicio()
jueguito.empezar_juego()