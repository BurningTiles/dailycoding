def reshape_matrix(m, x, y):
	if x*y!=len(m)*len(m[0]):
		return None

	tmp, ans, ptr= [x for row in m for x in row], [], 0

	for i in range(y):
		row = []
		for j in range(x):
			row.append(tmp[ptr])
			ptr += 1
		ans.append(row)

	return ans
	
print(reshape_matrix([[1, 2], [3, 4]], 1, 4))
print(reshape_matrix([[1, 2], [3, 4]], 2, 3))