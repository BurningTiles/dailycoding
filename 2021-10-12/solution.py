class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def min_depth_bt(root):
	if root==None:
		return 0
	if root.left==None and root.right==None:
		return 1
	ans = int(1e9)
	if root.left!=None:
		ans = min([ans, min_depth_bt(root.left)])
	if root.right!=None:
		ans = min([ans, min_depth_bt(root.right)])
	return ans+1

n = Node(1, Node(2), Node(3, None, Node(4)))
#      1
#     / \
#    2   3
#         \
#          4
print(min_depth_bt(n))

n = Node(1, Node(2, Node(4)), Node(3, Node(5, Node(7), Node(8)), Node(6)))
#       1
#      / \
#     2   3
#    /   / \
#   4   5   6
#      / \
#     7   8
print(min_depth_bt(n))