import os


def show_sudoku(sudoku):
	print("-"*25)
	for i in range(9):
		print("|", end=" ")
		for j in range(9):
			print(sudoku[i][j], end=" ")
			if j % 3 == 2:
				print("|", end=" ")
		print()
		if i % 3 == 2:
			print("-"*25, sep="")


def import_sudoku():
	with open("sudoku.txt") as f:
		lines = f.read()

	sudoku = [[character for character in line if not character == " "] for line in lines.split("\n")]

	return sudoku


def grid_index(grid, value):
	for i, row in enumerate(sudoku):
		for j, _ in enumerate(row):
			if sudoku[i][j] == value:
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
	for i in range(3):
		for j in range(3):
			cell = sudoku[square_i + i][square_j + j]
			if cell == candidate:
				return False

	return True


def solve(sudoku):
	coords = grid_index(sudoku, '.')

	if coords == (-1,-1):
		return True

	for candidate in '123456789':
		if can_fill_cell(sudoku, coords, candidate):
			sudoku[coords[0]][coords[1]] = candidate
			if solve(sudoku):
				return True
	sudoku[coords[0]][coords[1]] = '.'

	return False


sudoku = import_sudoku()
show_sudoku(sudoku)

if solve(sudoku):
	show_sudoku(sudoku)
else:
	print("Pas de solution")


os.system("pause")
