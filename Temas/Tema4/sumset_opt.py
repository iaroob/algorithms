from typing import *
from algoritmia.schemes.bt_scheme import *
from dataclasses import dataclass

def sumset_opt_solver(e: Tuple[int, ...], S: int):
	@dataclass
	class Extra:
		sum: int = 0 	#accumulated sum

	class SumSetDS(ScoredDecisionSequence):
		def is_solution(self) -> bool:
			return len(self) == len(e) and self.extra.sum == S

		def successors(self) -> Iterable["SumSetDS"]:
			if len(self) < len(e):
				yield self.add_decision(0, self.extra)
				if self.extra.sum + e[len(self)] <= S:
					sum = self.extra.sum + e[len(self)]
					yield self.add_decision(1, Extra(sum))

		def state(self) -> State:
			return len(self), self.extra.sum

		def score(self) -> int:
			return sum(self.decisions())

	initial_ds = SumSetDS(Extra())
	return bt_min_solve(initial_ds)

#------------PROGRAMA PINCIPAL---------------------------------------------------------------
elements, target_sum = (640, 777, 276, 224, 737, 677, 893, 87, 422, 30), 1199


sol = list(sumset_opt_solver(elements, target_sum))
if len(sol) > 0:
	print(f'Optimization version	- Best solution: {sol[-1]}')
else:
	print(f'Optimization version	- There is no solution')


