from typing import *
from algoritmia.schemes.bt_scheme import *
from dataclasses import dataclass
from algoritmia.datastructures.digraphs import UndirectedGraph

def hamiltoniancycle_solver(graph: UndirectedGraph):
	class HamiltonianCycleDS(DecisionSequence):
		def is_solution(self):
			ds = self.decisions()
			return len(ds) == len(graph.V) and ds[0] in graph.succs(ds[-1])

		def successors(self):
			ds = self.decisions()
			if len(ds) < len(graph.V):
				for v in graph.succs(ds[-1]):
					if v not in ds:
						yield self.add_decision(v)

	v_initial = next(iter(graph.V))
	initial_ds = HamiltonianCycleDS().add_decision(v_initial)
	return bt_solve(initial_ds)

# How to use the function --------------------------------------------------------
G = UndirectedGraph(E=[(0, 2), (0, 3), (0, 9), (1, 3), (1, 4), (1, 8), (2, 3),
					   (2, 5), (3, 4),(3, 6), (4, 7), (5, 6), (5, 8), (6, 7), (6, 8), (6, 9)])

for solution in hamiltoniancycle_solver(G):
	print(solution)
