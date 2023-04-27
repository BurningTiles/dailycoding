def maxNonAdjacentSum(a):
	inc, exc = a[0], 0
	for i in range(1, len(a)):
		tmp = inc if inc>exc else exc
		inc = exc + a[i]
		exc = tmp
	return inc if inc>exc else exc

print(maxNonAdjacentSum([3, 4, 1, 1]))
print(maxNonAdjacentSum([2, 1, 2, 7, 3]))
print(maxNonAdjacentSum([5, 5, 10, 100, 10, 5]))