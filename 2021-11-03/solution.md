# Leaf-Similar Trees

### Python
```python
class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def getLeafs(node, leafs):
	if node==None:
		return
	if node.left==None and node.right==None:
		leafs.append(node.value)
	if node.left!=None:
		getLeafs(node.left, leafs)
	if node.right!=None:
		getLeafs(node.right, leafs)

def leafSimilar(n1, n2):
	l1, l2 = [], []
	getLeafs(n1, l1)
	getLeafs(n2, l2)
	if len(l1)==len(l2):
		for i in range(len(l1)):
			if l1[i]!=l2[i]:
				return False
		return True
	return False

#     3
#    / \ 
#   5   1
#  / \
# 6   2 
t1 = Node(3, Node(5, Node(6), Node(2)), Node(1))

#     7
#    / \ 
#   2   1
#  / \
# 6   2 
t2 = Node(7, Node(2, Node(6), Node(2)), Node(1))


print(leafSimilar(t1, t2))
```

### C++
```cpp
#include <bits/stdc++.h>
#define toBool(x) (x ? "true" : "false")
using namespace std;

class Node{
	public:
	int value;
	Node *left, *right;
	Node(int v, Node *l=NULL, Node *r=NULL)
		:value{v}, left{l}, right{r} {}
};

void getLeafs(Node *n, vector<int> &v){
	if(!n) return;
	if(!n->left && !n->right)
		v.push_back(n->value);
	if(n->left)
		getLeafs(n->left, v);
	if(n->right)
		getLeafs(n->right, v);
}

bool leafSimilar(Node *n1, Node *n2){
	vector<int> v1, v2;
	getLeafs(n1, v1);
	getLeafs(n2, v2);
	if(v1.size() == v2.size()){
		for(int i=0; i<v1.size(); i++)
			if(v1[i]!=v2[i]) return false;
		return true;
	}
	return false;
}

signed main() {
	Node *n1 = new Node(3, new Node(5, new Node(6), new Node(2)), new Node(1));
	Node *n2 = new Node(7, new Node(2, new Node(6), new Node(2)), new Node(1));
	cout << toBool(leafSimilar(n1, n2)) << endl;
	return 0;
}
```