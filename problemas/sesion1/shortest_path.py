from algoritmia.datastructures.digraphs import UndirectedGraph
from typing import *
from labyrinth import create_labyrinth
import sys
from algoritmia.datastructures.queues import Fifo
Vertex = TypeVar('Vertex')
Edge = Tuple[Vertex, Vertex]
Path = List[Edge]

# Recorrido aristas profundidad
def df_search(g: UndirectedGraph,
			  source: Vertex,
			  target: Vertex) -> Path:
	def recorrido_desde(u: Vertex,v: Vertex):
		seen.add(v)
		aristas.append((u,v))
		if v == target: return
		for suc in g.succs(v):
			if suc not in seen:
				recorrido_desde(v,suc)
	aristas = []
	seen = set()
	recorrido_desde(source, source)
	return aristas

# Recuperador de caminos
def recover_path(edges: List[Edge],
				 target: Vertex) -> Path:
	# Crea un dicionario de punteros hacia atrás (backpointers)
	bp = {}
	for orig,dest in edges:
		bp[dest] = orig
	# Reconstruye el camino yendo hacia atrás
	v = target
	camino = [v]
	while v != bp[v]:
		v = bp[v]
		camino.append(v)
	# Invierte el camino pues lo hemos obtenido al revés
	camino.reverse()
	return camino

# Recorrido aristas anchura
def bf_search(g: UndirectedGraph,
			  source: Vertex,
			  target: Vertex) -> List[Edge]:
	aristas = []
	queue = Fifo()
	seen = set()
	queue.push(source, source)
	seen.add(source)
	while len(queue) > 0:
		u, v = queue.pop()
		aristas.append((u,v))
		if v == target: return aristas
		for suc in g.succs(v):
			if suc not in seen:
				seen.add(suc)
				queue.push((v,suc))
	return aristas

def read_data(f):
	rows = int(f.readline())
	cols = int(f.readline())
	return rows, cols

def process(rows: int, cols: int) -> Tuple[UndirectedGraph, Path]:
	g = create_labyrinth(rows, cols)
	la = df_search(g, (0, 0), (rows - 1, cols - 1))
	path = recover_path(la, (rows - 1, cols - 1))
	return g, path

def show_results(path: Path):
	for v in path:
		print(v)
							# Se hace para usar shortest path como módulo importado.
if __name__ == "__main__":  # Si se utiliza este fichero como modulo no se ejecuta el main de este fichero
	rows, cols = 40, 60
	g, path = process(rows, cols)
	show_results(path)