class Node(object):
	def __init__(self, val, next=None):
		self.val = val
		self.next = next
	def __str__(self):
		if not self.next:
			return str(self.val)
		return str(self.val) + " " + str(self.next)

def deleteDuplicates(node):
	ans = Node(-1, node)
	prev, cur = ans, node
	while cur!=None:
		while cur.next!=None and prev.next.val == cur.next.val:
			cur = cur.next
		if prev.next == cur:
			prev = prev.next
		else:
			prev.next = cur.next
		cur = cur.next
	return ans.next

n = Node(1, Node(2, Node(3, Node(3, Node(4)))))
print(n)
n = deleteDuplicates(n)
print(n)