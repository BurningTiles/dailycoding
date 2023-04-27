# Swap Every Two Nodes in a Linked List

### Python
```python
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

void print(Node *n){
	while(n){
		cout << n->value << " ";
		n = n->next;
	}
	cout << endl;
}

// Recursive solution
Node* swap_rec(Node *n){
	if(!n or !n->next) return n;
	Node *ans = n->next;
	n->next = swap_rec(n->next->next);
	ans->next = n;
	return ans;
}

// Iterative solution
Node* swap_every_two(Node *n){
	if(!n or !n->next) return n;
	Node *ptr=n, *tmp, *ans, *prev=NULL;
	while(ptr && ptr->next){
		if(prev) prev->next = ptr->next;
		else prev=ptr, ans=ptr->next;
		tmp = ptr->next;
		ptr->next = ptr->next->next;
		tmp->next = ptr;
		prev = ptr;
		ptr = ptr->next;
	}
	return ans;
}

signed main() {
	Node *n = new Node(1, new Node(2, new Node(3, new Node(4, new Node(5)))));
	print(swap_every_two(n));
	return 0;
}
```