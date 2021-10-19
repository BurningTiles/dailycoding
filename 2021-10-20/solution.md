# Root to leaf numbers summed

### Python
```python
class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __repr__(self):
		return f"({self.value}, {self.left}, {self.right})"

def bst_numbers_sum(root, cur=0):
	ans = 0
	if root!=None:
		cur *= 10
		cur += root.value
		if root.left!=None or root.right!=None:
			if root.left!=None:
				ans += bst_numbers_sum(root.left, cur)
			if root.right!=None:
				ans += bst_numbers_sum(root.right, cur)
		else:
			return cur
	return ans

n = Node(1, Node(2, Node(4), Node(5)), Node(3))
#      1
#    /   \
#   2     3
#  / \
# 4   5

print(bst_numbers_sum(n))
# 262
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

long long bst_numbers_sum(Node *root, long long cur=0){
	int ans=0;
	if(root){
		cur *= 10;
		cur += root->value;
		if(root->left || root->right){
			if(root->left)
				ans += bst_numbers_sum(root->left, cur);
			if(root->right)
				ans += bst_numbers_sum(root->right, cur);
		}
		else
			return cur;
	}
	return ans;
}

signed main() {
	Node *root = new Node(1, new Node(2, new Node(4), new Node(5)), new Node(3));
	
	cout << bst_numbers_sum(root);

	return 0;
}
```