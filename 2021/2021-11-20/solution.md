# Level Order Traversal of Binary Tree

### Python
```python
class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right
	
def print_level_order(n):
	dq = [n]
	while len(dq)>0:
		n = dq[0]
		del dq[0]
		if n==None: continue
		print(n.value, end=" ")
		dq.append(n.left)
		dq.append(n.right)
	print()

n = Node(1, Node(2), Node(3, Node(4), Node(5)))
print_level_order(n)
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

class Node{
	public:
	int value;
	Node *left, *right;
	Node(int v, Node *l=NULL, Node *r=NULL)
		:value{v}, left{l}, right{r} {}
};

void print_level_order(Node *n){
	deque<Node*> dq={n};
	while(dq.size()){
		n = dq.front();
		dq.pop_front();
		if(!n) continue;
		cout << n->value << " ";
		dq.push_back(n->left);
		dq.push_back(n->right);
	}
	cout << endl;
}

signed main() {
	Node *n = new Node(1, new Node(2), new Node(3, new Node(4), new Node(5)));
	print_level_order(n);
	return 0;
}
```