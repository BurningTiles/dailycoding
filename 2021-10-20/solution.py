class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __repr__(self):
		return f"({self.value}, {self.left}, {self.right})"

def bst_numbers_sum(root, cur=0):
	ans = 0
	if root!=None:
		cur *= 10
		cur += root.value
		if root.left!=None or root.right!=None:
			if root.left!=None:
				ans += bst_numbers_sum(root.left, cur)
			if root.right!=None:
				ans += bst_numbers_sum(root.right, cur)
		else:
			return cur
	return ans

n = Node(1, Node(2, Node(4), Node(5)), Node(3))
#      1
#    /   \
#   2     3
#  / \
# 4   5

print(bst_numbers_sum(n))
# 262