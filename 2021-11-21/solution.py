class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def is_palindrome(node):
	s=[]
	p1, p2 = node, node
	while p2!=None and p2.next!=None:
		s.append(p1.value)
		p1 = p1.next
		p2 = p2.next.next
	if p2!=None:
		p1 = p1.next
	
	while len(s)>0:
		if s[-1]!=p1.value: return False
		p1 = p1.next
		del s[-1]
	return True

node = Node('a', Node('b', Node('b', Node('a'))))
print(is_palindrome(node))