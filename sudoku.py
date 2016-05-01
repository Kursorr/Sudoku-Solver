import os


def show_sudoku(sudoku):
	for i in sudoku:
		print(i)
	print("\n")


def import_sudoku():
	with open("sudoku.txt") as f:
		lines = f.read()

	sudoku = [[character for character in line if not character == " "] for line in lines.split("\n")]

	return sudoku

sudoku = import_sudoku()
show_sudoku(sudoku)


def empty_and_filled_cell():
	empty = 0
	filled = 0
	for x in range(9):
		for y in range(9):
			if sudoku[x][y] == ".":
				empty += 1
			else:
				filled += 1
	print(empty, "empty cell and", filled, "filled cell")


def grid_index(grid, value):
	for i, row in enumerate(grid):
		for j, cell in enumerate(row):
			if cell == value:
				return i, j
	return -1, -1


def can_fill_cell(sudoku, coords, candidate):
	row = sudoku[coords[0]]
	for cell in row:
		if cell == candidate:
			return False

	column = [row[coords[1]] for row in sudoku]
	for cell in column:
		if cell == candidate:
			return False

	square_i, square_j = (coords[0]//3)*3, (coords[1]//3)*3
	square = [sudoku[square_i + x][square_j + y] for x in range(3) for y in range(3)]
	for cell in square:
		if cell == candidate:
			return False

	return True


def solve_next_unsolved(sudoku):
	coords = grid_index(sudoku, '.')

	for candidate in '123456789':
		if can_fill_cell(sudoku, coords, candidate):
			sudoku[coords[0]][coords[1]] = candidate
			show_sudoku(sudoku)
			return True
	return False


def solve(sudoku):
	while solve_next_unsolved(sudoku):
		print('-'*80)


solve(sudoku)
os.system("pause")
