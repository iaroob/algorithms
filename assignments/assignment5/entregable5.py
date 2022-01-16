import sys
from typing import *

infinity = float("infinity")

Score = int                 # El tipo de las puntuaciones
Decision = int              # Un índice de globo
Decisions = List[Decision]  # Lista con los índices de los globos explotados
SParams = Tuple[int, int]

# ------------------------------------------------------------

# Salida: Una tupla con dos listas de enteros: (alturas de los globos, puntuaciones de los globos)
def read_data(f) -> Tuple[List[int], List[int]]:
	alturas = []
	puntuaciones = []
	for line in f.readlines():
		line = line.split()
		alturas.append(int(line[0]))
		puntuaciones.append(int(line[1]))
	return alturas, puntuaciones


# Salida: Una tupla (puntuación, lista con los índices de los globos explotados)
def process(heights: List[int], scores: List[int]) -> Tuple[Score, Decisions]:
	def S(h: int, n: int) -> Score:
		if n == 0: return 0                                 #h, n son la altura donde nos encontramos y el número de globos (restantes) respectivamente
		if (h, n) not in mem:
			mem[h, n] = -infinity, (-1, -1), -1
			if n > 0 and h > heights[n - 1]:                #si el globo anterior estaba más bajo, el globo donde estamos no se podría coger
				mem[h, n] = (S(h, n - 1), (h, n - 1), -1)
			elif n > 0 and h <= heights[n - 1]:             #si el globo anterior estaba más alto, el de ahora sí se podría coger
				mem[h, n] = max((S(h, n - 1), (h, n - 1), -1),
								(S(heights[n - 1], n - 1) + scores[n - 1], (heights[n - 1], n - 1), n - 1))
		return mem[h, n][0]
	mem: Dict[SParams, Tuple[Score, SParams, Decision]] = {}
	score = S(0, len(heights))
	h, n = 0, len(heights)
	solution = []  # Solution = List[Decision]; Decision = int
	while n != 0:
		_, (h_p, n_p), d = mem[h, n]
		if d != -1:
			solution.append(d)
		h = h_p
		n = n_p
	solution.reverse()
	return score, solution


def show_results(score: int, decisions: List[int]):
	print(score)
	sol = ""
	for d in decisions:
		sol = sol + str(d) + " "
	print(sol)

# ------------------------------------------------------------

if __name__ == '__main__':
	g_heights, g_scores = read_data(sys.stdin)
	g_score, g_decisions = process(g_heights, g_scores)
	show_results(g_score, g_decisions)
