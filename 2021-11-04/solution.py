class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def getLeafs(node, leafs):
	if node==None:
		return
	if node.left==None and node.right==None:
		leafs.append(node.value)
	if node.left!=None:
		getLeafs(node.left, leafs)
	if node.right!=None:
		getLeafs(node.right, leafs)

def leafSimilar(n1, n2):
	l1, l2 = [], []
	getLeafs(n1, l1)
	getLeafs(n2, l2)
	if len(l1)==len(l2):
		for i in range(len(l1)):
			if l1[i]!=l2[i]:
				return False
		return True
	return False

#     3
#    / \ 
#   5   1
#  / \
# 6   2 
t1 = Node(3, Node(5, Node(6), Node(2)), Node(1))

#     7
#    / \ 
#   2   1
#  / \
# 6   2 
t2 = Node(7, Node(2, Node(6), Node(2)), Node(1))


print(leafSimilar(t1, t2))