# Array to Binary Search Tree

### Python
```python
class Node(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
	def __str__(self):
		return f"{self.val}, ({self.left}, {self.right})"

def sortedArrayToBST(nums, s=0, e=-1):
	if e<0: 
		e=len(nums)-1
	if e==s: 
		return Node(nums[s])
	if e-s==1:
		return Node(nums[e], sortedArrayToBST(nums, s, e-1))
	mid = (s+e)//2
	return Node(
		nums[mid],
		sortedArrayToBST(nums, s, mid-1),
		sortedArrayToBST(nums, mid+1, e)
	)

n = sortedArrayToBST([-10, -3, 0, 5, 9])
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

Node* sortedArrayToBST(vector<int> v, int s=0, int e=-1){
	if(e<0) e=v.size()-1;
	if(e==s) return new Node(v[s]);
	if(e-s==1) 
		return new Node(v[e], sortedArrayToBST(v, s, e-1));
	int mid = (s+e)/2;
	return new Node(v[mid], 
		sortedArrayToBST(v, s, mid-1),
		sortedArrayToBST(v, mid+1, e)
	);
}

void print(Node *n) {
	if(!n)
		cout << "Null";
	else {
		cout << n->value << ", (";
		print(n->left);
		cout << ", ";
		print(n->right);
		cout << ")";
	}
}

signed main() {
	Node *n = sortedArrayToBST({-10, -3, 0, 5, 9});
	print(n);
	return 0;
}
```