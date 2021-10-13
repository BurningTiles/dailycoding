class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def target_sum_bst(root, target, cur=0):
	if root==None:
		return cur
	cur += root.value
	ans = False
	if root.left!=None:
		ans = ans or target_sum_bst(root.left, target, cur)
	if root.right!=None:
		ans = ans or target_sum_bst(root.right, target, cur)
	if root.left==None and root.right==None:
		ans = target==cur
	return ans

#      1
#    /   \
#   2     3
#    \     \
#     6     4
n = Node(1, Node(2, None, Node(6)), Node(3, None, Node(4)))

print(target_sum_bst(n, 9))