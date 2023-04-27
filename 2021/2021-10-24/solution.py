def findKthLargest(arr, k):
	return sorted(arr)[len(arr)-k]

print(findKthLargest([8, 7, 2, 3, 4, 1, 5, 6, 9, 0], 3))