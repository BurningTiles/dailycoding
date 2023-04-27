from collections import deque

class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def zigzag_order(n):
	dq = deque()
	dq.append(n)
	ans = []
	rev, s, e = False, 0, 1
	while len(dq)>0:
		tmp = dq.popleft()
		ans.append(tmp.value)
		if tmp.left: dq.append(tmp.left)
		if tmp.right: dq.append(tmp.right)
		if e==len(ans):
			if rev:
				ans[s:] = ans[s:][::-1]
			rev = not rev
			s = e
			e = s+len(dq)
	return ans

n = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
print(zigzag_order(n))