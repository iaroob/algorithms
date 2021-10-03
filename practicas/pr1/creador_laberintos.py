import sys
from random import shuffle
from typing import *
from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet

Vertex = Tuple[int, int]
Edge = Tuple[Vertex, Vertex]

def read_data(f):
	rows = int(f.readLine())
	cols = int(f.readLine())
	return rows, cols

def process(rows: int, cols: int) -> UndirectedGraph:
	# Paso 1
	vertices = [(r, c) for r in range(rows) for c in range(cols)]

	# Paso 2
	mfs = MergeFindSet()
	for v in vertices: mfs.add(v)

	# Paso 3
	edges = []
	for r in range(rows):
		for c in range(cols):
			if r+1 < rows: edges.append( ((r, c), (r+1, c)) )
			if c+1 < cols: edges.append( ((r, c), (r, c+1)) )

	shuffle(edges)

	# Paso 4
	corridors = []

	# Paso 5
	for (u, v) in edges:
		if mfs.find(u) != mfs.find(v):
			corridors.append((u, v))
			mfs.merge(u, v)

	# Paso 6
	return UndirectedGraph(E = corridors)

def show_results(labyrinth: UndirectedGraph):
	print(labyrinth)

# PROGRAMA PRINCIPAL------------------------------------------

if __name__ == "__main__":
	rows, cols = 40, 60
	labyrinth = process(rows, cols)
	# show_results(labyrinth)