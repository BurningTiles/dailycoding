# Rotate Linked List

### Python
```python
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
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

class Node{
	public:
	int value;
	Node *next;
	Node(int v, Node *n=NULL)
		:value{v}, next{n}{}
};

Node* rotate_list(Node *n, int k){
	if(k==0 || !n) return n;
	int i=1;
	Node *tmp=n, *ans = NULL;
	while(i<k && tmp->next)
		++i, tmp=tmp->next;
	if(!tmp->next && i<=k)
		return rotate_list(n, k%i);
	ans = tmp->next;
	tmp->next = NULL;
	tmp = ans;
	while(tmp->next)
		tmp=tmp->next;
	tmp->next=n;
	return ans;
}

void print(Node *n){
	while(n){
		cout << n->value << " ";
		n = n->next;
	} cout << endl;
}

signed main() {
	Node *n = new Node(1, new Node(2, new Node(3, new Node(4, new Node(5)))));
	print(rotate_list(n, 2));
	return 0;
}
```