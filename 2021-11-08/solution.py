def canPick2(arr):
	if len(arr) < 5: return False
	s = [arr[0]]
	for i in range(1, len(arr)):
		s.append(s[-1]+arr[i])
	left, right = 1, len(arr)-2
	leftSum, rightSum = arr[0], arr[-1]
	while left<right:
		if leftSum==rightSum:
			if s[right-1]-s[left] == leftSum:
				return True
		if leftSum<rightSum:
			leftSum += arr[left]
			left += 1
		else:
			rightSum += arr[right]
			right -= 1
	return False

print(canPick2([2, 4, 5, 3, 3, 9, 2, 2, 2]))
print(canPick2([1, 2, 3, 4, 5]))