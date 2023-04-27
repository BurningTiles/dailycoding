class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right
	
def print_level_order(n):
	dq = [n]
	while len(dq)>0:
		n = dq[0]
		del dq[0]
		if n==None: continue
		print(n.value, end=" ")
		dq.append(n.left)
		dq.append(n.right)
	print()

n = Node(1, Node(2), Node(3, Node(4), Node(5)))
print_level_order(n)