def rotate(m):
	rows= len(m)
	for i in range(rows):
		for j in range(i):
			m[i][j], m[j][i] = m[j][i], m[i][j]
	for i in range(rows):
		m[i] = m[i][::-1]
	return m

m = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]]
print(rotate(m))