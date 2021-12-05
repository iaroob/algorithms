import sys
from typing import *
from dataclasses import dataclass
from bt_scheme import *

# Tipos ----------------------------------------------------------------------

Board    = List[List[str]]  # Matriz como lista de listas, con un carácter por celda ['#', 'o', '.']
Pos      = Tuple[int, int]  # Posición en el tablero: (fila,col)
Step     = Tuple[Pos, Pos]  # Un movimiento del puzle
Solution = Tuple[Step,...]  # Tupla con los movimientos que resuelven el puzle


# Funciones principales ------------------------------------------------------

# Salida. Matriz como lista de listas, con un carácter por celda ['#', 'o', '.']
def read_data(f) -> Board:
    board = []
    for line in f.readlines():
        board.append(list(line[:-1]))
    return board

def posibles(board: Board, vacia: Pos) -> List[int]:
    posibles = []
    maxr = len(board)
    maxc = len(board[0])
    row, col = vacia
    if row > 1:
        if board[row - 2][col] == "o" and board[row - 1][col] == "o":       #movimineto hacia abajo
            posibles.append(row - 2)
            posibles.append(col)
    if row < maxr - 2:
        if board[row + 2][col] == "o" and board[row + 1][col] == "o":       #movimiento hacia arriba
            posibles.append(row + 2)
            posibles.append(col)
    if col > 1:
        if board[row][col - 2] == "o" and board[row][col - 1] == "o":       #movimiento hacia la derecha
            posibles.append(row)
            posibles.append(col - 2)
    if col < maxc - 2:
        if board[row][col + 2] == "o" and board[row][col + 1] == "o":       #movimiento hacia la izquierda
            posibles.append(row)
            posibles.append(col + 2)
    return posibles

def primera_posible(board: Board, vacia: Pos) -> Iterable[Pos]:
    posiciones = posibles(board, vacia)
    for i in range(len(posiciones)/2):
        col = posiciones.pop()
        row = posiciones.pop()
        yield row, col

def vacias(board: Board) -> Iterable[Pos]:          # Posiciones vacias
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == ".":
                yield row, col

def primera_vacia(board: Board) -> Optional[Pos]:           # Primera posicion vacia encontrada
    try:
        return next(vacias(board))
    except StopIteration:
        return None

def inicio(board: Board) -> int:        # Numero de piezas al inicio del juego
    cont = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "o":
                cont += 1
            # if board[i][j] == ".":
            #     vacia = (i, j)
    return cont #, vacia

# Salida. La solución como una tupla de Step (o None, si no hay solución).
def process(board: Board) -> Optional[Solution]:
    @dataclass
    class Extra:
        board: Board
        piezas: int = inicio(board)
        # vacias: List[Pos]
        # vacias = list
        # vacias.append(inicio(board, filas, columnas)[1])

    class SolitarioDS(DecisionSequence):
        def is_solution(self) -> bool:
            return self.extra.piezas == 1

        def solution(self) -> Optional[Solution]:
            print("SOLUTION")
            return self.decisions()

        def successors(self) -> Iterable["SolitarioDS"]:
            hueco = primera_vacia(self.extra.board)
            if hueco is not None:
                posibles_lista = posibles(self.extra.board, hueco)
                medios = []
                posi_mov = posibles_lista
                for i in range(int(len(posibles_lista)/2)):
                    col = posibles_lista.pop()
                    row = posibles_lista.pop()
                    posible = row, col
                    # self.extra.vacias.append(posible)
                    if posible[0] == hueco[0]:
                        if posible[1] > hueco[1]:
                            medio = posible[0], posible[1] - 1
                            medios.append(medio[0])
                            medios.append(medio[1])
                        else:
                            medio = posible[0], posible[1] + 1
                            medios.append(medio[0])
                            medios.append(medio[1])
                    else:
                        if posible[0] > hueco[0]:
                            medio = posible[0] - 1, posible[1]
                            medios.append(medio[0])
                            medios.append(medio[1])
                        else:
                            medio = posible[0] + 1, posible[1]
                            medios.append(medio[0])
                            medios.append(medio[1])
                    # self.extra.vacias.append(medio)
                    # self.extra.vacias.remove(vacia)
                    self.extra.piezas -= 1
                    self.extra.board[medio[0]][medio[1]] = "."
                    self.extra.board[posible[0]][posible[1]] = "."
                    self.extra.board[hueco[0]][hueco[1]] = "o"
                    yield self.add_decision((posible, hueco), self.extra)
                for i in range(int(len(medios) / 2)):           #devolver las casillas que se han saltado a su estado anterior
                    col = medios.pop()
                    row = medios.pop()
                    self.extra.board[row][col] = "o"
                for i in range(int(len(posi_mov)/2)):           #devolver los posibles que habíamos movido a su estado anterior
                    col = posibles_lista.pop()
                    row = posibles_lista.pop()
                    self.extra.board[row][col] = "o"
                self.extra.board[hueco[0]][hueco[1]] = "."      #devolver el hueco al estado anterior
                self.extra.piezas += 1

        def state(self):
            return len(self), self.extra.piezas

    initial_ds = SolitarioDS(Extra(board))
    return bt_vc_solve(initial_ds)


def show_results(solution: Optional[Solution]):
    if solution is None:
        print('THERE IS NO SOLUTION')
    else:
        for step in solution:
            for i in range(len(step)):
                print(step[i][0][0], step[i][0][1], step[i][1][0], step[i][1][1])


# Programa principal ------------------------------------------------------

if __name__ == '__main__':
    board = read_data(sys.stdin)
    solution = process(board)
    show_results(solution)