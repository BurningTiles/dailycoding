class Node():
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def sum_rec(n, d):
	if n==None: return 0
	ans = n.value + sum_rec(n.left, d) + sum_rec(n.right, d)
	if ans in d:
		d[ans] += 1
	else:
		d[ans] = 1
	return ans

def most_freq_subtree_sum(n):
	d = dict()
	sum_rec(n, d)
	ans, max_freq = [], 0
	for key, value in d.items():
		if value>max_freq:
			max_freq = value
			ans = [key]
		elif value==max_freq:
			ans.append(key)
	return ans

n = Node(3, Node(1), Node(-3))
print(most_freq_subtree_sum(n))

n = Node(5, Node(2), Node(-3))
print(most_freq_subtree_sum(n))