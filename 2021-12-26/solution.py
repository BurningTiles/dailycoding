class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def isValid(t, s):
	if t and s:
		return (t.value==s.value and 
			isValid(t.left, s.left) and
			isValid(t.right, s.right))
	if not t and not s: return True
	return False

def find_subtree(t, s):
	if t and s:
		if t.value==s.value and isValid(t, s):
			return True
		return find_subtree(t.left, s) or find_subtree(t.right, s)
	return t==s

t = Node(1, Node(4, Node(3), Node(2)), Node(5, Node(4), Node(-1)))
s = Node(4, Node(3), Node(2))

print(find_subtree(t, s))