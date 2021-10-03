from typing import *
from algoritmia.datastructures.digraphs import Digraph
from algoritmia.datastructures.queues import Fifo
Vertex = TypeVar('Vertex')
Edge = Tuple[Vertex, Vertex]

def recorredor_aristas_anchura(grafo: Digraph, v_inicial: Vertex) -> List[Edge]:
	aristas = []
	queue = Fifo()
	seen = set()
	queue.push(v_inicial, v_inicial)
	seen.add(v_inicial)
	while len(queue) > 0:
		u, v = queue.pop()
		aristas.append((u,v))
		for suc in grafo.succs(v):
			if suc not in seen:
				seen.add(suc)
				queue.push((v,suc))
	return aristas

