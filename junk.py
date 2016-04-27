def unsolved_point():
	empty = 0
	find = 0
	for x in range(9):
		for y in range(9):
			if sudoku[x][y] == ".":
				empty += 1
			else:
				find += 1
