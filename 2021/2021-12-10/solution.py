class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __str__(self):
		# pre-order printing of the tree.
		result = ''
		result += str(self.value) + " "
		if self.left:
			result += str(self.left)
		if self.right:
			result += str(self.right)
		return result

def serialize(root):
	if root==None: return "# "
	return str(root.value) + " " + serialize(root.left) + serialize(root.right)

def deserialize_rec(s):
	if len(s)==0 or s[0]=='#':
		del s[0]
		return None
	n = Node(str(s[0]))
	del s[0]
	n.left = deserialize_rec(s)
	n.right = deserialize_rec(s)
	return n

def deserialize(s):
	return deserialize_rec(s.split())

#     1
#    / \
#   3   4
#  / \   \
# 2   5   7
n = Node(1, Node(3, Node(2), Node(5)), Node(4, None, Node(7)))

print(serialize(n))
print(deserialize('1 3 2 # # 5 # # 4 # 7 # #'))