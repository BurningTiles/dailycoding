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

def node_to_list(root, lst):
	if root!=None:
		lst.append(root)
		node_to_list(root.left, lst)
		node_to_list(root.right, lst)

def flatten_bst(root):
	lst = []
	node_to_list(root, lst)
	for i in range(len(lst)-1):
		lst[i].left = None
		lst[i].right = lst[i+1]
	if len(lst)>0:
		lst[-1].left, lst[-1].right = None, None

n = Node(1, Node(2, Node(5)), Node(3, Node(4)))
print("Before:")
print(n)
#      1
#    /   \
#   2     3
#  /     /
# 5     4

flatten_bst(n)
print("After:")
print(n)
# n1 should now look like
#   1
#    \
#     2
#      \
#       5
#        \
#         3
#          \
#           4
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

void node_to_vector(Node *root, vector<Node*> &v) {
	if(root){
		v.push_back(root);
		node_to_vector(root->left, v);
		node_to_vector(root->right, v);
	}
}

void flatten_bst(Node *root) {
	vector<Node *> v;
	node_to_vector(root, v);
	for(int i=0; i<v.size()-1; i++){
		v[i]->left = NULL;
		v[i]->right = v[i+1];
	}
	if(v.size())
		v.back()->left = v.back()->right = NULL;
}

void print(Node *n){
	if(n){
		cout << "(" << n->value << ", ";
		print(n->left);
		cout << ", ";
		print(n->right);
		cout << ")";
	}
	else
		cout << "null";
}

signed main() {
	Node *root = new Node(1, new Node(2, new Node(5)), new Node(3, new Node(4)));
	
	cout << "Before:\n";
	print(root);

	flatten_bst(root);

	cout << "\n\nAfter:\n";
	print(root);

	return 0;
}
```