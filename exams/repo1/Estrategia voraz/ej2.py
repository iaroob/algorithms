from math import sqrt
from algoritmia.utils import infinity

def solve1(s):
	solucion=[]
	punto=0
	zonas=len(s)
	while(len(solucion)!= zonas):
		distancia_menor=infinity
		if len(solucion)==0:
			inicial=(0,0)
		else:
			inicial=punto
		for i in s:
			distancia=calcula_distancia(inicial,i)
			if distancia<distancia_menor:
				distancia_menor=distancia
				punto=i
		solucion.append(punto)
		s.remove(punto)
	return solucion



def calcula_distancia(x,y):
	return sqrt(((y[0]-x[0])*(y[0]-x[0]))+((y[1]-x[1])*(y[1]-x[1])))

S=[(1,2),(4,6), (5,7), (3,4)]
print(solve1(S))



#a) el coste de este algoritmo es O(NlogN)
#
#b) En Principio si
#============================================================================================================
print("===============================================================")
def solve2(c:"Ilist<€kilo> compra", v:"Ilist<€kilo> venta",k:"IList<disponibilidad>",K:"capacidad camion"):

	resultado=[]
	resultado=[0]*len(c)
	sorting_permutation = list(reversed(sorted(range(len(c)), key = lambda i: (v[i]-c[i])*k[i])))
	for i in sorting_permutation:

		if K>k[i]:
			resultado[i]=1
			K=K-k[i]
		elif K>0:
			resultado[i]=K/k[i]
			K=K-resultado[i]*k[i]
	return resultado
c=[5,2,7]
v=[7,5,8]
k=[9,2,10]
K=15
print(solve2(c,v,k,K))


#d) no, O(NlogN)
#==================================================================================
print("============================================================================")
def solve3(v:"Ilist<€kilo> venta",k:"IList<disponibilidad>",m:"viajes que puede hacer de recojida"):
	resultado=[0]*len(v)
	sorting_permutation = list(reversed(sorted(range(len(c)), key = lambda i: (v[i]*k[i]))))
	for i in sorting_permutation:
		resultado[i]=1
		m=m-1
		if m<1:
			break

	return resultado

v=[7,5,8]
k=[9,2,10]
m=2
print(solve3(v,k,m))

#f) si, no se me ocurre ningun caso que lo mejore
#g) O(mlogN)