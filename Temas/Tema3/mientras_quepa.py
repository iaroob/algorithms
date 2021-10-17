from typing import *

def beneficio(v: List[int], sol: List[float]) -> float:
	return sum(f*v[i] for i, f in enumerate(sol))

def mochila_fraq0(w: List[int], v: List[int], C: int) -> List[float]:
	x = [0] * len(w)
	for i in range(len(w)):
		x[i] = min(1, C / w[i])
		C -= x[i] * w[i]
	return x

v, w, C = [60, 30, 40, 20, 75], [40, 30, 20, 10, 50], 50
sol = mochila_fraq0(w, v, C)
print(sol, beneficio(v, sol))    # [1, 0.33333, 0.0, 0.0, 0.0] 70.0 -> Not optimal answer

# Time complexity: O(n)