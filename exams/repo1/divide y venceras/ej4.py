def is_simple(s):
	return len(s)==2
def trivial_solution(s):
	s.sort
	return s

def divide(s):
	return (s[:len(s)//2],s[len(s)//2:])
def combine(izquierda,derecha):

	lista=izquierda
	for i in derecha:
		lista.append(i)
	lista.sort()
	return lista

def funcion(s):
	if is_simple(s):
		return trivial_solution(s)
	else:
		lista=divide(s)
		return combine(funcion(lista[0]),funcion(lista[1]))
def mediana(a,b):
	for i in b:
		a.append(i)
	parcial=funcion(a)
	return parcial//2


a=[1,2,3,4]
b=[5,3,7,8]
l=[]