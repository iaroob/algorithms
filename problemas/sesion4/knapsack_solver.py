import sys
from typing import *
from dataclasses import dataclass
from algoritmia.schemes.bt_scheme import *

Decisions = int										# 0 o 1
Solution = Tuple[int, int, Tuple[Decision, ...]]	# (value, weight, decisions)

def read_data(f) -> Tuple[int, List[int], List[int]]:
	capacity = int(f.readline())
	values = []
	weights = []
	for line in f.readlines():
		value, weight = line.strip().split()
		values.append(int(value))
		weights.append(int(weight))
	return capacity, values, weights

def process(C: int, v: List[int], w: List[int]) -> Solution:
	@dataclass
	class Extra:
		weight: int			# nos hace falta el peso acumulado para saber luego si se pasa del limite o no
		value: int
	class KnapsackDS(ScoredDecisionSequence): 	# scoredDecSeq son puntuadas, igual que las decisionsequence pero con un método mas
		def is_solution(self) -> bool:
			return len(self) == len(v)			# len(self) = O(1)  ||  len(self.decisions()) = O(n)

		def successors(self) -> Iterable["KnapsackDS"]:		# successors devuelve iterador
			n = len(self)
			print("n = ", n)
			if len(self) < len(v):								# if no estoy en hoja
				yield self.add_decision(0, self.extra)	# add_dec devuelve objetos de la clase KnapsackDS
				if self.extra.weight + w[n] <= C:
					weight2 = self.extra.weight + w[n]
					value2 = self.extra.value + v[n]
					print("weight2 y value2 = ", weight2, value2)
					yield self.add_decision(1, Extra(weight2, value2))

		def score(self) -> int:
			return self.extra.value

		def solution(self):
			return self.extra.value, self.extra.weight, self.decisions()

		def state(self) -> State:		# si pesan lo mismo y la lista  de num de decisiones es la misma -> futuro es mismo
			return len(self), self.extra.weight

	initial_ds = KnapsackDS(Extra(0, 0))
	sols = list(bt_max_solve(initial_ds))
	return sols[-1]

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