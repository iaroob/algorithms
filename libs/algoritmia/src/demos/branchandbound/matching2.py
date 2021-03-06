#coding: latin1

#< full
from algoritmia.problems.matching import MatchingAsBranchAndBoundProblem2
from algoritmia.schemes.branchandbound import BranchAndBoundSolver
from algoritmia.datastructures.prioritydicts import MinHeapMap

c = [[3, 1, 2, 1], [3, 3, 4, 2], [2, 1, 1, 1], [4, 2, 4, 3]]
problem = MatchingAsBranchAndBoundProblem2(c)
x, cost = BranchAndBoundSolver(problem, lambda keyvalues: MinHeapMap(keyvalues)).solve()
print('Las piezas se ensamblan en el orden', x, 'con coste', cost)
#> full
