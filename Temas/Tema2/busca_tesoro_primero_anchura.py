from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo
from typing import *

Vertex = Tuple[int, int]
pasillos = [((0,0),(0,1)), ((0,2),(0,3)), ((1,0),(1,1)), ((1,1),(1,2)),
			((2,0),(2,1)), ((2,1),(2,2)), ((2,2),(2,3)), ((0,1),(1,1)),
			((0,2),(1,2)), ((0,3),(1,3)), ((1,1),(2,1)), ((1,2),(2,2))]
laberinto = UndirectedGraph(E=pasillos)

v_inicio = (0,0)
v_tesoro = (1,3)

def busca_tesoro_primero_anchura(lab: UndirectedGraph, v_inicial: Vertex) -> Optional[Vertex]:
	queue = Fifo()
	seen = set()
	queue.push(v_inicial)
	seen.add(v_inicial)
	while len(queue)>0:
		v = queue.pop()
		if v == v_tesoro:
			return v
		for suc in lab.succs(v):
			if suc not in seen:
				seen.add(suc)
				queue.push(suc)
	return None

pos_tesoro_encontrada = busca_tesoro_primero_anchura(laberinto, v_inicio)
if pos_tesoro_encontrada == None:
	print("Tesoro no encontrado")
else:
	print("Tesoro encontrado en la habitación {0}".format(pos_tesoro_encontrada))