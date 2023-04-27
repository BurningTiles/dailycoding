class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right



def findLeftmost(root):
	ans = [0, -1]	
	def helper(n, cur_depth=0):
		if n:
			if cur_depth>ans[1]:
				ans[1] = cur_depth
				ans[0] = n.value
			helper(n.left, cur_depth+1)
			helper(n.right, cur_depth+1)
	helper(root)
	return ans[0]

n = Node(2, Node(1), Node(3))
print(findLeftmost(n))

n = Node(1, Node(2, Node(4)), Node(3, Node(5, Node(7)), Node(6)))
print(findLeftmost(n))