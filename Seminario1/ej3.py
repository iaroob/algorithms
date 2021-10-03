def squares1():
	n = 1
	while True:
		res = (n*n)+1
		yield res
		n+=1

if __name__ == "__main__":
	n = 10
	todos = squares1()
	for i in range(n):
		print(next(todos))