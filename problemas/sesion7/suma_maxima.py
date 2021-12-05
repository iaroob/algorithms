from typing import *
import sys

def read_data(f) -> List[int]:
	return [int(line) for line in f.readlines()]

def process_rec(vector: List[int]) -> Tuple[int, int, int]:
	def div_solve(start: int, end: int) -> Tuple[int, int, int]:
		# if is_simple:
			# return trivial_solution
		# else:
			# divide y el combine (dos llamadas recursivas)
			# devolver la solucion (suma, b, e) return (..., ..., ...)
			# Coste: O(n) porque cada for se hace n/2 veces

		ne = end - start
		if ne == 1:
			return vector[start], start, start + 1
		else:
			half = (start + end) // 2
			best_left = div_solve(start, half)
			best_right = div_solve(half, end)

			best_right_sum = vector[half]
			best_right_index = half
			acu = vector[half]
			for i in range(half, end):
				acu += vector[i]
				if acu > best_right_sum:
					best_right_sum = acu
					best_right_index = i

			best_left_sum = vector[half-1]
			best_left_index = half - 1
			acu = vector[half-1]
			for i in range(half - 2, start - 1, -1):		# el range va al revés
				acu += vector[i]
				if acu > best_left_sum:
					best_left_sum = acu
					best_left_index = i

			best_center = (best_right_sum + best_left_sum, best_left_index, best_right_index + 1)

			return max(best_left, best_right, best_center) 	# el primer elemento de las tuplas ya es la suma

	return div_solve(0, len(vector))

def show_results(suma: int, b: int, e: int):
	print(suma)
	print(b)
	print(e)

# --------PROGRAMA PRINCIPAL---------------------------------------------
if __name__ == "__main__":
	vector = read_data(sys.stdin)
	suma, b, e = process_rec(vector)
	show_results(suma, b, e)