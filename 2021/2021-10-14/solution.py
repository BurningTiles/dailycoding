def majority_element(nums):
	count = {}
	for n in nums:
		if n in count:
			count[n] += 1
		else:
			count[n] = 1
	for key, value in count.items():
		if value>len(nums)//2:
			return key
	return "No majority element found"

print(majority_element([3, 5, 3, 3, 2, 4, 3]))