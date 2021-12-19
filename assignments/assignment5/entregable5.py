import sys
from typing import *

Score = int                 # El tipo de las puntuaciones
Decision = int              # Un índice de globo
Decisions = List[Decision]  # Lista con los índices de los globos explotados

# ------------------------------------------------------------

# Salida: Una tupla con dos listas de enteros: (alturas de los globos, puntuaciones de los globos)
def read_data(f) -> Tuple[List[int], List[int]]:
    heights = []
    scores = []
    for line in f.readlines():
        height, score = line[:-1].split(' ')
        heights.append(int(height))
        scores.append(int(score))
    return heights, scores

# Salida: Una tupla (puntuación, lista con los índices de los globos explotados)
def process(heights: List[int], scores: List[int]) -> Tuple[Score, Decisions]:
    pass

def show_results(score: int, decisions: List[int]):
    print(score)
    for decision in decisions:
        print(decision, end=' ')

# ------------------------------------------------------------

if __name__ == '__main__':
    g_heights, g_scores = read_data(sys.stdin)
    g_score, g_decisions = process(g_heights, g_scores)
    show_results(g_score, g_decisions)
