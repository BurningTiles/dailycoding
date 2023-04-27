def helper(nums, ans, cur=[], n=0):
	if n==len(nums): 
		ans.append(cur[:])
		return
	helper(nums, ans, cur, n+1)
	cur.append(nums[n])
	helper(nums, ans, cur, n+1)
	del cur[-1]

def generateAllSubsets(nums):
	ans=[]
	helper(nums, ans)
	return ans

print(generateAllSubsets([1, 2, 3]))