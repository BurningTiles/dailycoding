class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def is_bst(n, lower=int(-1e10), upper=int(1e10)):
	if n==None: return True
	return (
		n.value>lower and
		n.value<upper and
		is_bst(n.left, lower, n.value) and
		is_bst(n.right, n.value, upper)
	)

n = Node(5, Node(3, Node(1), Node(4)), Node(7, Node(6)))
print(is_bst(n))