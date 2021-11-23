class Node():
	def __init__(self, value, next=None, prev=None):
		self.value = value
		self.next = next
		self.prev = prev

def is_palindrome(n):
	l, r = n, n
	while r.next!=None:
		r = r.next
	while l.next!=None:
		if l.value!=r.value:
			return False
		l = l.next
		r = r.prev
	return True

node = Node('a')
node.next = Node('b')
node.next.prev = node
node.next.next = Node('b')
node.next.next.prev = node.next
node.next.next.next = Node('a')
node.next.next.next.prev = node.next.next

print(is_palindrome(node))