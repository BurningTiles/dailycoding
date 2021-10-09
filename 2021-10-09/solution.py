def remove_dups(nums):
	j=1
	for i in range(1,len(nums)):
		if nums[i]!=nums[i-1]:
			nums[j] = nums[i]
			j += 1
	while len(nums)>j:
		del nums[-1]
	return j

nums = [1, 1, 2, 3, 4, 4, 4, 4, 4, 5, 5, 6, 7, 9]
print(remove_dups(nums))
print(nums)

nums = [1, 1, 1, 1, 1, 1]
print(remove_dups(nums))
print(nums)