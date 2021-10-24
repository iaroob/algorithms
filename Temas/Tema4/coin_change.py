from typing import *
from algoritmia.schemes.bt_scheme import *
from dataclasses import dataclass

# WITHOUT THE CLASS EXTRA
def coin_change_solve_naif(v: Tuple[int, ...], Q: int):
	def calc(ds: Tuple[int, ...]) -> int:
		return sum(ds[i] * v[i] for i in range(len(ds)))

	class CoinChangeDS(DecisionSequence):
		def is_solution(self) -> bool:
			q = calc(self.decisions())
			return len(self) == len(v) and q == Q

		def successors(self) -> Iterable["CoinChangeDS"]:
			n = len(self)
			if n < len(v):
				q = calc(self.decisions())
				pending = Q - q
				for num_coins in range(pending // v[n] + 1):
					yield self.add_decision(num_coins)

	initial_ds = CoinChangeDS()
	return bt_solve(initial_ds)

# WITH THE CLASS EXTRA
def coin_change_solve(v: Tuple[int, ...], Q: int):
	@dataclass
	class Extra:
		pending: int

	class CoinChangeDS(DecisionSequence):
		def is_solution(self) -> bool:
			return len(self) == len(v) and self.extra.pending == 0

		def successors(self) -> Iterable["CoinChangeDS"]:
			n = len(self)
			if n < len(v):
				for num_coins in range(self.extra.pending // v[n] + 1):
					p2 = self.extra.pending - num_coins * v[n]
					yield self.add_decision(num_coins, Extra(p2))

	initial_ds = CoinChangeDS(Extra(Q))
	return bt_solve(initial_ds)

coins, quantity = (1, 2, 5, 10), 11
for sol in coin_change_solve_naif(coins, quantity):
	print(sol)

for sol in coin_change_solve(coins, quantity):
	print(sol)