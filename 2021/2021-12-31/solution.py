class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def maxAncestorDiff(n, mn=int(1e10), mx=0):
	if not n: return mx-mn
	mn = min(mn, n.value)
	mx = max(mx, n.value)
	return max(
		maxAncestorDiff(n.left, mn, mx),
		maxAncestorDiff(n.right, mn, mx)
	)

n = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, None, Node(14, Node(13))))
print(maxAncestorDiff(n))