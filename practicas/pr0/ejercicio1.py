#!/usr/bin/env python3

import sys

def read_data(f):
# Leer del fichero f
	lines = f.readlines()
	return [int(line) for line in lines]


def process(nums):
	m = nums[0]
	for num in nums:
		if num < m:
			m = num
	return m

def show_results(m):
	print(m)

if __name__ == "__main__":
	nums = read_data(sys.stdin)
	m = process(nums)
	show_results(m)