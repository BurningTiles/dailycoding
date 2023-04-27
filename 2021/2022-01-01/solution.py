class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def maxPathDown(n, mx):
	if not n: return 0
	left = max(0, maxPathDown(n.left, mx))
	right = max(0, maxPathDown(n.right, mx))
	mx[0] = max(mx[0], left+right+n.value)
	return max(left, right)+n.value

def maxPathSum(n):
	mx = [int(-1e9)]
	maxPathDown(n, mx)
	return mx[0]

n = Node(10, Node(2, Node(20), Node(1)), Node(10, None, Node(-25, Node(3), Node(4))))
print(maxPathSum(n))