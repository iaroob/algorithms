from typing import *
import sys

def read_data(f) -> List[int]:
	return [int(line) for line in f.readlines()]

def process_rec(vector: List[int]) -> int:
	def dec_solve(start: int, end: int) -> int:
		ne = end - start
		if ne == 0:
			raise Exception("El vector debe tener al menos un elemento")
		if ne == 1:
			return start
		else:
			half = (start + end) // 2			# decrease: obtener ounto medio y elegir lado
			if vector[half] >= vector[half-1]:
				start = half
			else:
				end = half
			# llamada recursiva sobre el lado elegido
			return dec_solve(start, end)

	if len(vector) == 0:
		raise Exception("El vector debe tener al menos un elemento")
	return dec_solve(0, len(vector))

def process(vector: List[int]) -> int:
	start = 0
	end = len(vector)
	while end - start > 1:		# while not is_simple
		half = (start + end) // 2			# decrease: obtener ounto medio y elegir lado
		if vector[half] >= vector[half-1]:
			start = half
		else:
			end = half
	# return trivial_solution
	return start

def show_results(pos_pico: int):
	if solution is None:
		print("No hay punto fijo")
	else:
		print(solution)

# --------PROGRAMA PRINCIPAL---------------------------------------------
if __name__ == "__main__":
	vector = read_data(sys.stdin)
	solution = process(vector)
	show_results(solution)