from typing import *
from algoritmia.schemes.bt_scheme import *

def bt_min_solve(initial_ds: DecisionSequence) -> Iterable[Solution]:
	def bt(ds: DecisionSequence) -> Iterable[Solution]:
		nonlocal bs
		ds_score = ds.score()
		best_seen[ds.state()] = ds_score
		if ds.is_solution() and ds_score < bs:
			bs = ds_score
			yield ds.solution()
		for new_ds in ds.successors():
			st = new_ds.state()
			if new_ds.score() < best_seen.get(st, infinity):
				yield from bt(new_ds)
	best_seen = {}
	bs = infinity
	return bt(initial_ds)