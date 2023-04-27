class Node:
	def __init__(self, value, left=None, right=None, parent=None):
		self.value = value
		self.left = left
		self.right = right
		self.parent = parent

	def __repr__(self):
		return f"(Value: {self.value}, Left: {self.left}, Right: {self.right})"

def inorder_successor(n):
	ans = None
	if n.right:
		ans = n.right
		while ans.left: ans = ans.left
	elif n.parent:
		ans = n.parent
		while ans.parent and ans.value<n.value: ans = ans.parent
		if ans.value<n.value: ans = None
	return  ans.value if ans else None

tree = Node(3, Node(2, Node(1)), Node(4, None, Node(5)))
tree.left.parent = tree
tree.right.parent = tree
tree.left.left.parent = tree.left
tree.right.right.parent = tree.right

print(inorder_successor(tree.left))
print(inorder_successor(tree.right))