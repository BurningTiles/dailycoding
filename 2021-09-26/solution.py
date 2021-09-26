def transpose(mat):
	ans = []
	for i in range(len(mat[0])):
		tmp = []
		for j in range(len(mat)):
			tmp.append(mat[j][i])
		ans.append(tmp)
	return ans

mat = [
	[1, 2, 3],
	[4, 5, 6],
]

print(transpose(mat))