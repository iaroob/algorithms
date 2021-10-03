#!/usr/bin/env python3

import sys

def read_data(f):
# Leer del fichero f
	lines = f.readlines()
	return [int(line) for line in lines]

def process(data):
	d = {}
	for i in range(len(data)):
		if data[i] in d:
			d[data[i]] += 1
		else:
			d[data[i]] = 0

	return d.values()

def show_result(result):
	print(max(result))

if __name__ == "__main__":
	nums = read_data(sys.stdin)
	m = process(nums)
	show_result(m)