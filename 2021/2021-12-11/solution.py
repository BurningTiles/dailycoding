class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __str__(self):
		# pre-order printing of the tree.
		i, q, ans = 0, [self], []
		while i<len(q):
			tmp = q[i]
			i += 1
			if tmp==None:
				ans.append(None)
				continue
			ans.append(tmp.value)
			if tmp.left==None and tmp.right==None: continue
			q.append(tmp.left)
			q.append(tmp.right)
		if not ans[-1]: del ans[-1]
		return str(ans)

def generateTrees(e, s=1):
	if s>e: return [None]
	ans = []
	for i in range(s, e+1):
		left = generateTrees(i-1, s)
		right = generateTrees(e, i+1)
		for l in left:
			for r in right:
				ans.append(Node(i, l, r))
	return ans

v = generateTrees(3)
for n in v:
	print(n)