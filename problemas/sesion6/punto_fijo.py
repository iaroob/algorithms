from typing import *
import sys

def read_data(f) -> List[int]:
	return [int(line) for line in f.readlines()]

def process_rec(vector: List[int]) -> Optional[int]:
	def dec_solve(start: int, end: int) -> Optional[int]:
		ne = end - start
		if  ne == 0:
			return None
		elif ne == 1:
			return start if vector[start] == start else None
		else:
			half = (start + end) // 2
			if half == vector[half]:
				return half
			elif half < vector[half]:
				end = half
			else:
				start = half + 1
			return dec_solve(start, end)
	return dec_solve(0, len(vector))

def process(vector: List[int]) -> Optional[int]:
	start = 0			# primer elemento
	end = len(vector)	# ultimo - 1 elemento
	while end - start > 1:		# mientras quedan elementos
		half = (start + end) // 2		# punto medio
		if half == vector[half]:		# indice coincide con el elemento medio
			return half
		elif half < vector[half]:		# indice medio menor que el elemento medio
			end = half					# ahora el final es el indice medio, se coge el trozo vector izq
		else:
			start = half + 1			# sino cogemos el vector dcha
	ne = end - start					# actualizar num elementos
	if  ne == 0:						# si el vector queda vacio
		return None
	elif ne == 1:						# si solo queda un elem
		return start if vector[start] == start else None

def show_results(solution: Optional[int]):
	if solution is None:
		print("No hay punto fijo")
	else:
		print(solution)

# --------PROGRAMA PRINCIPAL---------------------------------------------
if __name__ == "__main__":
	vector = read_data(sys.stdin)
	solution = process(vector)
	#solution = process_rec(vector)
	show_results(solution)
