#!/usr/bin/env python3

import sys

def read_data(f):
# Leer del fichero f
	lines = f.readlines()
	return [int(line) for line in lines]

def process(data):
	seen = set([])
	for i in range(len(data)):
		if data[i] in seen:
			return True
		else:
			seen.add(data[i])
	return False

def show_result(result):
	print("No hay repetidos" if not result
		else "Hay repetidos")

if __name__ == "__main__":
	nums = read_data(sys.stdin)
	m = process(nums)
	show_result(m)