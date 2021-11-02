def findDuplicates(nums):
	count = [0]*(len(nums)+1)
	for num in nums:
		count[num] += 1
	ans = []
	for i in range(len(count)):
		if count[i]>1:
			ans.append(i)
	return ans

print(findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))