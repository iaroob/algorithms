from typing import *

def cambio2(q: int, values: Tuple[int]) -> Optional[List[int]]:
	# Crear vector de indices para recorrer values de menor valor:
	sorted_indexes = sorted(range(len(values)), key=lambda i: -values[i])
	res = [0] * len(values)

	for i in sorted_indexes:
		res[i] = q//values[i]
		q = q % values[i]
	if q == 0:
		return res
	return None

print(cambio2(6, (1, 2, 5, 10)))     # [1, 0, 1, 0]
print(cambio2(7, (2, 5, 10)))        # [1, 1, 0]
print(cambio2(19, (1, 9, 15)))       # [4, 0, 1] -> Wrong answer
print(cambio2(10, (2, 9, 5)))        # None -> Wrong answer

# Time complexity: O(|v|log|v|)