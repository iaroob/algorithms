from typing import *
from algoritmia.datastructures.digraphs import UndirectedGraph, WeightingFunction
from numpy import argmin

Vertex = TypeVar('Vertex')
Edge = Tuple[Vertex, Vertex]

def prim_dic(g: UndirectedGraph, d: WeightingFunction) -> List[Edge]:
	edges = []
	u: Vertex = next(iter(g.V))
	added: Set[Vertex] = {u}
	in_frontier_from: Dict[Vertex, Vertex] = {}
	for v in g.succs(u):
		in_frontier_from[v] = u
	while len(in_frontier_from) > 0:
		v, u = argmin(in_frontier_from.items(), d)
		del in_frontier_from[v]
		added.add(v)
		edges.append((u, v))
		for w in g.succs(v):
			if w not in added and (w not in in_frontier_from or d(v, w) < d(in_frontier_from[w], w)):
				in_frontier_from[w] = v
	return edges