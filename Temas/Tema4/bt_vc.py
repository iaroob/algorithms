from typing import *
from algoritmia.schemes.bt_scheme import *

def bt_vc_solve(initial_ds: DecisionSequence) -> Iterable[Solution]:
	def bt(ds: DecisionSequence) -> Iterable[Solution]:
		seen.add(ds.state())
		if ds.is_solution():
			yield ds.solution()
		for new_ds in ds.successors():
			state = new_ds.state()
			if state not in seen:
				yield from bt(new_ds)

	seen = set()
	return bt(initial_ds)