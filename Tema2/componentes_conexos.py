import recorredor_vertices_anchura
import recorredor_vertices_profundidad
from typing import *
from algoritmia.datastructures.digraphs import Digraph
from algoritmia.datastructures.digraphs import UndirectedGraph
Vertex = TypeVar('Vertex')
def componentes_conexos(g: UndirectedGraph, recorredor: Callable[[UndirectedGraph, Vertex], List[Vertex]]) -> List[List[Vertex]]:
	vertices_no_visitados = set(g.V)
	resultado = []
	while len(vertices_no_visitados) > 0:
		u = vertices_no_visitados.pop()
		vertices_visitados = recorredor(g, u)
		vertices_no_visitados -= set(vertices_visitados)
		resultado.append(vertices_visitados)
	return resultado


# Programa principal
pasillos = [((0,0), (0,1)), ((0,2),(0,3)), ((1,0),(1,1)), ((2,0),(2,1)), ((2,2),(2,3)),
			((0,1),(1,1)), ((0,2),(1,2)), ((0,3),(1,3)), ((1,2),(2,2))]
laberinto = UndirectedGraph(E=pasillos)
ccs_anchura = componentes_conexos(laberinto, recorredor_vertices_anchura)
ccs_profundidad = componentes_conexos(laberinto, recorredor_vertices_profundidad)