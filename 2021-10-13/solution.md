# Target Sum from Root to Leaf

### Python
```python
class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def target_sum_bst(root, target, cur=0):
	if root==None:
		return cur
	cur += root.value
	ans = False
	if root.left!=None:
		ans = ans or target_sum_bst(root.left, target, cur)
	if root.right!=None:
		ans = ans or target_sum_bst(root.right, target, cur)
	if root.left==None and root.right==None:
		ans = target==cur
	return ans

#      1
#    /   \
#   2     3
#    \     \
#     6     4
n = Node(1, Node(2, None, Node(6)), Node(3, None, Node(4)))

print(target_sum_bst(n, 9))
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

bool target_sum_bst(Node *root, int target, int cur=0){
	if(!root) return target==cur;
	cur += root->value;
	bool ans = false;
	if(root->left)
		ans = ans | target_sum_bst(root->left, target, cur);
	if(root->right)
		ans = ans | target_sum_bst(root->right, target, cur);
	if(!root->left && !root->right)
		ans = target==cur;
	return ans;
}

signed main() {
	/*
	      1
	    /   \
	   2     3
	    \     \
	     6     4
	*/
	Node *n = new Node(1,new Node(2,NULL, new Node(6)), new Node(3, NULL, new Node(4)));
	
	cout << (target_sum_bst(n,9) ? "true" : "false") << endl;

	return 0;
}
```