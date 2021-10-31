from typing import *
from algoritmia.schemes.bt_scheme import *
from dataclasses import dataclass

def sumset_vc_solver(e: Tuple[int, ...], S: int):
	@dataclass
	class Extra:
		sum: int = 0 	#accumulated sum

	class SumSetDS(DecisionSequence):
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

	initial_ds = SumSetDS(Extra())
	return bt_vc_solve(initial_ds)

#------------PROGRAMA PINCIPAL---------------------------------------------------------------
elements, target_sum = (640, 777, 276, 224, 737, 677, 893, 87, 422, 30), 1199

try:
	sol = next(sumset_vc_solver(elements, target_sum))
	print(f'Visited control version	- First solution: {sol}')
except StopIteration:
		print(f'Visited control version	- There is no solution')