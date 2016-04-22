import os

value_to_input = "9"

def import_sudoku():
	with open("sudoku.txt") as f:
		lines = f.read()

	sudoku = [[character for character in line if not character == " "] for line in lines.split("\n")]

	return sudoku

sudoku = import_sudoku()
print(sudoku) #fonction variadique


def unsolved_point():
	empty = 0
	find = 0
	for x in range(9):
		for y in range(9):
			if sudoku[x][y] == ".":
				empty += 1
			else:
				find += 1

unsolved_point()


def grid_index(grid, value):
	for i, row in enumerate(grid):
		for j, cell in enumerate(row):
			if cell == value:
				return i, j
	return -1, -1


def can_fill_cell(sudoku, coords):
	row = sudoku[0]

	for cell in row:
		if cell == value_to_input:
			return False

	column = [row[0] for row in sudoku]

	for cell in column:
		if cell == value_to_input:
			return False

	square = [sudoku[x][y] for x in range(3) for y in range(3)]

	for cell in square:
		if cell == value_to_input:
			return False

	return True


def solve_next_unsolved(sudoku):
	coords = grid_index(sudoku, ".")

	if can_fill_cell(sudoku, coords):
		sudoku[coords[0]][coords[0]] = value_to_input

	print(sudoku)


solve_next_unsolved(sudoku)
os.system("pause")
