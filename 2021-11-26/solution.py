def validate_sudoku(board):
	b = [[[0]*10 for i in range(3)]*3 for i in range(3)]
	for i in range(9):
		r, c=[0]*10, [0]*10
		x = i//3
		for j in range(9):
			y = j//3
			if board[i][j]!=' ':
				if r[board[i][j]]>0 or b[x][y][board[i][j]]>0:
					return False
				r[board[i][j]] += 1
				b[x][y][board[i][j]] += 1
			if board[j][i]!=' ':
				if c[board[j][i]]>0:
					return False
				c[board[j][i]] += 1
	return True

board = [
	[5, ' ', 4, 6, 7, 8, 9, 1, 2],
	[6, ' ', 2, 1, 9, 5, 3, 4, 8],
	[1,   9, 8, 3, 4, 2, 5, 6, 7],
	[8,   5, 9, 7, 6, 1, 4, 2, 3],
	[4,   2, 6, 8, 5, 3, 7, 9, 1],
	[7,   1, 3, 9, 2, 4, 8, 5, 6],
	[9,   6, 1, 5, 3, 7, 2, 8, 4],
	[2,   8, 7, 4, 1, 9, 6, 3, 5],
	[3,   4, 5, 2, 8, 6, 1, 7, 9],
]

print(validate_sudoku(board))