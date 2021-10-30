class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def findNode(a, b, node):
	q = [a]
	q1 = [b]
	while q:
		tmp = q[0]
		tmp1 = q1[0]
		del q[0]
		del q1[0]
		if tmp==node:
			return tmp1
		if tmp.left!=None:
			q.append(tmp.left)
			q1.append(tmp1.left)
		if tmp.right!=None:
			q.append(tmp.right)
			q1.append(tmp1.right)
	return None

#   1
#  / \
# 2   3
#    / \
#   4*  5
a = Node(1, Node(2), Node(3, Node(4), Node(5)))

b = Node(1, Node(2), Node(3, Node(4), Node(5)))

print(findNode(a, b, a.right.left).value)