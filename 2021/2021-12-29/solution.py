class Node:
	def __init__(self, value, left=None, right=None, next=None):
		self.value = value
		self.left = left
		self.right = right
		self.next = next
	def __str__(self):
		ans = ""
		cur, next=None, self
		while next:
			cur = next
			next = cur.left
			while cur:
				ans += str(cur.value) + " "
				cur = cur.next
			ans += "# "
		return ans

def connect(root):
	prev, cur = root, None
	while prev:
		cur = prev
		while cur and cur.left:
			cur.left.next = cur.right
			if cur.next:
				cur.right.next = cur.next.left
			cur = cur.next
		prev = prev.left

n = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
connect(n)
print(n)