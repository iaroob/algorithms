import sys
from typing import *

def mientras_quepa(w: List[int], C: int) -> List[int]: # devuelve la tupla con info donde va cada cosa
	nc = 0
	available = C
	sol = []
	for w_i in w:
		if w_i == available:
			nc += 1
			available = C
		sol.append(nc)
		available -= w_i
	return sol

def primero_que_quepa(w: List[int], C: int) -> List[int]:
	sol = []
	free_space = [C] * len(w) # Espacio libre en cada contenedor
	for w_i in w:
		for nc in range(len(w)): # len w = len free_space, nc = numero contenedor
			if w_i <= free_space[nc]: # si cabe
				sol.append(nc)
				free_space[nc] -= w_i
				break
	return sol

def primero_que_quepa_ordenado(w: List[int], C: int) -> List[int]:
	indice_ordenados = sorted(w)							# AÑADIDO
	sol = [-1]*len(w)												# CAMBIA
	free_space = [C] * len(w) 								# Espacio libre en cada contenedor
	for i in indice_ordenados:							# CAMBIA: for i in indices_ordenados
		for nc in range(len(w)): 				# len w = len free_space, nc = numero contenedor
			if w[i] <= free_space[nc]: 			# si cabe
				sol[i] = nc								# CAMBIA
				free_space[nc] -= w[i]
				break
	return sol


def read_data(f) -> Tuple[int, int, List[int]]:
	mode = int(f.readline())
	C = int(f.readline())
	w = [ int(e) for e in f.readlines() ]
	return mode, C, w

def process(mode: int, C: int, w: List[int]) -> List[int]:
	if mode == 0:
		return mientras_quepa(w, C)
	if mode == 1:
		return primero_que_quepa(w, C)
	if mode == 2:
		return primero_que_quepa_ordenado(w, C)
	raise Exception(f'Process: unknown mode {mode}')

def show_results(sol: List[int]):
	for num_contenedor in sol:
		print(num_contenedor)


if __name__ == "__main__":
	mode, capacity, weights = read_data(sys.stdin)
	solution = process(mode, capacity, weights)
	show_results(solution)
