from collections import deque

class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __str__(self):
		nodes = deque([self])
		answer = ''
		while len(nodes):
			node = nodes.popleft()
			if not node:
				continue
			answer += str(node.value) + ", "
			nodes.append(node.left)
			nodes.append(node.right)
		return answer[:-2]

def createBalancedBST(nums, s=0, e=-1):
	if e<0: 
		e=len(nums)-1
	if e==s: 
		return Node(nums[s])
	if e-s==1:
		return Node(nums[e], createBalancedBST(nums, s, e-1))
	mid = (s+e)//2
	return Node(
		nums[mid],
		createBalancedBST(nums, s, mid-1),
		createBalancedBST(nums, mid+1, e)
	)

print(createBalancedBST([1, 2, 3, 4, 5, 6, 7]))