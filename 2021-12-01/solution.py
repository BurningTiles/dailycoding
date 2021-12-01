class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

	def __str__(self):
		cur = self
		ans = ""
		while cur!=None:
			ans += str(cur.value) + " "
			cur = cur.next
		return ans

def rotate_list(n, k):
	if k==0 or not n: return n
	i, tmp, ans = 1, n, None
	while i<k and tmp.next:
		i += 1
		tmp = tmp.next
	if not tmp.next and i<=k:
		return rotate_list(n, k%i)
	ans = tmp.next
	tmp.next = None
	tmp = ans
	while tmp.next:
		tmp = tmp.next
	tmp.next = n
	return ans

n = Node(1, Node(2, Node(3, Node(4, Node(5)))))

print(rotate_list(n, 2))