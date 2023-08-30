class TicTacToe:
    def __init__(self, size):
        self.size = size
        self.board = [[" " for _ in range(size)] for _ in range(size)]

    def print_board(self):
        for filas in range(self.size):
            for columnas in range(self.size):
                if self.board[filas][columnas] == " ":
                    print("__", end=" ")
                else:
                    print(self.board[filas][columnas], end=" ")
            print()

    def make_move_x(self, filas, columnas):
        if (filas < self.size) and (columnas < self.size):
            if self.board[filas][columnas] == " ":
                self.board[filas][columnas] = "X"


    def make_move_o(self, filas, columnas):
        if (filas < self.size) and (columnas < self.size):
            if self.board[filas][columnas] == " ":
                self.board[filas][columnas] = "O"