from typing import *
from algoritmia.datastructures.digraphs import Digraph
from algoritmia.datastructures.queues import Fifo

Vertex = TypeVar('Vertex')

def recorredor_vertices_anchura(grafo: Digraph, v_inicial: Vertex) -> List[Vertex]:
	vertices = []
	queue = Fifo()
	seen = set()
	queue.push(v_inicial)
	seen.add(v_inicial)
	while len(queue) > 0:
		v = queue.pop()
		vertices.append(v)
		for suc in grafo.succs(v):
			if suc not in seen:
				seen.add(suc)
				queue.push(suc)
	return vertices