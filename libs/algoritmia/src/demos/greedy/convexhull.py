#coding: latin1

#< full
from algoritmia.problems.geometry.convexhull.greedy import ConvexHullFinder

S = [(2.5,2.7),(0,0),(1,.5),(2,-1),(2.2,3.5),(3,3.3),(.5,0),(1.1,1.4),(4,2)]
print('Envolvente:', ConvexHullFinder().find(S))
#> full