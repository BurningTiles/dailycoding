def n_queens_helper(n, y, row, col, diag1, diag2):
	if y==n:
		return True
	for x in range(n):
		if col[x] or diag1[x+y] or diag2[x-y+n-1]:
			continue
		col[x] = diag1[x+y] = diag2[x-y+n-1] = True
		if n_queens_helper(n, y+1, row, col, diag1, diag2):
			row[y] = x
			return True
		col[x] = diag1[x+y] = diag2[x-y+n-1] = False
	return False

def n_queens(n):
	a = [0]*n
	col, diag1, diag2 = [False]*n, [False]*(n*2), [False]*(n*2)
	n_queens_helper(n, 0, a, col, diag1, diag2)
	ans = []
	for i in range(n):
		ans.append((i, a[i]))
	return ans

print(n_queens(5))