def canThreePartsEqualSum(nums):
	if len(nums)<3: return False
	reqSum, curSum, count = 0, 0, 0
	for num in nums:
		reqSum += num
	if reqSum%3>0:
		return False
	reqSum = reqSum//3
	for num in nums:
		curSum += num
		if(curSum == reqSum):
			curSum = 0
			count += 1
		if count==3: return True
	return False

print(canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))