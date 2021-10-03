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

def busca_tesoro_primero_profundidad(lab: UndirectedGraph, v_inicial: Vertex) -> Optional[Vertex]:
	def explorar_desde(v):
		seen.add(v)
		if v == v_tesoro:
			return v
		for suc in lab.succs(v):
			if suc not in seen:
				res = explorar_desde(suc)
				if res != None:
					return res
		#if v == v_tesoro:
		# return v
	seen = set()
	return explorar_desde(v_inicial)

pos_tesoro_encontrada = busca_tesoro_primero_profundidad(laberinto, v_inicio)
if pos_tesoro_encontrada == None:
	print("Tesoro no encontrado")
else:
	print("Tesoro encontrado en la habitación")