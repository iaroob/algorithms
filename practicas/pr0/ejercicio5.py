#!/usr/bin/env python3

import sys

def read_data(f):
# Leer del fichero f
	lines = f.readlines()
	return [int(line) for line in lines]

def process(data):
	repeated = False
	for i in range(len(data)):
		for j in range(i+1, len(data)):
			if data[i] == data[j]:
				repeated = True
				break
	return repeated

def show_result(result):
	print("No hay repetidos" if not result
		else "Hay repetidos")

if __name__ == "__main__":
	nums = read_data(sys.stdin)
	m = process(nums)
	show_result(m)