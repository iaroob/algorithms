import sys

from typing import List


def read_data(f) -> List[int]:
    return [int(l) for l in f.readlines()]


def error(m):
    sys.stderr.write(m + "\n")
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        error("Uso: es_pico.py <posición>")
    try:
        p = int(sys.argv[1])
    except:
        error("La posición debe ser un entero")
    try:
        v = read_data(sys.stdin)
    except Exception as e:
        error(f"Error leyendo el vector:\n {e}")
    if p < 0 or p >= len(v):
        error("La posición debe ser un número entre 0 y la longitud del vector")
    if (len(v) <= 1
        or p == 0 and v[0] >= v[1]
        or p == len(v) - 1 and v[-1] >= v[-2]
        or v[p-1] <= v[p] and v[p] >= v[p+1]):
            print("OK")
    else:
        print(f"Error, {p} no es un pico")
