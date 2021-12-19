def is_simple(s):
	return len(s)==1
def tribial_solution(s):
	lista=[]
	lista.append(s[0])
	return lista
def divide(s):
	return (s[:len(s)//2],s[len(s)//2:])
def combine(izquierda, derecha):

	for i in derecha:
		izquierda.append(i)
	return izquierda

def funcion(s):
	if is_simple(s):
		return tribial_solution(s)
	else:
		lista=divide(s)
		return combine(funcion(lista[0]),funcion(lista[1]))
def maximoBeneficio(estudiomercado):
	return(estudiomercado.index(min(funcion(estudiomercado)))+1,estudiomercado.index(max(funcion(estudiomercado)))+1)

mercado=[1034,1234,4523,6543,9387,2345,76523,987,453345,486273,86752,4752]
compra,vende=maximoBeneficio(mercado)
print("Deberiamos comprar el mes={} por {}€ y vender el mes={} por {}€ tendriamos un beneficio de {} €".format(compra,mercado[compra-1],vende,mercado[vende-1],mercado[vende-1]-mercado[compra-1]))