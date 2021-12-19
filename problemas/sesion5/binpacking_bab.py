import sys
from math import ceil
from dataclasses import dataclass
from typing import *

from algoritmia.schemes.bab_scheme import *

Decision = int
Solution = Tuple[Decision]

def read_data(f) -> Tuple[int, List[int]]:
	C = int(f.readline())
	w = [ int(e) for e in f.readlines() ]
	return C, w

def process(C: int, w: List[int]) -> Solution:
	@dataclass
	class Extra:
		container_weights = Tuple[int, ...]

	class BinPackingBDS(BoundedDecisionSequence):
		#TODO: IMPLEMENTAR - Relajar el problema. Trata los objetos que quedan como si fueran un liquido
		def calculate_opt_bound(self) -> int:
			pass

		#TODO: IMPLEMENTAR - Algoritmo voraz. Completa la solucion parcial actual con "Es el primero en el que quepa"
		def calculate_pes_bound(self) -> int:
			pass

		def is_solution(self) -> bool:
			return len(self) == len(w)

		def successors(self) -> Iterable["BinPackingBDS"]:
			n = len(self)
			if n < len(w):
				# Crea un hijo por cada contenedor existente en el que quepa
				for num_container, container_weight in enumerate(self.extra.container_weights):
					if container_weight + w[n] <= C:
						cw2 = list(self.extra.container_weights) # copia tupla a lista
						cw2[num_container] += w[n]
						yield self.add_decision(num_container, Extra(tuple(cw2)))

				# Crea un hijo con un contenedor nuevo para el objeto nuevo
				num_container = len(self.extra.container_weights)
				yield self.add_decision(num_container, Extra(self.extra.container_weights + (w[n],)))

	ca = (0, )
	initial_ps = BinPackingBDS(Extra(ca))
	return bab_min_solve(initial_ps)
def show_results(solution: Solution):
	for num_contenedor in solution:
		print(num_contenedor)


if __name__ == "__main__":
	capacity, weights = read_data(sys.stdin)
	solution = process(capacity, weights)
	show_results(solution)