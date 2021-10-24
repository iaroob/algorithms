from typing import *
from algoritmia.schemes.bt_scheme import *

def nqueen_solve(n: int) -> Iterable[Solution]:
	class NQueensDS(DecisionSequence):
		def is_solution(self) -> bool:
			return len(self) == n

		def successors(self) -> Iterable["NQueensDS"]:
			res = []
			t = len(self)
			if t < n:
				decisions = self.decisions()
				for row in range(n):
					if row not in decisions and \
							all(r != row and t - j != abs(row - r) for j, r in enumerate(decisions)):
						res.append(self.add_decision(row))
			return res
	initial_ds = NQueensDS()
	return bt_solve(initial_ds)

# How to use the function
n = 4
for sol in nqueen_solve(n):
	print(sol)

