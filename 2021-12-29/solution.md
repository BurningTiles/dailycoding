# Populating Next Right Pointers in Each Node

### Python
```python
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
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

class Node{
	public:
	int value;
	Node *left, *right, *next;
	Node(int v, Node *l=NULL, Node *r=NULL, Node *n=NULL)
		:value{v}, left{l}, right{r}, next{n} {}
};

void connect(Node *root){
	Node *prev=root, *cur;
	while(prev){
		cur = prev;
		while(cur and cur->left){
			cur->left->next = cur->right;
			if(cur->next) cur->right->next = cur->next->left;
			cur = cur->next;
		}
		prev = prev->left;
	}
}

void print(Node *n){
	Node *cur, *next=n;
	while(next) {
		cur = next, next = cur->left;
		while(cur)
			cout << cur->value << " ", cur = cur->next;
		cout << "# ";
	}
	cout << endl;
}

signed main() {
	Node *n = new Node(1, new Node(2, new Node(4), new Node(5)), new Node(3, new Node(6), new Node(7)));
	connect(n);
	print(n);
	return 0;
}
```