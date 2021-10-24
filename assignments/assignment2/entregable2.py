import sys
from typing import *


# Entrada: El descriptor de fichero. Podemos leer una línea de texto con f.readline().
#          El formato de la entrada se especifica en el apartado 2.1.
# Salida: Una lista de booleanos con True si la moneda está cara arriba (‘o’) o
#         False si está cara abajo (‘x’).
def read_data(f) -> List[bool]:
    raise NotImplementedError()


# Entrada: Un parámetro, el mismo que devuelve la función read_data.
# Salida: Lista de enteros con las instrucciones para el robot.
def process(stack: List[bool]) -> List[int]:
    raise NotImplementedError()


# Entrada: Un parámetro, el mismo que devuelve la función process.
# Salida: No devuelve nada. Solo muestra líneas de texto por la salida estándar
#         siguiendo el formato que se detalla en el apartado 2.2.
def show_results(solution: List[int]):
    raise NotImplementedError()


if __name__ == '__main__':
    my_stack = read_data(sys.stdin)
    my_solution = process(my_stack)
    show_results(my_solution)
