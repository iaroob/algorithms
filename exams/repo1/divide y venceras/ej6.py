'''
Created on 27/12/2013

@author: sergio
'''
#apartado a)
def ruso_product(m,n):
	if n==0: return 0
	elif n==1: return m
	elif n>1 and n%2==0: return 2*m*ruso_product(m, n//2)
	elif n>1 and n%2!=1: return m+2*ruso_product(m, n//2)
#apartado b)
#=================================
#temporal f("ruso_product")=C
#espacial O(nlogn)
#=================================
#apartado d)
def ruso_product_iterativo(m,n):
	valor=0
	while n!=0:
		if n==1:
			valor+=m
			n=0
		elif n>1 and n%2==0:
			valor+= 2*m*(n//2)
			n=n//2
		elif n>1 and n%2!=0:
			valor+=m+2*m*(n//2)
			n=n//2
	return valor
#complejidad espacial O(logn)
