from typing import *
from algoritmia.datastructures.digraphs import UndirectedGraph
from graph2dviewer import Graph2dViewer

Vertex = Tuple[int, int]
Edge = Tuple[Vertex, Vertex]

def knight_graph(num_rows: int, num_cols: int) -> UndirectedGraph:
	# Creo los vertices
	vertices = [(r, c) for r in range(num_rows) for c in range(num_cols)]

	# Creo las aristas de saltos de caballo válidos
	edges = []
	jumps = [(-2, -1), (-1, -2), (-2, 1), (-1, 2)]  # Solo saltos hacia la parte superior del tablero
	for (r, c) in vertices:
		for (ir, ic) in jumps:
			if (0 <= r + ir < num_rows) and (0 <= c + ic < num_cols):
				edges.append(((r, c), (r + ir, c + ic)))

	# Creo el grafo y lo devuelvo
	return UndirectedGraph(V=vertices, E=edges)

def recorredor_vertices_anchura(graph: UndirectedGraph, v_initial: Vertex) -> List[Vertex]:
	vertices = []
	queue = []
	seen = set()
	queue.append(v_initial)
	seen.add(v_initial)
	while len(queue) > 0:
		v = queue.pop()
		vertices.append(v)
		for suc in graph.succs(v):
			if suc not in seen:
				queue.append(suc)
				seen.add(suc)
	return vertices

if __name__ == '__main__':
	g = knight_graph(8, 8)
	print("Num. vértices alcanzables desde el vértice (0,3):", len(recorredor_vertices_anchura(g, (0, 3))))
	viewer = Graph2dViewer(g, vertexmode=Graph2dViewer.ROW_COL)
	viewer.run()