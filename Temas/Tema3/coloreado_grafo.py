from algoritmia.datastructures.digraphs import UndirectedGraph
from typing import *
def colorea(G: UndirectedGraph) -> List[Set[int]]:
	V = set(G.V) # Creamos una copia de vertices
	res = [] # Lista con los grupos de vertices del mismo color
	while len(V) > 0:
		grupo = set() # creamos un nuevo grupo vacio
		for v in V:
			if all(v not in G.succs(u) for u in grupo):
				grupo.add(v) # Añadimos los vertices cuyos sucesores no esten ya en grupo
		V -= grupo # Quitamos los verices del grupo de V ( resta de conjuntos )
		res.append(grupo)
	return res

G = UndirectedGraph(E=[(0,1), (0,2), (0,3), (1,3), (1,4), (2,3), (2,5), (3,4),
						(3,5), (3,6), (4,7), (5,6), (5,8), (6,7),(6,8), (6,9), (7,9), (8,9)])
print(colorea(G)) # [{0, 9, 4, 5}, {1, 2, 6}, {8, 3, 7}]

