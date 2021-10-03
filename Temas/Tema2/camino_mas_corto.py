from typing import *
from algoritmia.datastructures.digraphs import UndirectedGraph
from recorredor_aristas_anchura import recorredor_aristas_anchura
from recuperador_camino import recuperador_camino
Vertex = TypeVar('Vertex')
Edge = Tuple[Vertex, Vertex]

def camino_mas_corto(grafo: UndirectedGraph,
					 desde: Vertex,
					 hasta: Vertex) -> List[Vertex]:
	bp = {}
	for u, v in recorredor_aristas_anchura(grafo, desde):
		bp[v] = u
		if v == hasta:
			break
		return recuperador_camino(bp, hasta)