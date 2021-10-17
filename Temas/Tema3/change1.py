from typing import *

def cambio1(q: int, values: Tuple[int]) -> Optional[List[int]]:
	res = []
	for v in values:
		res.append(q//v)
		q = q % v
	if q == 0:
		return res
	return None

print(cambio1(6, (1, 2, 5, 10)))     # [6, 0, 0, 0] -> wrong answer
print(cambio1(7, (2, 5, 10)))        # None -> wrong answer
print(cambio1(19, (1, 9, 15)))       # [19, 0, 0]

# Time complexity: O(|V|)