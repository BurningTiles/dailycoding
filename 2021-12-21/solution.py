class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

	def __repr__(self):
		if not self.next: return f"{self.value}"
		return f"{self.value} {self.next.__repr__()}"

def swap_every_two(n):
	if not n or not n.next: return n
	ans = n.next
	n.next = swap_every_two(n.next.next)
	ans.next = n
	return ans

n = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(swap_every_two(n))