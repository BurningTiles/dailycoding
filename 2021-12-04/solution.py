class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __repr__(self):
		return f"({self.value}, {self.left}, {self.right})"

def bfs(n, ans):
	if n==None: return
	ans.append(n)
	bfs(n.left, ans)
	bfs(n.right, ans)

def flatten_bst(root):
	if n==None: return
	a = []
	bfs(root, a)
	a.append(None)
	for i in range(len(a)-1):
		a[i].left = None
		a[i].right = a[i+1]

n = Node(1, Node(2, Node(5)), Node(3, Node(4)))

flatten_bst(n)
print(n)