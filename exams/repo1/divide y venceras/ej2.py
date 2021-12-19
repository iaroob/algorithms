def is_simple(s):
	return len(s)==2
def trivial_solution(s):
	lista=[]
	lista.append((s[0],s[1]))
	return lista
def divide(s):
	return (s[:len(s)//2],s[len(s)//2:])

def combine(l1,l2):
	lista=[]
	for i in l1:
		if i not in lista:
			lista.append(i)
		for j in l2:
			if j not in lista:
				lista.append(j)
			if (i[0],j[0]) not in lista:
				lista.append((i[0],j[0]))
			if (i[1],j[0]) not in lista:
				lista.append((i[1],j[0]))
			if (i[0],j[1]) not in lista:
				lista.append((i[0],j[1]))
			if (i[1],j[1]) not in lista:
				lista.append((i[1],j[1]))
	return lista




def calendario(participantes):
	if is_simple(participantes):
		return trivial_solution(participantes)
	else:
		lista=divide(participantes)
		return combine(calendario(lista[0]),calendario(lista[1]))

participantes=['Jorge','Ana','Pablo','Neus','Roberto','Lucia','Sergio','Lydia']
partidos=calendario(participantes)
for i in partidos:
	print (i)
print(len(calendario(participantes)))