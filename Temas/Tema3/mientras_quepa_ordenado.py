from typing import *

def beneficio(v: List[int], sol: List[float]) -> float:
	return sum(f*v[i] for i, f in enumerate(sol))

def mochila_fraq0(w: List[int], v: List[int], C: int) -> List[float]:
	sorted_indexes = sorted(range(len(w)), key = lambda i: -v[i]/w[i])  # n log n
	x = [0] * len(w)
	for i in sorted_indexes:
		x[i] = min(1, C / w[i])
		C -= x[i] * w[i]
	return x

v, w, C = [60, 30, 40, 20, 75], [40, 30, 20, 10, 50], 50
sol = mochila_fraq0(w, v, C)
print(sol, beneficio(v, sol))    # [0.5, 0.0, 1, 1, 0.0] 90.0 -> Not optimal answer

# Time complexity: O(n log n)