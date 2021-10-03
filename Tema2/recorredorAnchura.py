from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo
from typing import *

Vertex = TypeVar('Vertex')
Edge = Tuple[Vertex, Vertex]
class RecorredorAnchura:
	def __init__(self, grafo: UndirectedGraph,
				 v_inicial: Vertex):
		self.grafo = grafo
		self.v_inicial = v_inicial
		self.queue = Fifo()
		self.seen = set()
		self.queue.push((v_inicial, v_inicial))
		self.seen.add(v_inicial)

	def __iter__(self):
		return self

	def __next__(self):
		if len(self.queue) == 0:
			raise StopIteration()
		u, v = self.queue.pop()
		for suc in self.grafo.succs(v):
			if suc not in self.seen:
				self.seen.add(suc)
				self.queue.push((v, suc))
		return (u, v)
