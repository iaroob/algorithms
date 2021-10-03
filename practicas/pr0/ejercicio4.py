#!/usr/bin/env python3

import sys

def read_data(f):
# Leer del fichero f
	lines = f.readlines()
	return [int(line) for line in lines]

def average(nums):
	return sum(nums)/len(nums)


def process(nums):
	s = 0
	for num in nums:
		s += (num - average(nums)) ** 2
		res = s/len(nums)
	return res

def show_results(m):
	print(m)

if __name__ == "__main__":
	nums = read_data(sys.stdin)
	m = process(nums)
	show_results(m)