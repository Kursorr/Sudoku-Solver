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

	# compute position of (upper left corner of) square containing cell at coords `coords`
	square_i, square_j = (coords[0]//3)*3, (coords[1]//3)*3
	# recover all cells in square
	square = [sudoku[square_i + x][square_j + y] for x in range(3) for y in range(3)]
	for cell in square:
		if cell == candidate:
			return False

	return True


def solve_next_unsolved(sudoku, candidate):
	coords = (3,0)
	if can_fill_cell(sudoku, coords, 2):
		sudoku[coords[0]][coords[1]] = candidate
		show_sudoku(sudoku)


solve_next_unsolved(sudoku, "2")
os.system("pause")
