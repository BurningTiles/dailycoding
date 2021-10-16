def searchMatrix(mat, val):
	m, n = len(mat), len(mat[0])
	left, right = 0, m*n-1
	while left<=right:
		mid = (left+right)//2
		tmp = mat[mid//n][mid%n]
		if tmp==val:
			return True
		elif val>tmp:
			left = mid+1
		else:
			right = mid-1
	return False

mat = [
	[1, 3, 5, 8],
	[10, 11, 15, 16],
	[24, 27, 30, 31],
]

print(searchMatrix(mat, 4))
print(searchMatrix(mat, 10))