import sys
from typing import *
from dataclasses import dataclass
from algoritmia.schemes.bab_scheme import *
infinity = float('infinity')

# TIPOS DEL PROGRAMA-----------------------------------------
Score = int											# Entero con el valor de la mochila
Decision = int										# Dos posibles decisiones: 0 o 1
Solution = Tuple[Score, Optional[List[Decision]]]

# TIPOS PARA EL DICCIONARIO----------------------------------
SParams = Tuple[int, int]						# Parametros de S: (u: int, n: int)
Mem = Dict[SParams, Score]									# Sin rec. de camino
MemPath = Dict[SParams, Tuple[Score, SParams, Decision]] 	# Con rec. de camino

# Salida: (Capacity, values, weights)
def read_data(f) -> Tuple[int, List[int], List[int]]:
	capacity = int(f.readline())
	v = []
	w = []
	for line in f.readlines():
		vv, ww = line.strip().split()
		v.append(vv)
		w.append(ww)
	return capacity, v, w

def process(impl: int, C: int, v: List[int], w: List[int]) -> Solution:
	if impl == 0:
		return resources_direct(w, v, C)
	elif impl == 1:
		return resources_memo(w, v, C)
	elif impl == 2:
		return resources_memo_path(w, v, C)
	elif impl == 3:
		return resources_iter(w, v, C)
	elif impl == 4:
		return resources_iter_red(w, v, C)

def show_results(value: Score, decisions: Optional[List[Decision]]):
	print(value)
	for d in decisions:
		print(d)

def resources_direct(v: List[List[int]], m: List[int], U: int) -> Solution:
	def S(u: int, n: int) -> Score:
		if n == 0: return 0
		else:
			mejor = -infinity
			for d in range(min(m[n-1], u) + 1):
				mejor = max(mejor, S(u-d, n-1) + v[n-1][d])
			return mejor

	return S(U, len(m)), None

def resources_memo(v: List[List[int]], m: List[int], U: int) -> Solution:
	def S(u: int, n: int) -> Score:
		if n == 0: return 0
		if(u, n) not in mem:
			mem[u, n] = -infinity
			for d in range(min(m[n-1], u) + 1):
				mem[u, n] = max(mem[u, n],
								S(u-d, n-1) + v[n-1][d])
		return mem[u, n]

	mem: Dict[SParams, Score] = {}
	return S(U, len(m)), None

def resources_memo_path(v: List[List[int]], m: List[int], U: int) -> Solution: 		# VERSION EXAMEN--------------
	def S(u: int, n: int) -> Score:					# COSTE ESPACIAL: O(U x N), lo que ocupa la tabla mem
		if n == 0: return 0							# COSTE TEMPORAL: O(U^2 x N)
		if(u, n) not in mem:
			mem[u, n] = (-infinity, (-1, -1) ,1)
			for d in range(min(m[n-1], u) + 1):
				mem[u, n] = max(mem[u, n],
								(S(u-d, n-1) + v[n-1][d], (u-d, n-1), d))
		return mem[u, n][0]

	mem: Dict[SParams, Tuple[Score, SParams, Decision]] = {}
	score = S(U, len(m))
	u, n = U, len(m)
	decisions = []
	while n != 0:					# mientras no sea caso base
		_, (u, n), d = mem[u, n]
		decisions.append(d)
	decisions.reverse()
	return score, decisions

def resources_iter(v: List[List[int]], m: List[int], U: int) -> Solution:
	mem: Dict[SParams, Tuple[Score, SParams, Decision]] = {}
	N = len(v) 	# numero de objetos

	for c in range(0, C + 1):
		mem[c, 0] = (0, (-1, -1), -1)
	for n in range(1, N + 1):
		for c in range(0, C + 1):
			if w[n-1] <= c:
				mem[c, n] = max((mem[c, n-1][0]                , (c, n-1),        0)
								(mem[c-w[n-1], n-1][0] + v[n-1], (c-w[n-1], n-1), 1))
			else:
				mem[c, n] = (mem[c, n - 1][0], (c, n - 1), 0)
		score = mem[c, n][0]  # ???

	c, n = C, len(v)
	decisions = []
	while n != 0:					# mientras no sea caso base
		_, (c, n), d = mem[c, n]
		decisions.append(d)
	decisions.reverse()
	return score, decisions

def resources_iter_red(v: List[List[int]], m: List[int], U: int) -> Solution:
	N = len(v)
	current = [0] * (C + 1)
	previous = [0] * (C + 1)

	for n in range(1, N + 1):
		current, previous = previous, current
		for c in range(0, C + 1):
			if w[n - 1] <= c:
				current[c] = max(previous[c], previous[c - w[n - 1]] + v[n - 1])
			else:
				current[c] = previous[c]
	return current[C], None
#-------------------PROGRAMA PRINCIPAL----------------------------------------------
if __name__ == "__main__":
	if len(sys.argv) == 1:
		implementacion = 0
	else:
		implementacion = int(sys.argv[1])

	u, n, v = read_data(sys.stdin)
	print(u, n, v)
	puntuacion, decisiones = process(implementacion, u, n, v)
	show_results(puntuacion, decisiones)
