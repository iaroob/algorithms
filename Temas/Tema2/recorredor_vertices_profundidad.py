from typing import *
from algoritmia.datastructures.digraphs import Digraph
Vertex = TypeVar('Vertex')
Edge = Tuple[Vertex, Vertex]

def recorredor_vertices_profundidad(grafo: Digraph, v_inicial: Vertex) -> List[Edge]:
	def recorrido_desde(v):
		seen.add(v)
		vertices.append(v)
		for suc in grafo.succs(v):
			if suc not in seen:
				recorrido_desde(suc)
	#vertices.append(v) Postorden

	vertices = []
	seen = set()
	recorrido_desde(v_inicial)
	return vertices

