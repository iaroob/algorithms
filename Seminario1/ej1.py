from typing import Iterator

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

if __name__ == "__main__":
	n = 10
	todos = primos()
	print(f"Los {n} primeros primos son:")
	for i in range(n):
		print(next(todos))

