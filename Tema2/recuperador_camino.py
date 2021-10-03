from typing import *
from algoritmia.datastructures.digraphs import UndirectedGraph
import recorredor_aristas_anchura
Vertex = TypeVar('Vertex')
Edge = Tuple[Vertex, Vertex]

def recuperador_camino(lista_aristas: List[Edge], v: Vertex) -> List[Vertex]:
	# Crea un dicionario de punteros hacia atrás (backpointers)
	bp = {}
	for orig,dest in lista_aristas:
		bp[dest] = orig
	# Reconstruye el camino yendo hacia atrás
	camino = []
	camino.append(v)
	while v != bp[v]:
		v = bp[v]
		camino.append(v)
	# Invierte el camino pues lo hemos obtenido al revés
	camino.reverse()
	return camino

# PROGRAMA PRINCIPAL
pasillos = [((0,0), (0,1)), ((0,2),(0,3)), ((1,0),(1,1)), ((1,1),(1,2)),
			((2,0),(2,1)), ((2,1),(2,2)), ((2,2),(2,3)), ((0,1), (1,1)),
			((0,2),(1,2)), ((0,3),(1,3)), ((1,1),(2,1)), ((1,2),(2,2))]
laberinto = UndirectedGraph(E=pasillos)
v_inicio = (0,0)
v_tesoro = (1,3)
a = recorredor_aristas_anchura(laberinto, v_inicio) # Traspa 14 --------
print(recuperador_camino(a, v_tesoro))