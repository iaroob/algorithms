import sys
from typing import Iterator

def read_data(f):
	lines = f.readlines()
	return [int(line) for line in lines]

def process(n):
	res = []
	todos = almost_squares()
	for i in range(n[0]):
		res.append(next(todos))
	return res

def show_results(l):
	for elem in l:
		print(elem)

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

def squares1():
	n = 1
	while True:
		res = (n*n)+1
		yield res
		n+=1

def almost_squares():
	p = iter(primos())
	s = iter(squares1())
	value_p = next(p)
	value_s = next(s)
	while True:
		if (value_p.__eq__(value_s)):
			yield value_p
			value_p = next(p)
			value_s = next(s)
		else:
			if (value_p.__lt__(value_s)):
				value_p = next(p)
			else:
				value_s = next(s)


if __name__ == "__main__":
	n = read_data(sys.stdin)
	l = process(n)
	show_results(l)
