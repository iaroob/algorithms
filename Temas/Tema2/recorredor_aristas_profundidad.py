from typing import *
from algoritmia.datastructures.digraphs import Digraph
Vertex = TypeVar('Vertex')
Edge = Tuple[Vertex, Vertex]

def recorredor_aristas_profundidad(grafo: Digraph, v_inicial: Vertex) -> List[Edge]:
	def recorrido_desde(u,v):
		seen.add(v)
		aristas.append((u,v))
		for suc in grafo.succs(v):
			if suc not in seen:
				recorrido_desde(v,suc)

	aristas = []
	seen = set()
	recorrido_desde(v_inicial, v_inicial)
	return aristas			