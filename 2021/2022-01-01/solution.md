# Maximum Path Sum in Binary Tree

### Python
```python
class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def maxPathDown(n, mx):
	if not n: return 0
	left = max(0, maxPathDown(n.left, mx))
	right = max(0, maxPathDown(n.right, mx))
	mx[0] = max(mx[0], left+right+n.value)
	return max(left, right)+n.value

def maxPathSum(n):
	mx = [int(-1e9)]
	maxPathDown(n, mx)
	return mx[0]

n = Node(10, Node(2, Node(20), Node(1)), Node(10, None, Node(-25, Node(3), Node(4))))
print(maxPathSum(n))
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

int maxPathDown(Node *n, int &mx){
	if(!n) return 0;
	int left = max(0, maxPathDown(n->left, mx));
	int right = max(0, maxPathDown(n->right, mx));
	mx = max(mx, left+right+n->value);
	return max(left, right)+n->value;
}

int maxPathSum(Node *n){
	int ans=INT_MIN;
	maxPathDown(n, ans);
	return ans;
}

signed main() {
	Node *n = new Node(10, new Node(2, new Node(20), new Node(1)), new Node(10, NULL, new Node(-25, new Node(3), new Node(4))));
	cout << maxPathSum(n) << endl;
	return 0;
}
```