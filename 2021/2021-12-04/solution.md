# Flatten Binary Tree

### Python
```python
class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __repr__(self):
		return f"({self.value}, {self.left}, {self.right})"

def bfs(n, ans):
	if n==None: return
	ans.append(n)
	bfs(n.left, ans)
	bfs(n.right, ans)

def flatten_bst(root):
	if n==None: return
	a = []
	bfs(root, a)
	a.append(None)
	for i in range(len(a)-1):
		a[i].left = None
		a[i].right = a[i+1]

n = Node(1, Node(2, Node(5)), Node(3, Node(4)))

flatten_bst(n)
print(n)
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

void bfs(Node *n, vector<Node*> &ans){
	if(!n) return;
	ans.push_back(n);
	bfs(n->left, ans);
	bfs(n->right, ans);
}

void flatten_bst(Node *n){
	if(!n) return;
	vector<Node*> v;
	bfs(n, v);
	v.push_back(NULL);
	for(int i=0; i<v.size()-1; i++)
		v[i]->left = NULL,
		v[i]->right = v[i+1];
}

void print(Node *n){
	if(!n) {
		cout << "None";
		return;
	}
	cout << "(" << n->value << ", ";
	print(n->left);
	cout << ", ";
	print(n->right);
	cout << ")";
}

signed main() {
	Node *n = new Node(1, new Node(2, new Node(5)), new Node(3, new Node(4)));
	
	flatten_bst(n);
	print(n);
	return 0;
}
```