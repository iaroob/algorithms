from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo
from typing import *

Vertex = TypeVar('Vertex')
Edge = Tuple[Vertex, Vertex]

def recorredor_anchura_yield(grafo: UndirectedGraph,
							 v_inicial: Vertex)-> Iterator[Edge]:
	queue = Fifo()
	seen= set()
	queue.push((v_inicial, v_inicial))
	seen.add(v_inicial)
	while len(queue)>0:
		u, v = queue.pop()
		yield (u, v)
		for suc in grafo.succs(v):
			if suc not in seen:
				seen.add(suc)
				queue.push((v, suc))