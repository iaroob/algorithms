import sys
from typing import *

def process(problem: str) -> Tuple[int, int, int]:
    def rec(i: int, j: int) -> Tuple[int, int, int]:
        if i == j:
            return 0, i, j
        c = (i + j) // 2
        izda = rec(i, c)
        dcha = rec(c + 1, j)
        aux = problem[c]
        cont = 0
        mejor = 0
        mejorneg = 0
        end = c + 1
        begin = c
        contneg = 0
        endneg = c + 1
        beginneg = c
        if j == len(problem):
            for pos in range(c, j):
                if problem[pos] == aux:
                    cont += 1
                    contneg -= 1
                else:
                    cont -= 1
                    contneg += 1
                if cont > mejor:
                    mejor = cont
                    end = pos + 1
                if contneg > mejorneg:
                    mejorneg = contneg
                    endneg = pos + 1
        else:
            for pos in range(c, j + 1):
                if problem[pos] == aux:
                    cont += 1
                    contneg -= 1
                else:
                    cont -= 1
                    contneg += 1
                if cont > mejor:
                    mejor = cont
                    end = pos + 1
                if contneg > mejorneg:
                    mejorneg = contneg
                    endneg = pos + 1
        cont = mejor
        contneg = mejorneg
        for pos in range(c - 1, i - 1, -1):
            if problem[pos] == aux:
                cont += 1
                contneg -= 1
            else:
                cont -= 1
                contneg += 1
            if cont > mejor:
                mejor = cont
                begin = pos
            if contneg > mejorneg:
                mejorneg = contneg
                beginneg = pos
        if mejorneg > mejor:
            mejor = mejorneg
            begin = beginneg
            end = endneg
        return max(izda, dcha, (mejor, begin, end))
    return rec(0, len(problem))

def read_data(f) -> str:
    return str(f.readline().strip())

def show_results(sol:int ,b:int, e:int):
    print(sol)
    print(b)
    print(e)


if __name__ == "__main__":
    cadena = read_data(sys.stdin)
    sol, b, e = process(cadena)
    show_results(sol, b, e)