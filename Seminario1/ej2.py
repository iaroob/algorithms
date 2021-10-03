from typing import Iterator
from typing import Iterable

def es_primo(n: int):
	if n < 2:
		return False
	if n == 2:
		return True
	else:
		for i in range(2, n):
			if n % i == 0:
				return False
		return True

def primos() -> Iterator[int]:
	p = 2
	while True:
		if es_primo(p):
			yield p
		p += 1

def take(n: int, it: Iterable[int]) -> Iterator[int]:
	res = []
	for i in range(n):
		res.append(next(it))
	return res

print(list(take(10, primos())))
