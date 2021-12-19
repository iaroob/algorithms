'''
Created on 27/12/2013

@author: sergio
'''
#apartado a)

def is_simple(s):
	return len(s)<=1
def trivial_solution(s):
	return s
def divide(s):
	return (s[:len(s)//2],s[len(s)//2:])
def combine(izquierda,derecha):
	for i in derecha:
		izquierda.append(i)

#apartdo b)
#======================================================
#1)
# coste temporal f("divide y venceras")=1+1*(n+1)
# coste espacial O(n.logn)
#2)
#coste temporal f("divide y venceras")=1+1*(n+1)
#Coste espacial O(n)
#======================================================