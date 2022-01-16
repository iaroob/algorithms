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
		def is_solution(self) -> bool:			# el Sudoku no tiene ninguna casila vacia
			return primera_vacia(self.extra.sudoku) is None

		def solution(self) -> Solution:			# devuelve el sudoku
			return self.extra.sudoku

		def successors(self) -> Iterable["SudokuDS"]:
			pos = primera_vacia(self.extra.sudoku)		# coger la primera pos vacia que se encuentre
			if pos is not None:							# si SI que hay posicion vacia
				for num in posibles_en(self.extra.sudoku, pos):		# posibles_en sirve para saber los numeros que se pueden poner en pos
					sudoku2 = deepcopy(self.extra.sudoku)			# se hace una copia
					r, c = pos
					sudoku2[r][c] = num					# colocar ese num en la pos vacia
					yield self.add_decision(num, Extra(sudoku2))		# añadir la decision

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
