import sys
from typing import *
from dataclasses import dataclass
from algoritmia.schemes.bab_scheme import *
Decisions = int										# 0 o 1
Solution = Tuple[int, int, Tuple[Decision, ...]]	# (value, weight, decisions)

def read_data(f) -> Tuple[int, List[int], List[int]]:
	capacity = int(f.readline())
	v = []
	w = []
	for line in f.readlines():
		vv, ww = line.strip().split()
		v.append(vv)
		w.append(ww)
	return capacity, v, w

def process(C: int, v: List[int], w: List[int]) -> Solution:
	@dataclass
	class Extra:
		weight: int			# nos hace falta el peso acumulado para saber luego si se pasa del limite o no
		value: int
	class KnapsackBDS(BoundedDecisionSequence):
		#TODO: Toma las decisiones que quedan como si fuera la mochila continua
		def calculate_opt_bound(self) -> int:		# Las cotas optimistas son relajar alguna condición de la pesimista. Relajamos la segunda condicion, los objetos si que se pueden romper
			value2 = self.extra.value
			weight2 = self.extra.weight
			for i in range(len(self), len(w)):
				if weight2 + w[i] <= C:			# Si cabe
					value2 += v[i]
					weight2 += w[i]
				else: 							# Si no cabe
					capacidad_libre = C + weight2
					value2 += (v[i]/w[i]) * capacidad_libre
					break
			return value2

		#TODO: Toma las decisiones que quedan mirando solo que la mochila no se pase de peso
		def calculate_pes_bound(self) -> int:
			return self.extra.value + 0

		def solution(self):
			return self.extra.value, self.extra.weight, self.decisions()

		def is_solution(self) -> bool:
			return len(self) == len(v)

		def successors(self) -> Iterable["KnapsackBDS"]:
			n = len(self)
			if n < len(v):
				yield self.add_decision(0, self.extra)
				if self.extra.weight + w[n] <= C:
					weight2 = self.extra.weight + w[n]
					value2 = self.extra.value + v[n]
					yield self.add_decision(1, Extra(weight2, value2))


	initial_ps = KnapsackBDS(Extra(0, 0))
	return bab_max_solve(initial_ps)		# bab_max_solve devuelve las decisiones solo


def show_results(value: int, weight: int, decisions: Tuple[Decision, ...]):
	print(value)
	print(weight)
	for d in decisions:
		print(d)

#-------------------- PROGRAMA PRINCIPAL ----------------------------------

if __name__ == "__main__":
	my_C, my_v, my_w = read_data(sys.stdin)
	my_value, my_weight, my_decisions = process(my_C, my_v, my_w)
	show_results(my_value, my_weight, my_decisions)

# Problema de maximización