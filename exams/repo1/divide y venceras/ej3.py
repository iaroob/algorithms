def is_simple(s):
	return len(s)==1
def trivial_solution(s):
	return s
def divide(s):
	return(s[:len(s)//2],s[len(s)//2:])

def combine(l1,l2,valor):
	lista=[]


	l1.sort()
	l2.sort()

	for i in l1:
		for j in l2:
			if i+j==valor:
				lista.append(True)

			elif i+j>valor:
				break
	for s in l1:
		lista.append(s)
	for t in l2:
		lista.append(t)

	return lista


def existe_combinacion(lista,valor):

	if is_simple(lista):
		return trivial_solution(lista)
	else:

		sublistas=divide(lista)
		return combine(existe_combinacion(sublistas[0], valor), existe_combinacion(sublistas[1], valor), valor)





lista=[2,3,5,2,8,6]
combinaciones=existe_combinacion(lista, 8)
print(combinaciones)
for i in combinaciones:

	if i>1:
		pass
	else:
		print("Existe una combinación que da el valor solicitado con la lista que tenemos")
		break
