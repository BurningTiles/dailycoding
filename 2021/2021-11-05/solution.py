class Node(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
	def __str__(self):
		return f"{self.val}, ({self.left}, {self.right})"

def sortedArrayToBST(nums, s=0, e=-1):
	if e<0: 
		e=len(nums)-1
	if e==s: 
		return Node(nums[s])
	if e-s==1:
		return Node(nums[e], sortedArrayToBST(nums, s, e-1))
	mid = (s+e)//2
	return Node(
		nums[mid],
		sortedArrayToBST(nums, s, mid-1),
		sortedArrayToBST(nums, mid+1, e)
	)

n = sortedArrayToBST([-10, -3, 0, 5, 9])
print(n)