def fourSum(nums, target):
	ans, n= [], len(nums)
	nums.sort()
	for i in range(n):
		if i>0 and nums[i]==nums[i-1]:
			continue
		for j in range(i+1,n):
			if j>i+1 and nums[j]==nums[j-1]:
				continue
			left, right, t = j+1, n-1, nums[i]+nums[j]
			while left<right:
				if left>j+1 and nums[left]==nums[left-1]:
					left += 1
					continue
				tmp = t+nums[left]+nums[right]
				if tmp==target:
					ans.append([nums[i], nums[j], nums[left], nums[right]])
					left += 1
				elif tmp<target:
					left += 1
				else:
					right -= 1
	return ans

print(fourSum([1, 1, -1, 0, -2, 1, -1], 0))
print(fourSum([3, 0, 1, -5, 4, 0, -1], 1))
print(fourSum([0, 0, 0, 0, 0], 0))