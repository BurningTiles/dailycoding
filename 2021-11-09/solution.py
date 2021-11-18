class Node:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def inorder(node):
	if node!=None:
		inorder(node.left)
		print(node.val, end=" ")
		inorder(node.right)

def inorder_iterative(node):
	s = []
	cur = node
	while cur!=None or len(s)>0:
		while cur!=None:
			s.append(cur)
			cur = cur.left
		cur = s[-1]
		del s[-1]
		print(cur.val, end=" ")
		cur = cur.right

n = Node(12, Node(6, Node(2), Node(3)), Node(4, Node(7), Node(8)))

inorder(n)
print()
inorder_iterative(n)