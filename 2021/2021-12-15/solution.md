# Find Bottom Left Tree Value

### Python
```python
class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right



def findLeftmost(root):
	ans = [0, -1]	
	def helper(n, cur_depth=0):
		if n:
			if cur_depth>ans[1]:
				ans[1] = cur_depth
				ans[0] = n.value
			helper(n.left, cur_depth+1)
			helper(n.right, cur_depth+1)
	helper(root)
	return ans[0]

n = Node(2, Node(1), Node(3))
print(findLeftmost(n))

n = Node(1, Node(2, Node(4)), Node(3, Node(5, Node(7)), Node(6)))
print(findLeftmost(n))
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

void helper(Node *n, int &depth, int &ans, int cur_depth=0){
	if(n){
		if(cur_depth>depth){
			depth = cur_depth;
			ans = n->value;
		}
		helper(n->left, depth, ans, cur_depth+1);
		helper(n->right, depth, ans, cur_depth+1);
	}
}

int findLeftmost(Node *n){
	int ans=0, depth=-1;
	helper(n, depth, ans);
	return ans;
}

signed main() {
	Node *n = new Node(2, new Node(1), new Node(3));
	cout << findLeftmost(n) << endl; 

	n = new Node(1, new Node(2, new Node(4)), new Node(3, new Node(5, new Node(7)), new Node(6)));
	cout << findLeftmost(n) << endl;  

	return 0;
}
```