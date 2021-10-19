class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __repr__(self):
		return f"({self.value}, {self.left}, {self.right})"

def node_to_list(root, lst):
	if root!=None:
		lst.append(root)
		node_to_list(root.left, lst)
		node_to_list(root.right, lst)

def flatten_bst(root):
	lst = []
	node_to_list(root, lst)
	for i in range(len(lst)-1):
		lst[i].left = None
		lst[i].right = lst[i+1]
	if len(lst)>0:
		lst[-1].left, lst[-1].right = None, None

n = Node(1, Node(2, Node(5)), Node(3, Node(4)))
print("Before:")
print(n)
#      1
#    /   \
#   2     3
#  /     /
# 5     4

flatten_bst(n)
print("After:")
print(n)
# n1 should now look like
#   1
#    \
#     2
#      \
#       5
#        \
#         3
#          \
#           4