import sys
from typing import *
from sudoku import *
from copy import deepcopy
from dataclasses import dataclass
from algoritmia.schemes.bt_scheme import bt_solve, DecisionSequence
Solution = Sudoku



def read_data(f) -> Sudoku:
	return desde_cadenas(f.readlines())

def process(sudoku: Sudoku) -> Iterable[Sudoku]:
	@dataclass
	class Extra:
		sudoku: Sudoku

	class SudokuDS(DecisionSequence):
		def is_solution(self) -> bool:
			return primera_vacia(self.extra.sudoku) is None

		def solution(self) -> Solution:
			return self.extra.sudoku

		def successors(self) -> Iterable["SudokuDS"]:
			pos = primera_vacia(self.extra.sudoku)
			if pos is not None:
				for num in posibles_en(self.extra.sudoku, pos):
					sudoku2 = deepcopy(self.extra.sudoku)
					r, c = pos
					sudoku2[r][c] = num
					yield self.add_decision(num, Extra(sudoku2))

	initial_ds = SudokuDS(Extra(sudoku))
	return bt_solve(initial_ds)

def show_results(solutions: Iterable[Sudoku]):
	for solution in solutions:
		pretty_print(solution)
	print("<END>")




#-------------------- PROGRAMA PRINCIPAL ----------------------------------

if __name__ == "__main__":
	sudoku = read_data(sys.stdin)
	solutions = process(sudoku)
	show_results(solutions)
