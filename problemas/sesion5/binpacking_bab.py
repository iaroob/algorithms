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

		def calculate_pes_bound(self) -> int:
			pass

		def is_solution(self) -> bool:
			pass

		def successors(self) -> Iterable["BinPackingBDS"]:
			pass

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