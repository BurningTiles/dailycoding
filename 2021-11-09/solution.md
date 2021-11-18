# Iterative In-Order Tree

### Python
```python
class Node:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def inorder(node):
	if node!=None:
		inorder(node.left)
		print(node.val, end=" ")
		inorder(node.right)

def inorder_iterative(node):
	s = []
	cur = node
	while cur!=None or len(s)>0:
		while cur!=None:
			s.append(cur)
			cur = cur.left
		cur = s[-1]
		del s[-1]
		print(cur.val, end=" ")
		cur = cur.right

n = Node(12, Node(6, Node(2), Node(3)), Node(4, Node(7), Node(8)))

inorder(n)
print()
inorder_iterative(n)
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

void inorder(Node *n){
	if(n){
		inorder(n->left);
		cout << n->value << " ";
		inorder(n->right);
	}
}

void inorder_iterative(Node *n){
	vector<Node*> s; // stack
	Node *cur = n;
	while(cur || s.size()){
		while(cur){
			s.push_back(cur);
			cur = cur->left;
		}
		cur = s.back();
		s.pop_back();
		cout << cur->value << " ";
		cur = cur->right;
	}
}

signed main() {
	Node *n = new Node(12, new Node(6, new Node(2), new Node(3)), new Node(4, new Node(7), new Node(8)));
	inorder(n);
	cout << endl;
	inorder_iterative(n);
	return 0;
}
```