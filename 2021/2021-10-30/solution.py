class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def findNode(a, b, node):
	if a==None or b==None:
		return None
	if a == node:
		return b
	ans = findNode(a.left, b.left, node)
	return ans if ans!=None else findNode(a.right, b.right, node)

#   1
#  / \
# 2   3
#    / \
#   4*  5
a = Node(1, Node(2), Node(3, Node(4), Node(5)))

b = Node(1, Node(2), Node(3, Node(4), Node(5)))

print(findNode(a, b, a.right.left).value)